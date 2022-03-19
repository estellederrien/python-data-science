"""
Usine de jouets

Une entreprise manufacture quatre jouets qui lui apportent des profits de 8,12,14 et 16 euros respectivement. 
Pour se faire, elle utilise 3 matières premières Plastique,Bois et Acier dont elle dispose en stock 42,17,24 kgs. 
Les ressources consommées pour fabriquer une unité de chacun de ces produits sont données dans le tableau ci-dessous. 
L’entreprise souhaite maximiser son profit.

Notons xi la quantité cherchée du produit i.

                automobile    cycle1      cycle2        dragon     nounours    poupee      arc                                stock  
Plastique           2           4           5           7           1           4           2                                  142

Bois                1           1           2           2           1           5           1                                  117

Acier               1           2           3           3           2           2           5                                  124

bénéfice            8           12          14          16          9           13          12



"""

# Import the PuLP lib
from pulp import *

# Créer le type de problème
prob = LpProblem ("MaximiserProfit", LpMaximize)

# La liste de nos produits
produits = ["automobile", "cycle1","cycle2","dragon","nounours","poupee","arc"]

# Les bénéfices en EUROS par produits
benefices = {"automobile": 8, "cycle1": 12, "cycle2": 14,"dragon": 3,"nounours":6,"poupee":13,"arc":12}

# Emplois (en kgs)
plastique = {"automobile": 2, "cycle1": 4, "cycle2": 5,"dragon": 3,"nounours":1,"poupee":4,"arc":2}
bois      = {"automobile": 1, "cycle1": 1, "cycle2": 2,"dragon": 2,"nounours":1,"poupee":5,"arc":1}
acier     = {"automobile": 1, "cycle1": 2, "cycle2": 3,"dragon": 3,"nounours":2,"poupee":2,"arc":5}


# Les noms de nos ressources
ressources = {"plastique", "bois", "acier"}

# Les stocks de nos ressources en KG
stocks = {"plastique": 142, "bois ": 117, "acier": 124}

# Problem variables 
x = LpVariable.dicts("produits ", produits , 0)

# Maximiser la quantité de produits et profit.
prob += lpSum([benefices[i] * x[i] for i in produits ]), "MaximiserBenefice"

# On respecte notre production sous contrainte de stocks
prob += lpSum([plastique[i] * x[i] for i in  produits]) <= 142 ,"MaxPlastique"
prob += lpSum([bois[i]      * x[i] for i in  produits]) <= 117 ,"MaxBois"
prob += lpSum([acier[i]     * x[i] for i in  produits]) <= 124 ,"MaxAcier"

# Production minimale par produits pour les clients : 2 unités
for p in produits:
   prob += x[p] >= 2, f"min production units for product {p}"

# On écrit aussi le probleme dans un fichier
prob.writeLP ( "JouetsModel.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables produits qui s'exprime en unité construites
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonctioj objectif est ici :
print ("TotalProfit", value (prob.objective))

""" Status: Optimal
produits__arc = 2.0
produits__automobile = 39.333333
produits__cycle1 = 2.0
produits__cycle2 = 2.0
produits__dragon = 2.0
produits__nounours = 27.333333
produits__poupee = 2.0
TotalProfit 586.6666620000001 """




# ne fonctionne pas ( A revoir , ce serait bien car plus rapide)
emplois  = {
            0:    [2.0, 4.0, 5.0, 7.0 , 1.0, 4.0, 2.0],
            1:    [1.0, 1.0, 2.0, 2.0 , 1.0, 5.0, 1.0],
            2:    [1.0, 2.0, 3.0, 3.0 , 2.0, 2.0, 5.0]
            }