""" 

Le problème du sac à dos .

Maximiser la valeur des objets que je porte dans mon sac
Sous contrainte de place (aussi appelé "espace"). 

POurquoi est-ce un problème en nombres entiers ? 
Par ce que on ne peut pas séparer un objet en 2, 
on ne peut pas avoir 1,5 objet dans son sac , par exemple .

Et si je ne veux mettre dans mon sac qu'un seul objet de chaque ? 
Alors on doit spécifier que les variables de décision sont binaires !

Caractéristiques de mon problème : 

Objet                       Valeur ( unité de 10 Euros)     Taille( En "unité générique" .)
Caméra                      5                               2
Figurine                    7                               4
Bouteille de cidre énorme   2                               7
Trompette                   10                              10

Maximise 5a + 7b + 2c + 10d (objective: maximiser la valeur globale (Σ somme ) des articles )
Sous les contraintes ( Subject to) :
    2a + 4b + 7c + 10d <= 15 (Contrainte d'espace dans le sac)


Author: 
Shanglun Wang
https://www.toptal.com/algorithms/mixed-integer-programming
https://www.toptal.com/resume/shanglun-sean-wang

"""

import pulp


prob = pulp.LpProblem("Minimize",pulp.LpMaximize)

produits = ["caméra", "figurine","bouteille","trompette"]

valeur = {"caméra": 5, "figurine": 7, "bouteille": 2,"trompette":10}

taille = {"caméra": 12, "figurine": 4, "bouteille": 7,"trompette":10}

# Déclarer les variables de décision : On peut mettre 10 au maximum de chaque produit
#  x = pulp.LpVariable.dicts("produits ", produits , lowBound=0, upBound=10, cat='Integer')

# Par contre, si on ne veut prendre qu'un seul objet de chaque, alors, on doit établir le dictionnaire de cette façon : 
x = pulp.LpVariable.dicts("produits ", produits , lowBound=0, upBound=1, cat='Binary')

# Ajouter la fonction objectif
prob += pulp.lpSum([valeur[i] * x[i] for i in produits ]), "MaximiserValeur"

# Ajouter les contraintes  
prob += pulp.lpSum([(taille[i] * x[i]) for i in produits]) <= 15, "TailleSac"

# On écrit aussi le problem dans un fichier
prob.writeLP ( "opt.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", pulp.LpStatus [prob.status])

# Afficher l'optimium de chaques variables produits qui s'exprime en unité construites
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# IMPRIMER LA SOLUTION OPTIMALE
print("La valeur maximale de mon sac au total , sous contrainte de taille des objets = ",pulp.value(prob.objective))


""" Result - Optimal solution found

Objective value:                17.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.02
Time (Wallclock seconds):       0.02

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.04   (Wallclock seconds):       0.04

Status: Optimal
produits__bouteille = 0.0
produits__caméra = 0.0
produits__figurine = 1.0
produits__trompette = 1.0
La valeur maximale de mon sac au total , sous contrainte de taille des objets =  17.0
Welcome to the CBC MILP Solver
Version: 2.9.0
Build Date: Feb 12 2015"""



# Le même programme écrit autrement par l'auteur : 

import pulp as pl

# declare some variables
# each variable is a binary variable that is either 0 or 1
# 1 means the item will go into the knapsack
a = pl.LpVariable("a", 0, 1, pl.LpInteger)
b = pl.LpVariable("b", 0, 1, pl.LpInteger)
c = pl.LpVariable("c", 0, 1, pl.LpInteger)
d = pl.LpVariable("d", 0, 1, pl.LpInteger)

# define the problem
prob = pl.LpProblem("knapsack", pl.LpMaximize)

# objective function - maximize value of objects in knapsack
prob += 5 * a + 7 * b + 2 * c + 10 * d

# constraint - weight of objects cannot exceed 15
prob += 2 * a + 4 * b + 7 * c + 10 * d <= 15

status = prob.solve()  # solve using the default solver, which is cbc
print(pl.LpStatus[status])  # print the human-readable status

# print the values
print("a", pl.value(a))
print("b", pl.value(b))
print("c", pl.value(c))
print("d", pl.value(d))

Result - Optimal solution found

""" Objective value:                17.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.02
Time (Wallclock seconds):       0.03

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.04   (Wallclock seconds):       0.04

Optimal
a 0.0
b 1.0 Mysterious figurine
c 0.0
d 1.0 French horn """