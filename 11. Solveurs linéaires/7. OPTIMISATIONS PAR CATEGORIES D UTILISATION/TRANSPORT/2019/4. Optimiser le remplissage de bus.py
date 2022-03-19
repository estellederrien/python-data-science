""" 

SOURCE : https://alexfleischer-84755.medium.com/optimization-simply-do-more-with-less-zoo-buses-and-kids-66940178db6


DESCRIPTION : 
300 enfants doivent se rendre au zoo de Londres. 
L'école peut louer des bus de 40 places et 30 places pour 500 $ et 400 $. 
Combien de bus de chacun pour minimiser les coûts?
Pour de nombreuses personnes, la réponse est simple, voire insignifiante. 
Un siège coûte 12,50 $ pour les autobus de 40 sièges et 13,33 $ pour les autobus de 30 sièges.
 On devrait donc préférer les bus 40 places aux bus 30 places. 
 Nous dépensons donc d'abord 3500 $ (7 * 500 $) pour 7 autobus et 280 enfants, 
 puis nous ajoutons un huitième autobus pour 400 $ (30 sièges) pour les 20 enfants restants. 
 Le coût total est de 3900 $.

Cela a l'air bien. Mais ce n'est pas la meilleure solution. 
Avec 6 bus 40 places (240 enfants et 3000 $) et 2 bus 30 places (60 enfants, 800 $), 
nous pouvons déplacer les enfants et ne payer que 3800 $). Nous pouvons économiser 100 $! 

"""


import pulp
solver_list = pulp.listSolvers(onlyAvailable=True)
print(solver_list)

# import cplex

bus_problem = pulp.LpProblem("bus", pulp.LpMinimize)

nbBus40 = pulp.LpVariable('nbBus40', lowBound=0, cat='Integer')
nbBus30 = pulp.LpVariable('nbBus30', lowBound=0, cat='Integer')

# Objective function
bus_problem += 500 * nbBus40 + 400 * nbBus30, "cost"

# Constraints
bus_problem += 40 * nbBus40 + 30 * nbBus30 >= 300

bus_problem.solve()

print(pulp.LpStatus[bus_problem.status])

for variable in bus_problem.variables():
    print ("{} = {}".format(variable.name, variable.varValue))