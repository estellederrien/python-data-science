# knapsack-pulp.py

from pulp import *

v = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
limit = 14
items = list(sorted(v.keys()))

# Create model
m = LpProblem("Knapsack", LpMaximize)

# Variables
x = LpVariable.dicts('x', items, lowBound=0, upBound=1, cat=LpInteger)

# Objective
m += sum(v[i]*x[i] for i in items)

# Constraint
m += sum(w[i]*x[i] for i in items) <= limit

# Optimize
m.solve()

# Print the status of the solved LP
print("Status = %s" % LpStatus[m.status])

# Print the value of the variables at the optimum
for i in items:
    print("%s = %f" % (x[i].name, x[i].varValue))

# Print the value of the objective
print("Objective = %f" % value(m.objective))