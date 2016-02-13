# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:33:14 2013

@author: Timothy Van Daele; Stijn Van Hoey

0.1 Class version of the ODE generator linkfile for optimization
"""

from __future__ import division
import warnings
import sys
import os
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if sys.hexversion > 0x02070000:
    import collections
else:
    import ordereddict as collections


class ode_measurements(object):
    '''class to include measured data in the framework


    Input possibilities (cfr. FME package R):

        1. Dictionary: {'variables':[var of measurement], 'time': [timeindex of measurement], 'values':[measurements]}
        2. DataFrame of the above Dictionary
        3. Dictionary: {'time': [time indices], 'var1': [meas for the timesteps of var1], 'var2':[meas for the timesteps of var2]}
        4. DataFrame of the above

    ATTENTION: The 'variables' and 'values' is required to let it work!

    '''

    def __init__(self, measdata, xdata = 'time', *args, **kwargs):
        '''
        '''
        if kwargs.get('print_on') == None:
            self._print_on = True
        else:
            self._print_on = kwargs.get('print_on')

        if isinstance(measdata, dict):
            #Different variables names in key-names
            if 'variables' in measdata:
                if not 'values' in measdata:
                    raise Exception('Values and variables needed as key-value')
                if not xdata in measdata:
                    raise Exception('Information about the xdata for the measurements is lacking!')
                self.Data = pd.DataFrame(measdata).pivot(index = xdata, columns='variables', values='values')

            else: #all variables in key names, so same length in all arrays
                lencheck = np.array([len(value) for value in measdata.items()])
                if not lencheck.min() == lencheck.max():
                    raise Exception('Dictionary data input requires equal lengths in this format')

                if xdata in measdata:
                    #convert Dictionary to pandas DataFrame
                    indext=measdata[xdata]
                    measdata = {key: value for key, value in measdata.items() if key != 'time'}
                    self.Data = pd.DataFrame(measdata, index=indext)
                else:
                    self.Data = pd.DataFrame(measdata)
                    if self._print_on:
                        print('Attention: Information for xdata is not explicitly set!')

        if isinstance(measdata, pd.DataFrame):
#            if isinstance(measdata.keys(), pd.MultiIndex):
#                measdata.columns.names = ['Experiment', 'Variable']

            #check if time is a column name
            if xdata in measdata.columns:
                measdata[xdata] = measdata[xdata].astype(np.float64)
                if 'variables' in measdata:
                    self.Data = measdata.pivot(index=xdata, columns='variables', values='values')
                else:
                    self.Data = measdata.set_index(xdata)
            else:
                measdata.index.name = xdata
                measdata = measdata.reset_index()
                measdata[xdata] = measdata[xdata].astype(np.float64)
                measdata = measdata.set_index(xdata)
                self.Data = measdata
                if self._print_on:
                    print('index of dataframe is seen as measurement xdata, and colnames are the measured variables')

        elif isinstance(measdata, pd.Series):
            self.Data = pd.DataFrame(measdata)
            self.Data.index.name = xdata
            self.Data = self.Data.reset_index()
            self.Data[xdata] = self.Data[xdata].astype(np.float64)
            self.Data = self.Data.set_index(xdata)

        else:
            raise Exception('Measured Data must be added as pandas DataFrame or dictionary of np arrays')

        #We provide for internal purposes also second data-type: dict with {'cvar1':Timeserie,'var': Timeserie}
        self._data2dictsystem()
        self.get_measured_outputs()

        #Create Error Covariance Matrix with unity matrixes
        unity_dict ={}
        for var in self.get_measured_outputs():
            unity_dict[var]=1
        if self._print_on:
            print(unity_dict)
        self.add_measured_errors(unity_dict, method = 'absolute')

        self._independent = self._index_to_dict(self.Data.index)

    def _data2dictsystem(self):
        '''
        Help function to merge the different date-profiles
        '''
        self.Data_dict={}
        for var in self.Data.columns:
            self.Data_dict[var] = pd.DataFrame(self.Data[var].dropna())

    def _index_to_dict(self, index):
        """
        """
        independent_dict = {}
        for name in index.names:
            independent_dict[name] = np.array(index.get_level_values(name))
        return independent_dict

    def add_measured_variable(self, newdata):
        '''add an extra measurement

        Parameters
        ------------
        newdata :  pd.DataFrame or dict
            Variable and the corresponding timesteps measured

        Notes
        -----
        Example dict: {'time':[0.5,2.,8.],'DO2':[5.,9.,2.]}

        '''
        if isinstance(newdata, dict):
            newdata = pd.DataFrame(newdata).set_index(self.xdata)
            self.Data = pd.concat([self.Data, newdata], axis=1).sort()
        elif isinstance(newdata, pd.DataFrame):
            self.Data = pd.concat([self.Data, newdata], axis=1).sort()

        #update the datadictionary
        self._data2dictsystem()
        self.get_measured_outputs()


    def get_measured_xdata(self):
        '''
        Based on the measurements timesteps, an array is made with the
        timesteps to get modelled output from (over all variables)

        '''
        self._measured_xdata = np.array(self.Data.index).astype('float')
        return self._measured_xdata

    def get_measured_outputs(self):
        '''
        Based on the measurements, get the variable names measured
        '''
        self._measured_outputs = self.Data.columns.tolist()
        return self._measured_outputs


    def add_measured_errors(self, meas_error_dict, method = 'relative',
                            lower_accuracy_bound = None,
                            minimal_relative_error = None):
        r'''calculates standard deviation of measurements

        Measurement errors on the measured data; options are relative and
        absolute.

        The second component of the FIM is the measurement error in the form
        of the inverse measurement error covariance matrix Q−1

        It should also be mentioned that correlations between measurements
        can also be specified using this covariance matrix. Throughout this
        package it will be assumed that the error characteristics of the
        measurements can be described in a relatively simple way:
            by asolute or relative errors or by Ternbach
        description.

        Typically, Q is chosen as the inverse of the measurement error
        covariance matrix(Marsili–Libelli et al., 2003; Omlin and Reichert,
        1999; Vanrolleghem and Dochain, 1998)

        Error values are also added to the data_dict version.

        Parameters
        -----------
        meas_error_dict : dict
            dictionary with the variable names and their corresponding errors
            (relative or absolute)
        method : relative|absolute
            relative is percentage value of the variable itself; absolute
            is a constant measurement value

        Notes
        -----
        For the Ternbach method,  the standard deviations of the measurements
        were calculated by:

        .. math:: \sigma_y = \hat{y} \cdot \varsigma_y \cdot \left(1+\frac{1}{(\frac{\hat{y}}{lb_y})^2 + \frac{\hat{y}}{lb_y}} \right)

        Here, :math:`\varsigma_y` and :math:`lb_y` respectively represent a
        constant minimal relative error and a lower accuracy bound on the
        measurement of y. In this way, the standard deviations of the
        meaurements are proportional to the value of the measurements
        :math:`\hat{y}`.
        '''
        #print 'Error Covariance Matrix is updated'

        for var in meas_error_dict:
            if not var in self.get_measured_outputs():
                raise Exception('Variable ', var, ' not listed in current measurements.')

        self.Meas_Errors = collections.OrderedDict(sorted(meas_error_dict.items(), key=lambda t: t[0]))
        self.Meas_Errors_type = method

        #update measurement error covariance matrix eenheidsmatrix
        #self._Error_Covariance_Matrix = np.identity(len(self._MeasuredList))
        #OLD VERSION; only for equal measurement size:
        #self._Error_Covariance_Matrix = np.zeros((len(self.get_measured_variables()),
        #len(self.get_measured_variables()), len(self.get_measured_xdata())))

        #The number of available measurements is time-dependent, so the FIM
        #and WSSE calculation need adaptation. In order to preserve flexibility
        #We'll put each timestep in a separate item in a dictionary
        self._Error_Covariance_Matrix = {}
        self._Error_Covariance_Matrix_PD = self.Data.copy()

        if method == 'absolute':
            for var in self.Meas_Errors:
                measerr = self.Meas_Errors[var]
                self.Data_dict[var]['error'] = measerr**2.

            for xstep in self.get_measured_xdata():
                temp = np.zeros((len(self.Data.loc[xstep].dropna()), len(self.Data.loc[xstep].dropna())))
                self._Error_Covariance_Matrix[xstep] = pd.DataFrame(temp, index=self.Data.loc[xstep].dropna().index.tolist(), columns=self.Data.loc[xstep].dropna().index.tolist())
                for ide, var in enumerate(self.Data.loc[xstep].dropna().index):
                    measerr = self.Meas_Errors[var]
                    self._Error_Covariance_Matrix[xstep].values[ide,ide] = measerr**2.  #De 1/sigma^2 komt bij inv berekening van FIM
            #Error covariance matrix PD
            for var in self.Data.columns:
                measerr = self.Meas_Errors[var]
                self._Error_Covariance_Matrix_PD[var] = measerr**2.  #De 1/sigma^2 komt bij inv berekening van FIM

        elif method == 'relative':
            for var in self.Meas_Errors:
                measerr = self.Meas_Errors[var]
                self.Data_dict[var]['error'] = np.array((measerr*self.Data_dict[var][var])**2.).flatten()

            for xstep in self.get_measured_xdata():
                temp = np.zeros((len(self.Data.loc[xstep].dropna()), len(self.Data.loc[xstep].dropna())))
                self._Error_Covariance_Matrix[xstep] = pd.DataFrame(temp, index=self.Data.loc[xstep].dropna().index.tolist(), columns=self.Data.loc[xstep].dropna().index.tolist())
                for ide, var in enumerate(self.Data.loc[xstep].dropna().index):
                    measerr = self.Meas_Errors[var]
                    self._Error_Covariance_Matrix[xstep].values[ide,ide] = np.array((measerr*self.Data_dict[var].loc[xstep][var])**2.)#.flatten()
            #Error covariance matrix PD
            for var in self.Data.columns:
                measerr = self.Meas_Errors[var]
                self._Error_Covariance_Matrix_PD[var] = (measerr*self.Data[var])**2.


        elif method == 'Ternbach': #NEEDS CHECKUP!!
            for var in self.Meas_Errors:
                yti = self.Data_dict[var][var]
                measerr = self.Meas_Errors[var]
                temp=1.+ 1./((yti/lower_accuracy_bound)**2 +(yti/lower_accuracy_bound))
                self.Data_dict[var]['error'] = yti*minimal_relative_error*temp

            for xstep in self.get_measured_xdata():
                temp = np.zeros((len(self.Data.loc[xstep].dropna()), len(self.Data.loc[xstep].dropna())))
                self._Error_Covariance_Matrix[xstep] = pd.DataFrame(temp, index=self.Data.loc[xstep].dropna().index.tolist(), columns=self.Data.loc[xstep].dropna().index.tolist())
                for ide, var in enumerate(self.Data.loc[xstep].dropna().index):
                    yti = self.Data_dict[var].loc[xstep][var]
                    measerr = self.Meas_Errors[var]
                    temp=1.+ 1./((yti/lower_accuracy_bound)**2 +(yti/lower_accuracy_bound))
                    self._Error_Covariance_Matrix[xstep].values[ide,ide] = yti*minimal_relative_error*temp
            #Error covariance matrix PD
            for var in self.Data.columns:
                measerr = self.Meas_Errors[var]
                temp=1.+ 1./((self.Data[var]/lower_accuracy_bound)**2 +(self.Data[var]/lower_accuracy_bound))
                self._Error_Covariance_Matrix_PD[var] = self.Data[var]*minimal_relative_error*temp

        elif method == 'direct':
            for var in self.Meas_Errors:
                measerr = self.Meas_Errors[var]
                self.Data_dict[var]['error'] = measerr

            for jde, xstep in enumerate(self.get_measured_xdata()):
                temp = np.zeros((len(self.Data.loc[xstep].dropna()), len(self.Data.loc[xstep].dropna())))
                self._Error_Covariance_Matrix[xstep] = pd.DataFrame(temp, index=self.Data.loc[xstep].dropna().index.tolist(), columns=self.Data.loc[xstep].dropna().index.tolist())
                for ide, var in enumerate(self.Data.loc[xstep].dropna().index):
                    measerr = self.Meas_Errors[var]
                    self._Error_Covariance_Matrix[xstep].values[ide,ide] = measerr[jde]

            #Error covariance matrix PD
            for var in self.Data.columns:
                measerr = self.Meas_Errors[var]
                self._Error_Covariance_Matrix_PD[var] = measerr

	# All values which should be nan are set to 1e50 (this is done by checking this with the data)
        # because in that way they are ignored. This is of importance when data is missing for one var
        # but not for the other one. Otherwise the FIM would be altered.
	self._Error_Covariance_Matrix_PD = self._Error_Covariance_Matrix_PD*self.Data.applymap(lambda x: np.nan if math.isnan(x) else 1)
	self._Error_Covariance_Matrix_PD = self._Error_Covariance_Matrix_PD.applymap(lambda x: 1e50 if math.isnan(x) else x)

    def set_error_datapoint(self, time, output, error):
        r'''
        A function to set the absolute error of a certain output at a certain
        time. Especially handy if you want to set the error of some points
        specifically.

        Parameters
        -----------
        time : int or float
            time at which the error of the output should be set
        output : string
            output of interest
        error : float
            absolute error for that specific time/variable

        '''
        # Error should be set in ECM dict and ECM pd, however we
        # ignore any covariance between the different outputs.
        self._Error_Covariance_Matrix_PD[output].loc[time] = error
        self._Error_Covariance_Matrix[time][output][output] = error

        #Create Multi-Index -> not working
#        arrays = [['Model']*len(self._data.get_measured_variables())+['Meas']*len(self._data.get_measured_variables()),self._data.get_measured_variables()*2]
#        tuples = zip(*arrays)
#        index = pd.MultiIndex.from_tuples(tuples, names=['Type', 'Variables'])
