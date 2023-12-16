"""
The Simplified Sponge Roll Problem for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell   2007
"""

# Import PuLP modeler functions
from pulp import *

# Une liste de toutes les longueurs de rouleaux que le consommateur peut commander
LenOpts = ["5", "7", "9"]

# Un dictionnaire de la demande pour chaque longueur désirée par les consommateurs
rollDemand = {"5": 150, "7": 200, "9": 300}

# Une liste de tous les modèles est créée
PatternNames = ["A", "B", "C"]

# Quand on découpe un rouleau, il y a plusieurs solutions possibles, on appelle cela un pattern.
# CA SE LIT EN COLONNE DANS LE PATTERN A ON A 7+9 LONGUEURS DANS LE PATTERN B ON A 2*5+9 longueurs, ça fait toujour smoins de 20 
patterns =    #A  B  C
            [[0, 2, 2], #  5
             [1, 1, 0], # 7
             [1, 0, 1]]  #  9

# Le coût de chaque rouleau de 20 cm de long utilisé
cost = 1

# Les données de modèle sont transformées en un dictionnaire
patterns = makeDict([LenOpts, PatternNames], patterns, 0)

# Les variables de problème du nombre de chaque motif à faire sont créées
vars = LpVariable.dicts("Patt", PatternNames, 0, None, LpInteger)

# La variable 'prob' est créée
prob = LpProblem("Cutting Stock Problem", LpMinimize)

# La fonction objectif est saisie : le nombre total de gros rouleaux utilisés * le coût fixe de chacun
prob += lpSum([vars[i] * cost for i in PatternNames]), "Production Cost"

# La contrainte minimale de demande est saisie
for i in LenOpts:
    prob += (
        lpSum([vars[j] * patterns[i][j] for j in PatternNames]) >= rollDemand[i],
        "Ensuring enough %s cm rolls" % i,
    )

# The problem data is written to an .lp file
prob.writeLP("SpongeRollProblem.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Production Costs = ", value(prob.objective))