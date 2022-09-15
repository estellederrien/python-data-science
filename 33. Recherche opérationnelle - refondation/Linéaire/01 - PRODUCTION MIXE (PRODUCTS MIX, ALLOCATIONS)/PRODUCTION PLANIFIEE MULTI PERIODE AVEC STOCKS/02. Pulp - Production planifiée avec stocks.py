"""
 PLANIFICATION DE PRODUCTION MULTI PERIODE AVEC PRISE EN COMPTE DES STOCKS
Source  :  https://machinelearninggeek.com/solvingmulti-period-production-scheduling-problem-in-python-using-pulp/

lE RéSULTAT EST IDENTIQUE à EXCEL ET COLUMBIA UNIVERSITY :
http://www.columbia.edu/itc/sipa/U6033/client_edit/lectures/lec4.pdf
"""

# Import all classes of PuLP module
from pulp import *

# 1. Initialize Class
model = LpProblem("Minimize Cost",LpMinimize)

# Define production cost, inventory cost, and demand.
quaters = list(range(4))
prod_cost=[3000, 3300, 3600, 3600]
inv_cost=[250, 250, 250, 250]
demand=[2300, 2000, 3100, 3000]

# 2. Define Decision Variables: Production and Inventory
x = LpVariable.dicts('quater_prod_', quaters,lowBound=0, cat='Continuous')
y = LpVariable.dicts('quater_inv_', quaters,lowBound=0, cat='Continuous')

# 3. Define Objective
model += lpSum([prod_cost[i]*x[i] for i in quaters]) + lpSum([inv_cost[i]*y[i] for i in quaters])

# Define Constraints
# Production-capacity constraints
for i in quaters:
    model.addConstraint(x[i]<=3000)

# Inventory-balance constraints
model.addConstraint(x[0] - y[0] == demand[0]) # (Month 1)

for i in quaters[1:]:
    model.addConstraint(x[i] - y[i] + y[i-1] == demand[i]) # for (Month 2, 3, 4) 

    # The problem is solved using PuLP's choice of Solver
model.solve()

# Print the variables optimized value
for v in model.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(model.objective))