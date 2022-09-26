"""
Usine de meubles 
Origine du problème : Université de Rennes 1 et INRIA Rennes Bretagne-Atlantique

Une entreprise manufacture quatre produits qui lui apportent des profits de 7,9,18 et 17 euros respectivement. 
Pour se faire, elle utilise les trois ressources A,B,C dont elle dispose en stock 42,17,24 unités. 
Les ressources consommées pour fabriquer une unité de chacun de ces produits sont données dans le tableau ci-dessous. 
L’entreprise souhaite maximiser son profit.

Notons xi la quantité cherchée du produiti.

                produit 1   produit 2   produit 3   produit 4      stock  
ressource A         2           4           5           7           42

ressource B         1           1           2           2           17

ressource C         1           2           3           3           24

bénéfice            7           9           18          17

Voici le PL :
Maximiser
z=7x1+9x2+18x3+17x4
s. c.
2x1+4x2+5x3+7x4≤42
x1+x2+2x3+2x4≤17
x1+2x2+3x3+3x4≤24
x1,x2,x3,x4≥0


NOTE : Le Pl est pas trop bien mis au format dictionnaire - liste, il faut arranger(factoriser) 
cela afin que si les datas proviennent d'une base de données, tout se fasse automatiquement ( du n et pas de valeurs fixe).
Le résultat est ok et conforme au polycopié de l'université de Rennes .

"""



# Import the PuLP lib
from pulp import *

# Create the problem variable
prob = LpProblem ("MaximiserProfit", LpMaximize)

# Problem Data

#une liste: La liste de nos prduits
produits = ["produit_1", "produit_2","produit_3","produit_4"]

#un dictionnaire : Les bénéfices en EUROS par produits
benefices = {"produit_1": 7, "produit_2": 9, "produit_3": 18,"produit_4": 17}

# Les ressources dépensées par produits
ressource_a =  {"produit_1": 2.0, "produit_2": 4.0, "produit_3": 5.0,"produit_4": 7.0}
ressource_b = {"produit_1": 1.0, "produit_2": 1.0, "produit_3": 2.0,"produit_4": 2.0}
ressource_c = {"produit_1": 1.0, "produit_2": 2.0, "produit_3": 3.0,"produit_4": 3.0}

# Les noms de nos ressources
ressources = {"ressource_a", "ressource_b", "ressource_c"}

# Les stocks de nos ressources
stocks = {"ressource_a": 42, "ressource_b": 17, "ressource_c": 24}


# Problem variables 
x = LpVariable.dicts("produits ", produits , 0)

# Maximiser la quantité de produits et profit.
prob += lpSum([benefices[i] * x[i] for i in produits ]), "MaximiserBenefice"

# On respecte notre production sous contrainte de stocks

prob += lpSum([ressource_a[i] * x[i] for i in produits]) <= stocks["ressource_a"], "ct1"

prob += lpSum([ressource_b[i] * x[i] for i in produits]) <= stocks["ressource_b"], "ct2"

prob += lpSum([ressource_c[i] * x[i] for i in produits]) <= stocks["ressource_c"], "ct3"


# On écrit aussi le problem dans un fichier
prob.writeLP ( "MeublesModel.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables produits qui s'exprime en unité construites
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonctioj objectif est ici :
print ("TotalProfit", value (prob.objective))

# Status: Optimal
# produits__produit_1 = 3.0
# produits__produit_2 = 0.0
# produits__produit_3 = 7.0
# produits__produit_4 = 0.0
# TotalProfit 147.0