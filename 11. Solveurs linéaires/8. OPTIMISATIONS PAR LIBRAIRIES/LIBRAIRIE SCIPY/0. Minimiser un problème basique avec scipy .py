""" 
Minimiser                   w = 10*y1 + 15*y2 + 25*y3

Sous les contraintes:       y1 + y2 + y3 >= 1000
                            y1 - 2*y2    >= 0
                            y3 >= 340

avec                        y1 >= 0, y2 >= 0

Source fiable : https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method


Autre source : https://stackoverflow.com/questions/61036775/solve-linear-programming-problem-of-otimization-with-scipy

Le linprog dans scipy est parfois incohérent parce que:

    Cela résout toujours un problème de minimisation, donc si vous voulez maximiser une fonction objectif, vous devez faire une solution de contournement comme dans cette solution pour la transformer en un problème de minimisation

    les équations qui ont> = doivent être multipliées par -1 pour devenir <=

    En créant ensemble des contraintes telles que A_ub A_eq ensemble, ce sont des matrices séparées, donc créez-les ensuite individuellement

Jetez un œil dans la documentation, ils ont également un bel exemple

https://stackoverflow.com/questions/42303470/scipy-optimize-inequality-constraint-which-side-of-the-inequality-is-considere

optimize.linprog always minimizes your target function. 
If you want to maximize instead, 
you can use that max(f(x)) == -min(-f(x))

"""



import numpy as np
from scipy.optimize import linprog

# On prends le programme linéaire et on le transforme en matrice , 
# et vu que linprog a besoin de contraintes du type f(x) <= const et que nos conraintes sont >=, 
# on doit tout inverser nos contraintes au format :  -f(x) <= - const : 

A = np.array([[-1, -1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
b = np.array([-1000, 0, -340, 0, 0])

# Ici , on reconnait bien la fonction objectif à minimiser : 
c = np.array([10,15,25])

# On récupère le résultat de l'exécution du simplexe :
res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)

# On voit que le résultat et y1 = 660 y2 = 0 et y3 = 340 pour une valeur globale de 15100
# ('Optimal value:', 15100.0, '\nX:', array([ 660.,    0.,  340.]))
# python3
# Optimal value: 15099.999961403426 
# X: [6.59999996e+02 1.00009440e-07 3.40000000e+02]