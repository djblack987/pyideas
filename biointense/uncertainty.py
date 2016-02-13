# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 16:59:56 2015

@author: timothy
"""
import sympy


class Uncertainty(object):
    """
    The aim of the uncertainty class is to ease the way to pass uncertainties,
    without reducing the flexibility.

    Parameters
    -----------
    uncertainty_dict: dict
        For each of the (measurable) modeloutputs, the uncertainty of has to be
        defined. The standard assumption is that the uncertainty/error is
        obeying a normal distribution, so two basic options can be used:

        * **Absolute error**
        This means that the error is the same for all values
        no matter the conditions or time of measurement. For example, if you
        have a normal distribution with an absolute deviation of 0.05, than you
        pass '0.05**2' as uncertainty.

        * **Relative error**
        The error is depending on the output value, this means
        that small values will have a smaller absolute error compared to large
        output values. For example, if you have an output (y) with a normal
        distributed error with a relative deviation of 5%, than you pass
        '(y*0.05)**2'.

        There are two options to pass your uncertainty: in a symbolic way or as
        a function. In the example below the uncertainty of y1 is passed as a
        function and the uncertainty of y2 is passed symbolically. The symbolic
        strings are automatically converted to function using sympy.

    Examples
    ---------
    >>> def uncertainty_y1(y1):
    >>>     return (0.1*y1)**2
    >>> uncertainty_dict = {'y1': uncertainty_y1,
                            'y2': '(0.09*y2)**2'}
    """

    def __init__(self, uncertainty_dict):
        """
        """
        self.uncertainty_dict = uncertainty_dict

    def get_uncertainty(self, output):
        r"""
        Function to calculate the uncertainty given the generated model output.

        Parameters
        -----------
        output: pandas.DataFrame
            pandas.DataFrame containing the output of the model run

        See also
        ---------
        biointense.ParameterOptimisation, biointense.confidence,
        biointense.BaseOED

        Examples
        ---------
        >>> import numpy as np
        >>> from biointense import AlgebraicModel, Uncertainty
        >>> system = {'y': 'a*x+b'}
        >>> parameters = {'a': 0.1, 'b': 2.}
        >>> M1 = AlgebraicModel('linear model', system, parameters)
        >>> M1.set_independent({'x': np.linspace(-10.,10.,1000)})
        >>> output = M1.run()
        >>> M1uncertainty = Uncertainty({'y': '(0.1*y)**2'})
        >>> output_uncertainty = M1uncertainty.get_uncertainty(output)
        >>> output_uncertainty.plot()
        """
        uncertainty = output.copy()
        for var, value in self.uncertainty_dict.items():
            if isinstance(value, str):
                sympy_uncertainty = sympy.sympify(value)
                fun = sympy.lambdify(var, sympy_uncertainty)
                uncertainty[var] = fun(output[var])
            elif hasattr(value, '__call__'):
                uncertainty[var] = value(output[var])
            else:
                raise Exception('Only strings and functions can be passed!')

        return uncertainty