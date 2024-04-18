""" 
 PLANIFICATION DE PRODUCTION MULTI PERIODE AVEC PRISE EN COMPTE DES STOCKS
 MINIMISATION DES COUTS


Source : Taiwan University  : 2022 https://www.coursera.org/learn/operations-research-modeling/lecture/vW447/2-8-simple-lp-formulation-production-and-inventory
Source 2 :  https://machinelearninggeek.com/solvingmulti-period-production-scheduling-problem-in-python-using-pulp/
Source 3 : http://www.columbia.edu/itc/sipa/U6033/client_edit/lectures/lec4.pdf
Source 4 : https://linuxtut.com/en/0d2a01c66230e0dc6fe9/ """


""" Histoire : 
Quand on veut faire des décisions, On veut se soucier de ce qui se passe dans le futur.
Ici, on parle de problèmes Multi Périodes ( Dates multiples)

Le plus souvent, les produits que l'on fait sont stockés et vendus plus tard.
parfois, le prix futur varie, la production est plus moins chère, ou la capacité par jour n'est pas suffisante...

Donc la décision de production doit être prise en onjonction avec la décision de l'inventaire.

Si on prends un exmple sur 4 jours différents, on a donc 
- la quantité à produire du fait de la demandee par jour
- le côut de production par jour ( par exemple si c'est le dimanche , c'est plus cher de produire)
- le coût de l'entretien des stocks est de 1 euro par jour par unité de produit vendu donc si on garde un produit 3 jours, le cout sera de 3 euros """

# NOTE : Cette version utilise des boucles FOR à la place du premier exemple ou les vars de décision sont écrites en dur ! ELLE TROUVE LE MEME RESULTAT
# Ce code fonctionne et retrouve le même résultat que http://www.columbia.edu/itc/sipa/U6033/client_edit/lectures/lec4.pdf sur le problème nuMéro 10
""" HISTOIRE COMPLETE DE TAIWAN UNIVERSITY: 
LE MANAGER DIT QUON VA VENDRE 100 , 150, 200 et 170 les jours 1 ,2 , 3 et 4 de la prochine semaine.
LES COUTS DE PROD VARIENT EN FONCTION DES JOURS : 9e 12e 10e ET 12e les jours 1 ,2 , 3 et 4 de la prochine semaine.
LE COUT DE STOCKAGE EST DE 1 E PAR OBJET STOCKE DONC SI ON LE GARDE 4 JOURS CA FAIT 4 EUROS DE COUT 
QUEL EST LE MEILLEUR PLAN DE PRODUCTION POUR MINIMISER LES COUTS ET NE PAS AVOIR TROP DE STOCKS ?

"""


# Importer PULP
from pulp import *

# 1. On veut minimiser Les coûts de production, et d'inventaire.
model = LpProblem("Minimiser le cout",LpMinimize)

# ON définit les couts de production et de stockage pour les jours 1 2 3 ET 4 ; Dans quaters, c'est le nombre de jours SOIT 4. Define production cost, inventory cost, and demande.
# Définir les couts de production par période, le cout de l'inventaire, et la demandee reportée par le service commercial
quaters = list(range(4))
cout_production=[9,12,10,12]
cout_stockage=[1,1,1,1]
demande=[100,150,200,170]


# 2. Définir les variables de décision : Production et Stock - Define Decision Variables: Production and Inventory
x = LpVariable.dicts('quater_prod_', quaters,lowBound=0, cat='Continuous')
y = LpVariable.dicts('quater_stock_', quaters,lowBound=0, cat='Continuous')


# 3. Définir l'objectif , On veut minimiser les coûts de production + de stockage comme dans le problème de université taiwan
model += lpSum([cout_production[i]*x[i] for i in quaters]) + lpSum([cout_stockage[i]*y[i] for i in quaters])

# Définir les contraintes
# Constrainte de capacité de production (Production-capacity constraints)
for i in quaters:
    model.addConstraint(x[i]<=3000)

# Contrainte de balance de stocks ( Inventory-balance constraints)
model.addConstraint(x[0] - y[0] == demande[0]) # (Month 1)

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