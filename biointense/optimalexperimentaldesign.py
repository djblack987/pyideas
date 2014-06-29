# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:39:49 2013

@author: Timothy Van Daele; Stijn Van Hoey

0.1 Class version of the ODE generator package
"""

from __future__ import division
import sys
import os
import datetime
import numpy as np
import scipy as sp
import sympy

import pandas as pd
from scipy import optimize,stats
from itertools import combinations

if sys.hexversion > 0x02070000:
    import collections
else:
    import ordereddict as collections

from plotfunctions import *
from matplotlib.ticker import MaxNLocator
from ode_generator import DAErunner
from measurements import ode_measurements
from ode_optimization import ode_optimizer

from random import Random
from time import time
import inspyred #Global optimization

class ode_FIM(object):
    '''
    OED aimed class functioning
    
    Deliverables:
    - FIM calcluation based on odegenerator model sensitivities
    - link with optimization algorithms for optimization of designs
    
    AIM:
    - Link with robust OED -> sequential design (paropt - exp-opt - paropt)
    '''
    
    def __init__(self, odeoptimizer, sensmethod = 'analytical',*args,**kwargs): #Measurements
        '''
        Measurements: measurements-class instance
        
        Parameters
        -----------
        sensmethod: analytical|numerical
            analytical is not always working, but more accurate, since not dependent
            on a selected perturbation factor for sensitivity calculation              
        
        '''
        if kwargs.get('print_on') == None:
            self._print_on = True
        else:
            self._print_on = kwargs.get('print_on')        
        
        if isinstance(odeoptimizer, ode_optimizer):
            self.odeoptimizer = odeoptimizer
        else:
            raise Exception('Input class is ode_optimizer instance!')
        
        self._model = odeoptimizer._model
        self._data = odeoptimizer._data
        self.Error_Covariance_Matrix = odeoptimizer._data._Error_Covariance_Matrix
        self.Error_Covariance_Matrix_PD = odeoptimizer._data._Error_Covariance_Matrix_PD
        self.Parameters = odeoptimizer._get_fitting_parameters()
        
        self.criteria_optimality_info = {'A':'min', 'modA': 'max', 'D': 'max', 
                                         'E':'max', 'modE':'min'}
        
        #initially set all measured variables as included
        self.set_variables_for_FIM(self.get_measured_outputs())
        
        #Run sensitivity
        if  self._data.get_measured_xdata()[0] == 0.:
            self._model._Time = self._data.get_measured_xdata()
        else:
            self._model._Time = np.concatenate((np.array([0.]),self._data.get_measured_xdata()))
        
#        self._model._Time = np.concatenate((np.array([0.]),self._data.get_measured_times()))
        if sensmethod == 'analytical':
            self._model.calcAlgLSA()
            self.sensitivities = dict(self._model.getAlgLSA.items())
        elif sensmethod == 'numerical':
            self._model.numeric_local_sensitivity(*args,**kwargs)
            self.sensitivities = self._model.numerical_sensitivity           
        self._model.set_time(self._model._TimeDict)
        #
        self.get_FIM()
        self.selected_criterion = None
        self.time_max = None
        self.time_min = None
        self.number_of_samples = None
        
    def get_all_outputs(self):
        '''
        returns all model variables in the current model
        '''
        return self._model._Outputs

    def get_measured_outputs(self):
        '''
        '''
        if sorted(self._model.get_measured_outputs()) != sorted(self._data.get_measured_outputs()):
            raise Exception('Model and Data measured variables are not in line with eachother.')
        return self._data.get_measured_outputs()
        
    def get_variables_for_FIM(self):
        '''variables for FIM calculation
        '''
        return self._FIMvariables

    def set_variables_for_FIM(self, varlist):
        '''variables for FIM calculation
        '''
        for var in varlist:
            if not var in self.get_measured_outputs():
                raise Exception('Variabel %s not measured')
        self._FIMvariables = varlist

    def test_extra_measured_timesteps(self, variable, timesteps):
        '''
        to change...
        input Dictionary: {'variables':[var of measurement], 'time': [timeindex of measurement]}
        '''      
        raise Exception('not working yet!')
#        newdata = pd.DataFrame(vartimedict).pivot(index='time', columns='variables')
        
        #The timesteps for these measurements need to be used and new FIM calculated
        # First, an update of sensitivities and error covariance matrix 
        # second, new FIM + criteria
        
        #combine with current data
        olddata = self._data.Data.copy()
        for timestep in timesteps:
            if timestep in olddata.index:
                if np.isnan(olddata[variable][timestep]):
                    olddata[variable][timestep] == -99.
                else:
                    raise Exception('Timestep ',timestep, 'already addressed as measurement')
            else:
                olddata #concatanate!!!
            
    def _get_nonFIM(self):
        '''
        '''
        return [x for x in self.get_measured_outputs() if not x in self.get_variables_for_FIM()]

    def get_newFIM(self):
        '''
        '''
        self.sensmatrix = np.zeros([len(self._data.get_measured_xdata()),len(self.Parameters),len(self.get_all_outputs())])
        #create sensitivity matrix
        for i, var in enumerate(self.get_measured_outputs()):
            self.sensmatrix[:,:,i] = np.array(self.sensitivities[var][1:])

        self.FIM_timestep = np.einsum('ijk,ilm->ijl',np.einsum('ijk,ill->ijl',self.sensmatrix,\
                               np.linalg.inv(np.atleast_3d(self.Error_Covariance_Matrix_PD))),self.sensmatrix)
        
        self.FIM = np.sum(self.FIM_timestep, axis = 0)
        return self.FIM

    def get_FIM(self):
        '''  
        TOMORROW!!!! eerst nonFIM dan nans eruit!!
        
        Based on the measurement errors and timesteps to include evaluation,
        the FIM is calculated
        
        calculate e FIM for each timestep and a combine FIM
        
        Notes
        ------
        
        '''        
        
        self.FIM = np.zeros((len(self.Parameters),len(self.Parameters)))
        self.FIM_timestep = {}
        
        Qerr = self.Error_Covariance_Matrix.copy()
        
        check_for_empties=False
        for timestep in self._data.get_measured_xdata():
            #select subset of Error Covariance based on variables selected for FIM
            for varnot in self._get_nonFIM():
                Qerr[timestep] = Qerr[timestep].drop(varnot,axis=1).drop(varnot)
            
            #control if there is a measured value for this timestep 
            #for all used values (check Error Covariance, since this one is prepared)
            if Qerr[timestep].empty:
                check_for_empties = True
            else:
                #GET SENS_MATRIX
                #varibales in time that are available
                nbvar = Qerr[timestep].shape[0]
                
                sensmatrix = np.zeros((nbvar,len(self.Parameters)))
                #create sensitivity amtrix
                for i, var in enumerate(Qerr[timestep].columns):
                    sensmatrix[i,:] = np.array(self.sensitivities[var][self.Parameters.keys()].xs(timestep))
    
                #calculate matrices
                FIMt = np.matrix(sensmatrix).transpose() * np.linalg.inv(np.matrix(Qerr[timestep])) * np.matrix(sensmatrix)
                self.FIM = self.FIM + FIMt
                self.FIM_timestep[timestep] = FIMt
        if check_for_empties == True and self._print_on:
            print('Not all timesteps are evaluated')
        return self.FIM

    def _check_for_FIM(self):
        ''' help function for FIM testing
        If FIM exists, ok, otherwise start FIM calculation
        '''  
        try:
            self.FIM
        except:
            if self._print_on:
                print('FIM matrix is calculated...')
            self.get_FIM()
            if self._print_on:
                print('... done!')

    def A_criterion(self, *args):
        '''OED design A criterion
        With this criterion, the trace of the inverse of the FIM is minimized, 
        which is equivalent to minimizing the sum of the variances of the 
        parameter estimates. In other words, this criterion minimizes the 
        arithmetic average of the variances of the parameter estimate. 
        Because this criterion is based on an inversion of the FIM, 
        numerical problems will arise when the FIM is close to singular.        
        '''
        if args:
            FIM = args[0]
        else:
            self._check_for_FIM()
            FIM = self.FIM
        if self._print_on:
            print('MINIMIZE A criterion for OED')
        return np.linalg.inv(FIM).trace()
        
    def modA_criterion(self, *args):
        '''OED design modified A criterion
        With this criterion, the trace of the inverse of the FIM is minimized, 
        which is equivalent to minimizing the sum of the variances of the 
        parameter estimates. In other words, this criterion minimizes the 
        arithmetic average of the variances of the parameter estimate. 
        Because this criterion is based on an inversion of the FIM, 
        numerical problems will arise when the FIM is close to singular.        
        '''
        if args:
            FIM = args[0]
        else:
            self._check_for_FIM()
            FIM = self.FIM            
        if self._print_on:
            print('MAXIMIZE modA criterion for OED')
        return FIM.trace()                   
        
    def D_criterion(self, *args):
        '''OED design D criterion
        Here, the idea is to maximize the determinant of the FIM 
        (Box and Lucas, 1959). The latter is inversely proportional to the 
        volume of the confidence region of the parameter es- timates, and this 
        volume is thus minimized when maximizing det (FIM). In other words, 
        one minimizes the geometric average of the variances of the parameter 
        estimates. More- over, D-optimal experiments possess the property of 
        being invariant with respect to any rescaling of the parameters 
        (Petersen, 2000; Seber and Wild, 1989). According to Walter and 
        Pronzato (1997), the D-optimal design criterion is the most used 
        criterion. However, several authors have pointed out that this 
        criterion tends to give excessive importance to the parameter which 
        is most influential.
        '''
        if args:
            FIM = args[0]
        else:
            self._check_for_FIM()
        if self._print_on:
            print('MAXIMIZE D criterion for OED')
        return np.linalg.det(FIM)   

    def E_criterion(self, *args):
        '''OED design E criterion
        The E-optimal design criterion maximizes the smallest eigenvalue of 
        the FIM and thereby minimizes the length of the largest axis of the 
        confidence ellipsoid. Thus, these designs aim at minimizing the 
        largest parameter estimation variance and thereby at maximizing the 
        distance from the singular, unidentifiable case.
        '''
        if args:
            FIM = args[0]
        else:
            self._check_for_FIM()
            FIM = self.FIM
        if self._print_on:
            print('MAXIMIZE E criterion for OED')
        w, v = np.linalg.eig(FIM)
        return min(w)
    
    def modE_criterion(self, *args):
        '''OED design modE criterion
        With this criterion, the focus is on the minimization of the condition 
        number, which is the ratio between the largest and the smallest 
        eigenvalue, or, in other words, the ratio of the shortest and the 
        longest ellipsoid axes. The minimum of this ratio is one, which 
        corresponds to the case where the shape of the confidence ellipsoid 
        is a (hyper)sphere.
        '''
        if args:
            FIM = args[0]
        else:
            self._check_for_FIM()
            FIM = self.FIM
        if self._print_on:
            print('MINIMIZE modE criterion for OED')
        w, v = np.linalg.eig(FIM)
        return max(w)/min(w)

    def get_all_optimality_design_criteria(self):
        '''Return all optimality criteria
        
        '''
        self._check_for_FIM()
        self._all_crit = {'A':self.A_criterion(), 'modA': self.modA_criterion(), 
                          'D': self.D_criterion(), 'E':self.E_criterion(), 'modE':self.modE_criterion()}
        return self._all_crit
        
    def get_parameter_correlation(self):
        '''Calculate correlations between parameters
            
        Returns
        --------
        R: pandas DataFrame
            Contains for each parameter the correlation with all the other
            parameters.
        
        '''
        self._check_for_FIM()
        ECM = self.FIM.I
        self.ECM = ECM
        
        R = np.zeros(ECM.shape)
        
        for i in range(0,len(ECM)):
            for j in range(0,len(ECM)):
                R[i,j] = ECM[i,j]/(np.sqrt(ECM[i,i]*ECM[j,j]))
        
        R = pd.DataFrame(R,columns=self.Parameters.keys(),index=self.Parameters.keys())     
        
        self.parameter_correlation = R
        return R
        
        
    def get_parameter_confidence(self, alpha = 0.95):
        '''Calculate confidence intervals for all parameters
        
        Parameters
        -----------
        alpha: float
            confidence level of a two-sided student t-distribution (Do not divide 
            the required alpha value by 2). For example for a confidence level of 
            0.95, the lower and upper values of the interval are calculated at 0.025 
            and 0.975.
        
        Returns
        --------
        CI: pandas DataFrame
            Contains for each parameter the value of the variable, lower and 
            upper value of the interval, the delta value which represents half 
            the interval and the relative uncertainty in percent.
        
        '''
        self._check_for_FIM()
        self.ECM = self.FIM.I

        CI = np.zeros([self.ECM.shape[1],8]) 
        n_p = sum(self._data.Data.count())-len(self.Parameters)
        
        CI[:,0] = self.Parameters.values()
        for i,variance in enumerate(np.array(self.ECM.diagonal())[0,:]):
            #TODO check whether sum or median or... should be used 
            #TODO Check of de absolute waarde hier gebruikt mag worden!!!!
            CI[i,1:3] =  stats.t.interval(alpha, n_p, loc=self.Parameters.values()[i],scale=np.sqrt(abs(variance)))
            #print stats.t.interval(alpha,self._data.Data.count()-len(self.Parameters),scale=np.sqrt(var))[1][0]
            CI[i,3] = stats.t.interval(alpha, n_p, scale=np.sqrt(abs(variance)))[1]
        CI[:,4] = abs(CI[:,3]/self.Parameters.values())*100
        CI[:,5] = self.Parameters.values()/np.sqrt(abs(self.ECM.diagonal()))
        CI[:,6] = stats.t.interval(alpha, n_p)[1]
        for i in np.arange(self.ECM.shape[1]):
            CI[i,7] = 1 if CI[i,5]>=CI[i,6] else 0
        
        if self._print_on:
            if (CI[:,7]==0).any():
                print('Some of the parameters show a non significant t_value, which\
                suggests that the confidence intervals of that particular parameter\
                include zero and such a situation means that the parameter could be\
                statistically dropped from the model. However it should be noted that\
                sometimes occurs in multi-parameter models because of high correlation\
                between the parameters.')
            else:
                print('T_values seem ok, all parameters can be regarded as reliable.')
            
        CI = pd.DataFrame(CI,columns=['value','lower','upper','delta','percent','t_value','t_reference','significant'],index=self.Parameters.keys())
        
        self.parameter_confidence = CI
        
        return CI
    
    def get_model_prediction_ECM(self):
        '''Calculate model prediction error covariance matrix
               
        Returns
        --------
        model_prediction_ECM: pandas DataFrame
            Contains for every timestep the corresponding model prediction
            error covariance matrix.
        
        '''
        self._check_for_FIM()
        self.ECM = self.FIM.I
        
        time_len = len(self._data.get_measured_xdata())
        par_len = len(self.Parameters)
        var_len = len(self.get_all_outputs())
           
        omega = np.zeros([time_len,var_len,var_len])
        #Mask parameter correlations!
        ECM = np.multiply(self.ECM,np.eye(par_len))
        sens_step = np.zeros([par_len,var_len])
        
        for j,timestep in enumerate(self._data.get_measured_xdata()):
            for i, var in enumerate(self.sensitivities.values()):
                sens_step[:,i] = var.ix[timestep]
            omega[j,:,:] = sens_step.T*ECM*sens_step
              
        self.model_prediction_ECM = omega
        
        return omega
    
    def get_model_confidence(self, alpha=0.95):
        '''Calculate confidence intervals for variables
        
        Parameters
        -----------
        alpha: float
            confidence level of a two-sided student t-distribution (Do not divide 
            the required alpha value by 2). For example for a confidence level of 
            0.95, the lower and upper values of the interval are calculated at 0.025 
            and 0.975.
        
        Returns
        --------
        model_confidence: dict
            Contains for each variable a pandas DataFrame which contains for 
            every timestep the value of the variable,lower and upper value of 
            the interval, the delta value which represents half the interval 
            and the relative uncertainty in percent.
        
        '''
        time_len = len(self._data.get_measured_xdata())
        par_len = len(self.Parameters)
           
        sigma = {}
        np.zeros([time_len,5])
        
        if self._data.get_measured_xdata()[0] == 0:
            time_uncertainty = self._data.get_measured_xdata()[1:]
        else:
            time_uncertainty = self._data.get_measured_xdata()

        for i,var in enumerate(self.get_measured_outputs()):
            sigma_var = np.zeros([time_len,5])
            sigma_var[0,0:3] = self._model.algeb_solved[var].ix[0]
            for j,timestep in enumerate(time_uncertainty):
                sigma_var[j,0] = self._model.algeb_solved[var].ix[timestep]
                sigma_var[j,1:3] = stats.t.interval(alpha,sum(self._data.Data.count())-par_len,loc=sigma_var[j,0],scale=np.sqrt(self.model_prediction_ECM[j,:,:].diagonal()[i]))
                sigma_var[j,3] = abs((sigma_var[j,2]-sigma_var[j,0]))
                sigma_var[j,4] = abs(sigma_var[j,3]/sigma_var[j,0])*100
            sigma_var = pd.DataFrame(sigma_var,columns=['value','lower','upper','delta','percent'],index=self._data.get_measured_xdata())       
            sigma[var] = sigma_var
        
        self.model_confidence = sigma
        return sigma

        
    def get_model_correlation(self, alpha = 0.95):
        '''Calculate correlation between variables
        
        Parameters
        -----------
        alpha: float
            confidence level of a two-sided student t-distribution (Do not divide 
            the required alpha value by 2). For example for a confidence level of 
            0.95, the lower and upper values of the interval are calculated at 0.025 
            and 0.975.
        
        Returns
        --------
        model_correlation: pandas DataFrame
            For every possible combination of variables a column is made which
            represents the correlation between the two variables.
        
        '''
        time_len = len(self._data.get_measured_xdata())
        
        if len(self.get_all_outputs()) == 1:
            if self._print_on:
                print('Model only has one output!')
            corr = pd.DataFrame(np.ones([1,1]), columns=self.get_all_outputs()[0],index=self._data.get_measured_xdata())
        else:
            comb_gen = list(combinations(self.get_all_outputs(), 2))
            print(comb_gen)
            for i,comb in enumerate(comb_gen):
                if i is 0:
                    combin = [comb[0] + '-' +comb[1]]
                else:
                    combin.append([comb[0] + '-' +comb[1]])
                    
            if self._data.get_measured_xdata()[0] == 0:
                time_uncertainty = self._data.get_measured_xdata()[1:]
            else:
                time_uncertainty = self._data.get_measured_xdata()
            
            corr = np.zeros([time_len, len(combin)])
            for h,timestep in enumerate(time_uncertainty):
                tracker = 0
                for i,var1 in enumerate(self.get_all_outputs()[:-1]):
                    for j,var2 in enumerate(self.get_all_outputs()[i+1:]):
                        corr[h, tracker] = self.model_prediction_ECM[h,i,j+1]/np.sqrt(self.model_prediction_ECM[h,i,i]*self.model_prediction_ECM[h,j+1,j+1])
                        tracker += 1          
                        
            corr = pd.DataFrame(corr, columns=combin,index=self._data.get_measured_xdata())                    
            self.model_correlation = corr
            return corr
        
    def get_model_adequacy(self, variable):
        '''
        TODO!
        '''
        
        repeated_meas = self._data.Data[variable].count()
        n_p_r = self._data.Data.count()-len(self.Parameters)-repeated_meas
        s_squared = sum(self._data.Data[variable]-self._model.algeb_solved[variable])/repeated_meas
        
        F = ((Sr_theta - repeated_meas*s_squared)/(n_p_r))/(s_squared)
        
        if self._print_on:
            print(stats.f_value(s_squared,0,n_p_r,1000))
    
    def _get_objective(self, candidates, args):
        '''
        '''
        fitness = []
        for cs in candidates:
            fitness.append(self._evaluator(np.sum(self._FIM_interp1d(cs),axis = 2)))
        return fitness
        
    def _sample_generator(self,random,args):
        '''
        '''
        if not self.time_max or self.time_min == None or not self.number_of_samples:
            raise Exception('Set number of samples, min time and max time!')
        
        sample_times = []
        #use get_fitting_parameters, since this is ordered dict!!
        for i in range(self.number_of_samples):
            sample_times.append(random.random()*(self.time_max - self.time_min))
        return sample_times
        
    def _bounder_generator(self):
        '''
        '''
        minsample = list(np.zeros(self.number_of_samples)+self.time_min)
        maxsample = list(np.zeros(self.number_of_samples)+self.time_max)
        return minsample, maxsample  
        
    def calc_Error_Covariance_Matrix(self, measerr, method = 'absolute'):
        '''
        '''
        self._ECM_PD = self._model.algeb_solved.copy()
        if method == 'absolute':
            for var in self._data.Data.columns:
                self._ECM_PD[var] = 0.0*self._ECM_PD[var] + measerr[var]**2.  #De 1/sigma^2 komt bij inv berekening van FIM
                
        elif method == 'relative':   
            #Error covariance matrix PD
            for var in self.Data.columns:
                measerr = self.Meas_Errors[var]
                self._ECM_PD[var] = (measerr[var]*self._ECM_PD[var])**2.
        
    def OED_inner(self, criterion, approach = 'PSO', sensmethod = 'analytical', prng = None, pop_size = 16, max_eval = 256, add_plot = False):
        '''
        '''
        self.selected_criterion = criterion
        
        if self.selected_criterion not in self.criteria_optimality_info:
            raise Exception('First set the variable self.selected_criterion to the criterion of interest!')
        else:
            if self.criteria_optimality_info[self.selected_criterion] == 'max':
                maximize = True
            else:
                maximize = False
                
        self._model._Time = np.linspace(self.time_min, self.time_max, 1e7)
        if sensmethod == 'analytical':
            self._model.calcAlgLSA()
            self.sensitivities = dict(self._model.getAlgLSA.items())
        elif sensmethod == 'numerical':
            self._model.numeric_local_sensitivity(*args,**kwargs)
            self.sensitivities = self._model.numerical_sensitivity   
        
        sensmatrix = np.zeros([len(self._model._Time),len(self.Parameters),len(self.get_all_outputs())])
        
        for i, var in enumerate(self.get_measured_outputs()):
            sensmatrix[:,:,i] = np.array(self.sensitivities[var])
            
        self.calc_Error_Covariance_Matrix(self._data.Meas_Errors, method = self._data.Meas_Errors_type)
        
        FIM_timestep = np.einsum('ijk,ilm->ijl',np.einsum('ijk,ill->ijl',sensmatrix,\
                               np.linalg.inv(np.atleast_3d(self._ECM_PD))),sensmatrix)
            
        self._FIM_interp1d = sp.interpolate.interp1d(self._model._Time, FIM_timestep.T)

        if self.selected_criterion == 'A':
            self._evaluator = self.A_criterion
        elif self.selected_criterion == 'modA':
            self._evaluator = self.modA_criterion
        elif self.selected_criterion == 'D':
            self._evaluator = self.D_criterion
        elif self.selected_criterion == 'E':
            self._evaluator = self.E_criterion
        else:
            self._evaluator = self.modE_criterion
                
        #OPTIMIZATION
        if prng is None:
            prng = Random()
            prng.seed(time()) 
        
        if approach == 'PSO':
            ea = inspyred.swarm.PSO(prng)
        elif approach == 'DEA':
            ea = inspyred.ec.DEA(prng)
        elif approach == 'SA':
            ea = inspyred.ec.SA(prng)
        else:
            raise Exception('This approach is currently not supported!')
            
        lower_bound, upper_bound = self._bounder_generator()

        ea.terminator = inspyred.ec.terminators.evaluation_termination
        final_pop = ea.evolve(generator=self._sample_generator, 
                              evaluator=self._get_objective, 
                              pop_size=pop_size, 
                              bounder=inspyred.ec.Bounder(lower_bound = lower_bound, upper_bound = upper_bound),
                              maximize=maximize,
                              max_evaluations=max_eval)#3000

        #put the best of the last population into the class attributes (WSSE, pars)
       # self.optimize_evolution = pd.DataFrame(np.array(self.optimize_evolution),columns=self._get_fitting_parameters().keys()+['WSSE'])
        self._model.set_time(self._model._TimeDict)
                              
        # Sort and print the best individual, who will be at index 0.
        if add_plot == True:
            self._add_optimize_plot()

                              
        final_pop.sort(reverse=True)
        return final_pop, ea


    
    
    
    
