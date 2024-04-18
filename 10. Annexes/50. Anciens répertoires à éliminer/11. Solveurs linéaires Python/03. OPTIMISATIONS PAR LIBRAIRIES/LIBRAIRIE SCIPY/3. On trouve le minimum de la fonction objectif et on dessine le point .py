# Source : https://www2.hawaii.edu/~jonghyun/classes/S18/CEE696/files/04_scipy_optimize.pdf
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html

""" 

On trouve le minimum de la fonction objectif f(x)= x^2 - 2x , sans contraintes
puis ,  on dessine ce minimum avec matplotlib 

min(x) x^2 - 2x

info scipy : 
scipy.optimize.minimize (fun, x0, args = (), method = None, jac = None, hess = None, hessp = None, bounds = None, contraintes = (), tol = None, callback = None, options = Aucun) [source] ¶

Minimisation de la fonction scalaire d'une ou plusieurs variables.

"""

# Charger les libs
import numpy as np
import scipy.optimize as opt

# on lui indique la fonction objectif avec np.poly1d: 
# 1 x ^2 - 2 x

objective = np.poly1d([1.0,-2.0,0.0])

# Ca l'écrit dans un format compréhensible :
print(objective)

# Estimation initiale. Tableau d’éléments réels de taille (n,), où «n» est le nombre de variables indépendantes. (??)
x0 = 3.0

# On minimize afin de trouver la solution à l'objectif:
results = opt.minimize(objective,x0)

# On imprime la solution:
print("Solution: x=%f"%results.x)

# On dessine le minimum trouvé avec un point rouge :
import matplotlib.pylab as plt
x=np.linspace(-3,5,100)
plt.plot(x,objective(x))
plt.plot(results.x,objective(results.x),'ro')
plt.show()