import sympy as sp
import numpy as np
from sympy import Matrix

A=Matrix([[2,3,4],
            [6,9,10],
            [9,12,17]])

echeleon=A.echelon_form()

print(echeleon)

help(Matrix)