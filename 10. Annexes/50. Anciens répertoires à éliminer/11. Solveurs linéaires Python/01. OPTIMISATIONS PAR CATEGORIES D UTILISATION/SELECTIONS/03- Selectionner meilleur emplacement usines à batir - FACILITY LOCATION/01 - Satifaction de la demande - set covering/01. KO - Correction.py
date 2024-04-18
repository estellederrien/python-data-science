# Source : AirSquid - StackOverflow
"""
Batir le minimum de batiments tout en comblant l'intégralité de la demande
https://www.coursera.org/learn/operations-research-modeling/lecture/gAB39/3-5-facility-location-covering
"""
# Import PuLP modeler functions
from pulp import *


prob = LpProblem('source minimzer', LpMinimize)
dist_limit = 5
sources = ['A', 'B']            # the source locations

# note this is zero-indexed to work with the list indexes in dist dictionary...

destinations = list(range(5))   # the demand locations 0, 1, 2, 3, 4   

dist = {    'A': [2, 23, 30, 54, 1],
            'B': [3, 1, 2, 2, 3]}

covered = LpVariable.dicts('covered', [(s, d) for s in sources for d in destinations], cat='Binary')

print (covered)
# set up constraint to limit covered if the destination is "reachable"
for s in sources:
    for d in destinations:
        print("--------- covered-------")
        print(covered[s, d] )
        print(dist[s][d])
        prob += covered[s, d] * dist[s][d] <= dist_limit

# add one more constraint to make sure that every destination is "covered"...

# The problem data is written to an .lp file
prob.writeLP("SetCovering.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Locations  = ", prob.objective)

constraints = prob.constraints

print(constraints)

for name in constraints.keys():
    value = constraints.get(name).value()
    slack = constraints.get(name).slack
    print(f'constraint {name} à la valeur de : {value} et une quantité inutilisée de: {slack}')
