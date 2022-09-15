""" 
 PLANIFICATION DE PRODUCTION AVEC STOCKS
 MINIMISATION DES COUTS
COMPARAISON DE RESULTAT ENTRE LINDO AMP CHAPITRE 9 ET PYTHON PULP
 """



# Importer PULP
from pulp import *

# 1. On veut minimiser Les coûts de production, et d'inventaire.
model = LpProblem("Minimiser le cout",LpMinimize)

# ON définit les couts de production et de stockage pour les jours 1 2 3 ET 4 ; Dans quaters, c'est le nombre de jours SOIT 4. Define production cost, inventory cost, and demande.
# Définir les couts de production par période, le cout de l'inventaire, et la demandee reportée par le service commercial
quaters = list(range(5))
cout_production=[600,600,600,600,600]
cout_production_2=[600,600,600,600,600]
cout_stockage=[700,700,700,700,700]
demande=[20,30,50,60,0]


# 2. Définir les variables de décision : Production et Stock - Define Decision Variables: Production and Inventory
x = LpVariable.dicts('quater_prod_', quaters,lowBound=0, cat='Continuous')
y = LpVariable.dicts('quater_stock_', quaters,lowBound=0, cat='Continuous')


# 3. Définir l'objectif , On veut minimiser les coûts de production + de stockage comme dans le problème de université taiwan
model += lpSum([cout_production[i]*x[i] for i in quaters]) + lpSum([cout_production_2[i]*x[i] for i in quaters]) + lpSum([cout_stockage[i]*y[i] for i in quaters])

# Définir les contraintes
# Constrainte de capacité de production (Production-capacity constraints)
for i in quaters:
    model.addConstraint(x[i]<=3000)

# Contrainte de balance de stocks ( Inventory-balance constraints)
model.addConstraint(x[0] - y[0] == demande[0]) # (Month 1)

model += x[0] == 40
model += x[4] == 40

for i in quaters[1:]:
    model.addConstraint(x[i] - y[i] + y[i-1] == demande[i]) # par (jour 2, 3, 4) 

#ON résouds avec le solveur pulp ou un autre entre parenthèses
model.solve()

# On imprime les solutions
for v in model.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(model.objective))

# Autre option pour afficher le slack (QUANTITE INUTILISEE): 

constraints = model.constraints
print(f'Les contraintes sont contenues dans {type(constraints)}')

for name in constraints.keys():
    value = constraints.get(name).value()
    slack = constraints.get(name).slack
    print(f'constraint {name} à la valeur de : {value} et une quantité inutilisée de: {slack}')