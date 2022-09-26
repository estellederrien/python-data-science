# knapsack.py

from pyomo_simplemodel import *

v = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
limit = 14
items = list(sorted(v.keys()))

# Create model
m = SimpleModel(maximize=True)

# Variables
x = m.var('m', items, within=Binary)

# Objective
m += sum(v[i]*x[i] for i in items)

# Constraint
m += sum(w[i]*x[i] for i in items) <= limit


# Optimize
status = m.solve('glpk')

# Print the status of the solved LP
print("Status = %s" % status.solver.termination_condition)

# Print the value of the variables at the optimum
for i in items:
    print("%s = %f" % (x[i], value(x[i])))

# Print the value of the objective
print("Objective = %f" % value(m.objective()))
