""" 
Afficher toutes les valeurs intermédiaires d'une optimisation


Source : https://stackoverflow.com/questions/16739065/how-to-display-progress-of-scipy-optimize-function


Comme mg007 l'a suggéré, certaines des routines scipy.optimize permettent une fonction de rappel 
(malheureusement, lessq ne le permet pas pour le moment). 
Voici un exemple utilisant la routine "fmin_bfgs" où 
j'utilise une fonction de rappel pour afficher la valeur actuelle des arguments et
 la valeur de la fonction objectif à chaque itération.

 
 """



import numpy as np
from scipy.optimize import fmin_bfgs

Nfeval = 1

def rosen(X): #Rosenbrock function
    return (1.0 - X[0])**2 + 100.0 * (X[1] - X[0]**2)**2 + \
           (1.0 - X[1])**2 + 100.0 * (X[2] - X[1]**2)**2

def callbackF(Xi):
    global Nfeval
    print '{0:4d}   {1: 3.6f}   {2: 3.6f}   {3: 3.6f}   {4: 3.6f}'.format(Nfeval, Xi[0], Xi[1], Xi[2], rosen(Xi))
    Nfeval += 1

print  '{0:4s}   {1:9s}   {2:9s}   {3:9s}   {4:9s}'.format('Iter', ' X1', ' X2', ' X3', 'f(X)')   
x0 = np.array([1.1, 1.1, 1.1], dtype=np.double)
[xopt, fopt, gopt, Bopt, func_calls, grad_calls, warnflg] = \
    fmin_bfgs(rosen, 
              x0, 
              callback=callbackF, 
              maxiter=2000, 
              full_output=True, 
              retall=False)


""" The output looks like this:

Iter    X1          X2          X3         f(X)      
   1    1.031582    1.062553    1.130971    0.005550
   2    1.031100    1.063194    1.130732    0.004973
   3    1.027805    1.055917    1.114717    0.003927
   4    1.020343    1.040319    1.081299    0.002193
   5    1.005098    1.009236    1.016252    0.000739
   6    1.004867    1.009274    1.017836    0.000197
   7    1.001201    1.002372    1.004708    0.000007
   8    1.000124    1.000249    1.000483    0.000000
   9    0.999999    0.999999    0.999998    0.000000
  10    0.999997    0.999995    0.999989    0.000000
  11    0.999997    0.999995    0.999989    0.000000
Optimization terminated successfully.
         Current function value: 0.000000
         Iterations: 11
         Function evaluations: 85
         Gradient evaluations: 17

At least this way you can watch as the optimizer tracks the minimum """