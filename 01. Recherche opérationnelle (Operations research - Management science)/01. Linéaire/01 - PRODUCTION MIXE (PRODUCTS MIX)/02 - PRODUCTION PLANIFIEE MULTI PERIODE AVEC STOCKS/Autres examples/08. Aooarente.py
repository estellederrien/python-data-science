"""
https://stackoverflow.com/questions/59814034/transforming-a-logic-constraint-into-python-pulp-code

 Une entreprise planifie son activité sur une période de trois mois. 
Il peut produire 110 unités au coût de 600 chacune.
 Le montant minimum qu'il doit produire par mois est de 15 unités s'il est actif 
 (mais bien sûr, il peut choisir d'être fermé pendant le mois et de produire 0 unités).
  Chaque mois, il peut sous-traiter la production de 60 unités, au coût de 660 chacune.
  Le stockage d'une unité pendant un mois coûte 20 $ par unité par mois.
   Le service marketing a prévu des ventes de 100, 130 et 150 unités pour les trois prochains mois, respectivement.
    L'objectif est de répondre à la demande chaque mois tout en minimisant le coût total




J'en ai déduit qu'il nous fallait une fonction objectif de la forme min[Sum(i=0..3) 600*x1+660*x2+20*x3].
 Nous devons ajouter des contraintes sur x1>=15, et sur x2 0<=x2<=60 
 Nous aurons également besoin d'une autre contrainte pour chaque mois... 
 Pour la première i=1 => x1+x2 = 100 - x3last (x3last est une variable supplémentaire qui 
 devrait contenir le montant existant en dépôt du mois précédent), et pour i=2 et i=3 mêmes contraintes. 
 Je n'ai aucune idée de comment écrire ceci en pulpe, et j'apprécierais de l'aide. Merci ^_

 """
from pulp import *
all_i = [1,2,3]
all_i_with_0 = [0,1,2,3]
sales = {1:100, 2:130, 3:150}

o = LpVariable.dicts('open', all_i, cat='Binary')
p =LpVariable.dicts('production', all_i, cat='Linear')
s =LpVariable.dicts('stored', all_i_with_0, lowBound=0, cat='Linear')
e =LpVariable.dicts('external', all_i, lowBound=0, cat='Linear')

prob = LpProblem("MinCost", LpMinimize)
prob += lpSum([p[i]*600 + s[i]*20 + e[i]*660 for i in all_i]) # Objective
for i in all_i:
    prob += p[i] >= o[i]*15
    prob += p[i] <= o[i]*110
    prob += e[i] <= 60
    prob += p[i] + e[i] + s[i-1] == sales[i] + s[i]

prob += s[0] == 0 # No stock inherited from previous monts
prob.solve()

# The status of the solution
print ("Status:", LpStatus [prob.status])

# Dislay the optimums of each var
for v in prob.variables ():
    print (v.name, "=", v.varValue)

# Objective fcn
print ("Obj. Fcn: ", value(prob.objective))