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
import sympy

import pandas as pd
from scipy import optimize

if sys.hexversion > 0x02070000:
    import collections
else:
    import ordereddict as collections

from plotfunctions import *
from matplotlib.ticker import MaxNLocator
from ode_generator import odegenerator
from measurements import ode_measurements
from ode_optimization import ode_optimizer

class ode_FIM(object):
    '''
    OED aimed class functioning
    
    Deliverables:
    - FIM calcluation based on odegenerator model sensitivities
    - link with optimization algorithms for optimization of designs
    
    AIM:
    - Link with robust OED -> sequential design (paropt - exp-opt - paropt)
    '''
    
    def __init__(self, odeoptimizer, sensmethod = 'analytical'): #Measurements
        '''
        Measurements: measurements-class instance
        
        Parameters
        -----------
        sensmethod: analytical|numerical
            analytical is ot always working, but more accurate, since not dependent
            on a selected perturbation factor for sensitivity calcluation              
        
        '''
        if isinstance(odeoptimizer, ode_optimizer):
            self.odeoptimizer = odeoptimizer
        else:
            raise Exception('Input class is ode_optimizer instance!')
        
        self._model = odeoptimizer._model
        self._data = odeoptimizer._data
        self.Error_Covariance_Matrix = odeoptimizer._data._Error_Covariance_Matrix
        self.Parameters = odeoptimizer._model.Parameters
        
        self.criteria_optimality_info = {'A':'min', 'modA': 'max', 'D': 'max', 
                                         'E':'max', 'modE':'min'}
        
        #initially set all measured variables as included
        self.set_variables_for_FIM(self.get_measured_variables())
        
        #Run sensitivity
        if  self._data.get_measured_times()[0] == 0.:
            self._model._Time = self._data.get_measured_times()
        else:
            self._model._Time = np.concatenate((np.array([0.]),self._data.get_measured_times()))
        
#        self._model._Time = np.concatenate((np.array([0.]),self._data.get_measured_times()))
        if sensmethod == 'analytical':
            self._model.analytic_local_sensitivity()
            self.sensitivities = self._model.analytical_sensitivity
        elif sensmethod == 'numerical':
            self._model.numeric_local_sensitivity()
            self.sensitivities = self._model.numerical_sensitivity           
        self._model.set_time(self._model._TimeDict)
        #
        self.get_FIM()        
        
    def get_all_variables(self):
        '''
        returns all model variables in the current model
        '''
        return self._model._model.get_variables()

    def get_measured_variables(self):
        '''
        '''
        if sorted(self._model.get_measured_variables()) != sorted(self._data.get_measured_variables()):
            raise Exception('Model and Data measured variables are not in line with eachother.')
        return self._data.get_measured_variables()
        
    def get_variables_for_FIM(self):
        '''variables for FIM calculation
        '''
        return self._FIMvariables

    def set_variables_for_FIM(self, varlist):
        '''variables for FIM calculation
        '''
        for var in varlist:
            if not var in self.get_measured_variables():
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
        return [x for x in self.get_measured_variables() if not x in self.get_variables_for_FIM()]

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
        for timestep in self._data.get_measured_times():
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
                    sensmatrix[i,:] = np.array(self.sensitivities[var].xs(timestep))
    
                #calculate matrices
                FIMt = np.matrix(sensmatrix).transpose() * np.linalg.inv(np.matrix(Qerr[timestep])) * np.matrix(sensmatrix)
                self.FIM = self.FIM + FIMt
                self.FIM_timestep[timestep] = FIMt
        if check_for_empties == True:
            print 'Not all timesteps are evaluated'
        return self.FIM

    def _check_for_FIM(self):
        ''' help function for FIM testing
        If FIM exists, ok, otherwise start FIM calculation
        '''  
        try:
            self.FIM
        except:
            print 'FIM matrix is calculated...'
            self.get_FIM()
            print '... done!'

    def A_criterium(self):
        '''OED design A criterium
        With this criterion, the trace of the inverse of the FIM is minimized, 
        which is equivalent to minimizing the sum of the variances of the 
        parameter estimates. In other words, this criterion minimizes the 
        arithmetic average of the variances of the parameter estimate. 
        Because this criterion is based on an inversion of the FIM, 
        numerical problems will arise when the FIM is close to singular.        
        '''
        self._check_for_FIM()
        print 'MINIMIZE A criterium for OED'
        return self.FIM.I.trace()
        
    def modA_criterium(self):
        '''OED design modified A criterium
        With this criterion, the trace of the inverse of the FIM is minimized, 
        which is equivalent to minimizing the sum of the variances of the 
        parameter estimates. In other words, this criterion minimizes the 
        arithmetic average of the variances of the parameter estimate. 
        Because this criterion is based on an inversion of the FIM, 
        numerical problems will arise when the FIM is close to singular.        
        '''
        self._check_for_FIM()
        print 'MAXIMIZE modA criterium for OED'
        return self.FIM.trace()                   
        
    def D_criterium(self):
        '''OED design D criterium
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
        self._check_for_FIM()
        print 'MAXIMIZE D criterium for OED'
        return np.linalg.det(self.FIM)          
    
    def E_criterium(self):
        '''OED design E criterium
        The E-optimal design criterion maximizes the smallest eigenvalue of 
        the FIM and thereby minimizes the length of the largest axis of the 
        confidence ellipsoid. Thus, these designs aim at minimizing the 
        largest parameter estimation variance and thereby at maximizing the 
        distance from the singular, unidentifiable case.
        '''
        self._check_for_FIM()
        print 'MAXIMIZE E criterium for OED'
        w, v = np.linalg.eig(self.FIM)
        return min(w)
    
    def modE_criterium(self):
        '''OED design modE criterium
        With this criterion, the focus is on the minimization of the condition 
        number, which is the ratio between the largest and the smallest 
        eigenvalue, or, in other words, the ratio of the shortest and the 
        longest ellipsoid axes. The minimum of this ratio is one, which 
        corresponds to the case where the shape of the confidence ellipsoid 
        is a (hyper)sphere.
        '''
        self._check_for_FIM()
        print 'MINIMIZE modE criterium for OED'
        w, v = np.linalg.eig(self.FIM)
        return max(w)/min(w)

    def get_all_optimality_design_criteria(self):
        '''Return all optimality criteria
        
        '''
        self._check_for_FIM()
        self._all_crit = {'A':self.A_criterium(), 'modA': self.modA_criterium(), 
                          'D': self.D_criterium(), 'E':self.E_criterium(), 'modE':self.modE_criterium()}
        return self._all_crit

    
    
    
    