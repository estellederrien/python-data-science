""" 
 PLANIFICATION DE PRODUCTION MULTI PERIODE AVEC PRISE EN COMPTE DES STOCKS
 MINIMISATION DES COUTS
 EXAMPLE LE PLUS SIMPLIFIE POSSIBLE

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


""" HISTOIRE COMPLETE DE TAIWAN UNIVERSITY: 
LE MANAGER DIT QUON VA VENDRE 100 , 150, 200 et 170 les jours 1 ,2 , 3 et 4 de la prochine semaine.
LES COUTS DE PROD VARIENT EN FONCTION DES JOURS : 9e 12e 10e ET 12e les jours 1 ,2 , 3 et 4 de la prochine semaine.
LE COUT DE STOCKAGE EST DE 1 E PAR OBJET STOCKE DONC SI ON LE GARDE 4 JOURS CA FAIT 4 EUROS DE COUT 
QUEL EST LE MEILLEUR PLAN DE PRODUCTION POUR MINIMISER LES COUTS ET NE PAS AVOIR TROP DE STOCKS ?

"""


# Importer PULP
from pulp import *

# 1. On veut minimiser Les coûts de production + de stockage.
problem = LpProblem("Problem",LpMinimize)


# Les Variables de décision
# production d'objets par jour 1 , 2 , 3 et 4
P1 = pulp.LpVariable('Prodution1', lowBound=0, cat='Integer')
P2 = pulp.LpVariable('Prodution2', lowBound=0, cat='Integer')
P3 = pulp.LpVariable('Prodution3', lowBound=0, cat='Integer')
P4 = pulp.LpVariable('Prodution4', lowBound=0, cat='Integer')


# Stocks par jour 1 , 2 , 3 et 4
S1 = pulp.LpVariable('Stock1', lowBound=0, cat='Integer')
S2 = pulp.LpVariable('Stock2', lowBound=0, cat='Integer')
S3 = pulp.LpVariable('Stock3', lowBound=0, cat='Integer')
S4 = pulp.LpVariable('Stock4', lowBound=0, cat='Integer')

#Objective function : On veut minimiser Le cout de prod + Le cout de stockage
problem += (9*P1 + 12*P2 + 10*P3 + 12*P4) + (S1 + S2 + S3 + S4) 

# Les contraintes de balance d'inventaire - Inventory balancing constraints
problem += P1 - 100 == S1
problem += S1 + P2 - 150 == S2
problem += S2 + P3 - 200 == S3
problem += S3 + P4 - 170 == S4

problem += P1 >= 0
problem += P2 >= 0 
problem += P3 >= 0 
problem += P4 >= 0 

#Confirmation of problem definition
print(problem)

# On résouds 
result = problem.solve()

#On imprime les résultats
print("---Premier jour---")
print("Production:" ,pulp.value(P1))
print("Stock:" ,pulp.value(S1))


print("---2nd jour---")
print("Production:" ,pulp.value(P2))
print("Stock:" ,pulp.value(S2))

print("---3rd jour---")
print("Production3:" ,pulp.value(P3))
print("Stock:" ,pulp.value(S3))

print("---4eme jour---")
print("Production:" ,pulp.value(P4))
print("Stock:" ,pulp.value(S4))

print("Cout global:" ,pulp.value(problem.objective))




# Autre méthode d'impression des solutions
for v in problem.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(problem.objective))

# Autre option pour afficher le slack (QUANTITE INUTILISEE): 

constraints = problem.constraints
print(f'Les contraintes sont contenues dans {type(constraints)}')

for name in constraints.keys():
    value = constraints.get(name).value()
    slack = constraints.get(name).slack
    print(f'constraint {name} à la valeur de : {value} et une quantité inutilisée de: {slack}')