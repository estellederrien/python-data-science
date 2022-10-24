""" 
 PLANIFICATION DE PRODUCTION MULTI PERIODE AVEC PRISE EN COMPTE DES STOCKS
 MINIMISATION DES COUTS 2022 

COMPARAISON ENTRE LE SOLVEUR EXCEL ET PYTHON PULP 
Répertoire 11 / 03. Production planifiée - Comparaison Excel/Python Pulp : 
Le fichier excel et python ne donnent pas le même résultat objectif - 
mais les mêmes ordonnances de planification de production par mois. 
La raison est que le calcul de la fonction objectif utilise une valeur de stock moyen ' average ' 
dans Excel, mais le script Python ( Qui est exact) , lui, ne calcule pas le résultat de l'objectif 
( Minimiser le cout ) en utilisant cette valeur de stock moyen (average inventory), qui est optionnelle.

"""


# Importer PULP
from pulp import *

# 1. On veut minimiser Les coûts de production, et d'inventaire.
model = LpProblem("Minimiser le cout",LpMinimize)

# ON définit les couts de production et de stockage pour les 6 mois différents ; Dans periodes, c'est le nombre de mois SOIT 6. Define production cost, inventory cost, and demande.
# Définir les couts de production par période, le cout de l'inventaire, et la demandee reportée par le service commercial

periodes = list(range(6)) 
demande=[1000,4500,6000,5500,3500,4000]
cout_production=[240,250,265,285,280,260]
cout_stockage=[3.60,3.75,3.98,4.28,4.20,3.90]


# Facultatif : On spécifie les max min de prod et stock par période, ce sont des contraintes en plus 
min_production=[2000,1750,2000,2250,2000,1750]
max_production=[4000,3500,4000,4500,4000,3500]

min_stock = [1500,1500,1500,1500,1500,1500] # Par sécurité on garde 1500 objets min en stock
max_stock = [6000,6000,6000,6000,6000,6000]

# 2. Définir les variables de décision : Production et Stock - Define Decision Variables: Production and Inventory
x = LpVariable.dicts('production_', periodes,lowBound=0, cat='Continuous')
y = LpVariable.dicts('stock_', periodes,lowBound=0, cat='Continuous') # Ces stocks seront calculés par l'algorithme lors de l'optimisation, au début on en a pas vuq u'on ne peut pas prédire les ventes futures


# 3. Définir l'objectif , On veut minimiser les coûts de production + de stockage comme dans le problème de université taiwan
model += lpSum([cout_production[i]*x[i] for i in periodes]) + lpSum([cout_stockage[i]*y[i] for i in periodes])

# Définir les contraintes

# Voici celles du fichier excel : 
# Ending inventory >= Min Inventory (safety stock) ( En anglais : Inventory = stock)
# Ending inventory >= Max Inventory
# Beggining inventory <= Max production capacity
# Beggining inventory >= Min production capacity


# Par rapport au problème classique, il ajoute la difficulté de prendre en compte 
# le stock présent AVANT les périodes que l'on va optimiser, donc le premier mois !


# Constrainte de stocks min et max
for i in periodes:
    model.addConstraint(y[i]<=max_stock[i])
for i in periodes:
    model.addConstraint(y[i]>=min_stock[i])


# Constrainte de capacité de production (Production-capacity constraints)
for i in periodes:
    model.addConstraint(x[i]<=max_production[i])
for i in periodes:
    model.addConstraint(x[i]>=min_production[i])



# Contrainte de balance de stocks ( Inventory-balance constraints)
model.addConstraint(x[0] - (y[0] - 2750) == demande[0]) # (Mois 1) On pars avec 2750 unités du stock précédent comme dans l'exemple du fichier excel
# model.addConstraint(x[0] - (y[0]) == demande[0])

for i in periodes[1:]:
    model.addConstraint(x[i] - y[i] + y[i-1] == demande[i]) # par mois  2 , 3 , 4 , 5 , 6

#ON résouds avec le solveur pulp ou un autre entre parenthèses
model.solve()

# On imprime les solutions
for v in model.variables():
    print(v.name, "=", v.varValue)
    
""" 

Optimal objective 6206377.5 - 4 iterations time 0.002, Presolve 0.00
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.05   (Wallclock seconds):       0.05

LA , LE SOLVEUR NOUS DIT COMBIEN PRODUIRE PAR MOIS 
TOUT EN TENANT COMPTE DES STOCKS AFIN DE MINIMISER TOUS LES COUTS POUR CES PERIODES !!

production__0 = 4000.0
production__1 = 3500.0
production__2 = 4000.0
production__3 = 4250.0
production__4 = 4000.0
production__5 = 3500.0
stock__0 = 5750.0
stock__1 = 4750.0
stock__2 = 2750.0
stock__3 = 1500.0
stock__4 = 2000.0
stock__5 = 1500.0 """