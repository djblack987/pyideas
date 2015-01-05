# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 16:30:34 2015

@author: joris
"""
from __future__ import division

import unittest

import numpy as np

from biointense.model import Model


class TestAlgebraicModel(unittest.TestCase):

    # def setup_method(self):
    #
    #     system = {'algebraic': {'W': 'W0*Wf/(W0+(Wf-W0)*exp(-mu*t))'}}
    #     parameters = {'W0': 2.0805,
    #                   'Wf': 9.7523,
    #                   'mu': 0.0659}
    #
    #     model = Model('Modsim1', system, parameters)
    #
    #     model.independent_values = np.linspace(0, 72, 1000)
    #     #model.variables = {'algebraic': ['W']}
    #
    #     self.model = model

    def test_model_instantiate(self):

        system = {'W': 'W0*Wf/(W0+(Wf-W0)*exp(-mu*t))'}
        parameters = {'W0': 2.0805,
                      'Wf': 9.7523,
                      'mu': 0.0659}

        model = Model('Modsim1', system, parameters)

        model.independent_values = np.linspace(0, 72, 1000)

        expected = {'W': 'W0*Wf/(W0+(Wf-W0)*exp(-mu*t))'}
        result = model.systemfunctions['algebraic']
        assert result == expected

        assert model.variables['algebraic'] == ['W']

    # def test_model_run(self):
    #
    #     result = self.model.run()
    #     assert result['W'].values[-1] == 9.4492688322077534


class TestOdeModel(unittest.TestCase):

    def test_model_instantiate(self):

        ODE = {'dS': 'Q_in/V*(S_in-S)-1/Ys*mu_max*S/(S+K_S)*X',
               'dX': '-Q_in/V*X+mu_max*S/(S+K_S)*X'}

        parameters = {'mu_max': 0.4, 'K_S': 0.015, 'Q_in': 2, 'Ys': 0.67,
                      'S_in': 0.02, 'V': 20}

        model = Model('Fermentor', ODE, parameters)

        # system parsing
        result = model.systemfunctions['ode']
        assert result == {'S': ODE['dS'], 'X': ODE['dX']}

        assert model.variables['ode'] == ['S', 'X']