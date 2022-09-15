""" 
Lien : 
https://stackoverflow.com/questions/19664865/migrating-from-pulp-to-scipy



Avant on utilisait ça, mais on en a marre ! : 
from pulp import *

Problem description 
 """
'''
Minimize        1.800A + 0.433B + 0.180C
Constraint      1A + 1B + 1C = 100
Constraint      0.480A + 0.080B + 0.020C >= 24
Constraint      0.744A + 0.800B + 0.142C >= 76
Constraint                            1C <= 2
'''

...

# Mais on ne veut plus utiliser PULP pour optimiser mais SCIPY !
import numpy as np
import scipy.optimize as opt

#Some variables
cost = np.array([1.800, 0.433, 0.180])
p = np.array([0.480, 0.080, 0.020])
e = np.array([0.744, 0.800, 0.142])

#Our function
fun = lambda x: np.sum(x*cost)

#Our conditions
cond = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 100},
        {'type': 'ineq', 'fun': lambda x: np.sum(p*x) - 24},
        {'type': 'ineq', 'fun': lambda x: np.sum(e*x) - 76},
        {'type': 'ineq', 'fun': lambda x: -1*x[2] + 2})


bnds = ((0,100),(0,100),(0,100))
guess = [20,30,50]
print(opt.minimize(fun, guess, method='SLSQP', bounds=bnds, constraints = cond))