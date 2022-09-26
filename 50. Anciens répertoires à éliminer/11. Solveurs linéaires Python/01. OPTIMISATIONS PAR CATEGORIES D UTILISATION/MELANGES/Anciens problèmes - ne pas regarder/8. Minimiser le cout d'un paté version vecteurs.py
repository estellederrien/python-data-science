""" 
Problème de paté avec des contraintes qualité protéine et gras .

Version avec des vecteurs 

https://www.coin-or.org/PuLP/CaseStudies/a_blending_problem.html

SOLUTION OK OK OK

On veut remplir une boite de conserve de paté pour chat de 100 grammes sous contrainte de protéines max, gras max, fibres min et sel min exprimées en pourcentages !

 """

import pulp
from pulp import *

# Liste des ingrédients
Ingredients = ['POULET', 'VIANDE']

# cout d'un ingrédient par gramme en euros
costs = {
            'POULET': 0.013, 
            'VIANDE': 0.008
        }

# grammes de protéines par gramme  d'ingrédient
proteinPercent = {
                    'POULET': 0.100, 
                    'VIANDE': 0.200
                 }

# grammes de gras par gramme  d'ingrédient
fatPercent = {
                'POULET': 0.080, 
                'VIANDE': 0.100
              }

# grammes de fibres par gramme  d'ingrédient
fibresPercent = {
                'POULET': 0.001, 
                'VIANDE': 0.005
              }

# grammes de sel par gramme  d'ingrédient
saltPercent = {
                'POULET': 0.002, 
                'VIANDE': 0.005
              }

# On veut minimiser nos couts
prob = LpProblem("The Whiskas Problem", LpMinimize)

# On se sert du dictionnaire Ingredients pour créer nos variables
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)

# Notre function objectif s'exprime en euros ou en dollars
prob += lpSum([costs[i]*ingredient_vars[i] for i in Ingredients]), "Cout total des ingrédients par boite de conserve de 100g"

# La production totale est de 100 g
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 100 ,"PercentagesSum"

# Nos contraintes de qualité pour pas créer un paté de mauvaise qualité ...
prob += lpSum([proteinPercent[i]    * ingredient_vars[i] for i in Ingredients]) >= 8.0, "ProteinRequirement"
prob += lpSum([fatPercent[i]        * ingredient_vars[i] for i in Ingredients]) >= 6.0, "FatRequirement"
prob += lpSum([fibresPercent[i]     * ingredient_vars[i] for i in Ingredients]) <= 2.0, "fibresRequirement"
prob += lpSum([saltPercent[i]       * ingredient_vars[i] for i in Ingredients]) <= 0.4, "saltRequirement"

# POSSIBILITE Utilisation minimale en g par element
# for p in Ingredients:
#    prob += ingredient_vars[p] >= 10, f"min  for product {p}"


prob.writeLP("WhiskasModel2.lp")
prob.solve()
# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chauqe variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
    print (v.name, "=", v.varValue)

# Le résultat de la fonction objectif :
print ("Cout total des ingrédients par boite de conserve de 100g = ", value(prob.objective))


""" 
Ingr_VIANDE = 66.666667
Ingr_POULET = 33.333333
Cout total des ingrédients par boite de conserve de 100g =  0.966666665 """