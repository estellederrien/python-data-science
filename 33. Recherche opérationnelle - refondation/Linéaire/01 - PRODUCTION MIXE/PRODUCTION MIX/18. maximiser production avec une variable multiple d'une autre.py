""" J'ai une usine de fabrication de jouets en bois.

Je dois construire des camions de pompier, des hélicoptères et des ambulances en bois.



2 employés, qui travaillent 1 h , 2H, 3H pour respectifs objets pour un maximum de 100H/semaine.

******Pour un camion de pompier produit, je dois produire 2 ambulances. *****


 """


import pulp
from pulp import *
 
# On déclare les variables 
x1 = LpVariable("x1", 0, 1000)   
x2 = LpVariable("x2", 0, 1000) 
x3 = LpVariable("x3", 0, 1000) 


# ON dit que c'est un problème de maximisation , car on veut maximiser nos profits.
prob = LpProblem("problem", LpMaximize)


# On définit la fonction économique à maximiser : 3$ * par le nb de soldats de bois produits, et 2$ * par le nb de trains produits .
prob += 3*x1 + 2*x2 + 4*x3 
 
# Ensuite, On définit les contraintes.

# Heures de travail max
prob += 1*x1 + 2*x2 + 3*x3 <= 100 

# On oblige Pulp que pour 1 camion produit (x1) il doit produire 2 hélicos (x2)
# Autrement dit,on produit toujours 2 * plus de camion que d'hélicos
# Dans le résulat, on voit que forcer un multiple fonctionne
prob += x1 * 2 == x2 

 
# solve the problem
prob.solve()
 
# On imprime les résultats 

print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

"""After Postsolve, objective 200, infeasibilities - dual 0 (0), primal 0 (0)
Optimal objective 200 - 1 iterations time 0.012, Presolve 0.00
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.05   (Wallclock seconds):       0.05

Status: Optimal
x1 = 20.0
x2 = 40.0
x3 = 0.0
"""