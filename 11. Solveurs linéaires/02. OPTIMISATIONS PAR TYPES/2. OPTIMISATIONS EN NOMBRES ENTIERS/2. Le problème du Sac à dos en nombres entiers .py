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


Auteur: 
Shanglun Wang
https://www.toptal.com/algorithms/mixed-integer-programming
https://www.toptal.com/resume/shanglun-sean-wang

Liens : 
http://web.mit.edu/15.053/www/AMP-Chapter-09.pdf

"""

import pulp


prob = pulp.LpProblem("Minimize",pulp.LpMaximize)

produits = ["caméra", "figurine","bouteille","trompette"]

valeur = {"caméra": 5, "figurine": 7, "bouteille": 2,"trompette":10}

taille = {"caméra": 12, "figurine": 4, "bouteille": 7,"trompette":10}

# Déclarer les variables de décision : On peut mettre 10 au maximum de chaque produit
x = pulp.LpVariable.dicts("produits ", produits , lowBound=0, upBound=10, cat='Integer')

# Par contre, si on ne veut prendre qu'un seul objet de chaque, alors, on doit établir le dictionnaire de cette façon : 
# x = pulp.LpVariable.dicts("produits ", produits , lowBound=0, upBound=1, cat='Binary')

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


""" 
Result - Optimal solution found

Objective value:                21.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.04
Time (Wallclock seconds):       0.04

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.05   (Wallclock seconds):       0.05

Status: Optimal
produits__bouteille = 0.0
produits__caméra = 0.0
produits__figurine = 3.0
produits__trompette = 0.0
La valeur maximale de mon sac au total , sous contrainte de taille des objets =  21.0
 """