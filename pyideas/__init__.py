# -*- coding: utf-8 -*-
"""
@author: Timothy Van Daele & Stijn Van Hoey

E-mail: timothy.vandaele@gmail.com
"""


from pyideas.version import version as __version__

from measurements import Measurements
from parameterdistribution import *

from model import BaseModel, Model, AlgebraicModel
from solver import HybridSolver, OdeSolver, AlgebraicSolver
from sensitivity import NumericalLocalSensitivity, DirectLocalSensitivity
from confidence import TheoreticalConfidence, CalibratedConfidence
from optimisation import ParameterOptimisation, MultiParameterOptimisation
from uncertainty import Uncertainty
from oed import BaseOED, RobustOED

from pyideas import __path__ as pyideas_path
BASE_DIR = pyideas_path[0]

if __name__ == '__main__':
    print("pyIDEAS ODE/OED package: python package for model development "
          "with Ordinary Differential Equations and Optimal Experimental "
          "Design")
