""" 
Disons que vous voulez maximiser les profits en vendant des soldats de bois (notés x1) 
et des trains de bois (notés x2) étant donné que la marge est de 3 $ pour un soldat et de 2 $ pour un train, 
vous voulez maximiser les bénéfices. 

De plus, vous avez les contraintes suivantes par semaine:

* un soldat a besoin de 2 heures de travail de finition. 
* un train nécessite 1 heure de travail de finition. 
* Vous avez seulement 100 heures de travail de finition disponibles par semaine
* un soldat a besoin d'une heure de travail de charpenterie. 
* Pareil pour un train. 
* Vous avez seulement 80 heures de travail de menuiserie disponibles par semaine
* La demande de soldats n'est de pas plus de 40 par semaine

Les contraintes peuvent être transformées en équations:

  2*x1 + x2 <= 100
  x1 + x2 <= 80
  x1 <=40
et bien sûr, x1> = 0 et x2 = 0 sinon il n'y a rien à optimiser.

Source :
https://thomas-cokelaer.info/blog/2012/11/solving-a-linear-programming-problem-with-python-pulp/

"""

import pulp
from pulp import *
 
# On déclare les variables , x1 c'est le soldat, x2, c'est le train.
x1 = LpVariable("x1", 0, 40)   # 0<= x1 <= 40  car la demande de soldat est inférieure à 40 par semaine .
x2 = LpVariable("x2", 0, 1000) # 0<= x2 <= 1000 La demande est inférieure à 1000
 
# ON dit que c'est un problème de maximisation , car on veut maximiser nos profits.
prob = LpProblem("problem", LpMaximize)


# On définit la fonction économique à maximiser : 3$ * par le nb de soldats de bois produits, et 2$ * par le nb de trains produits .
prob += 3*x1+2*x2
 
# Ensuite, On définit les contraintes.

# 2h de travail pour le train + 1 h pour le soldat doitêtre inférieur à 100 heures de travail par semaine.
prob += 2*x1+x2 <= 100 

# 1 heure de menuiserie + 1 h de menuiserie de soldat doit être inférieur à 80 heures de travail par semaine.
prob += x1+x2 <= 80
 
# solve the problem
prob.solve()
 
# On imprime les résultats x1 = 20, x2 = 60

print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

""" il faut construire 20 soldats de bois et 60 trains de bois par semaine pour gagner le plus d'argent possible !
Status: Optimal
x1 = 20.0
x2 = 60.0 
"""