https://stackoverflow.com/questions/55193756/select-the-same-item-several-times-in-the-knapsack-problem-pulp

from pulp import *
v = {'hammer':6, 'wrench':10, 'screwdriver':8, 'towel':40}
w = {'hammer':13, 'wrench':21, 'screwdriver':17, 'towel':100}
q = {'hammer':1000, 'wrench':400, 'screwdriver':500, 'towel':150}
limit = 1000
items = list(sorted(v.keys()))

# Create model
m = LpProblem("Knapsack", LpMaximize)

# Variables
x = LpVariable.dicts('x', items, lowBound=0, cat=LpInteger)

# Objective
m += sum(v[i]*x[i] for i in items)

# Constraint
m += sum(w[i]*x[i] for i in items) <= limit

# Quantity of each constraint:
for i in items:
    m += x[i] <= q[i]


# Optimize
m.solve()

# Print the status of the solved LP
print("Status = %s" % LpStatus[m.status])

# Print the value of the variables at the optimum
for i in items:
    print("%s = %f" % (x[i].name, x[i].varValue))

# Print the value of the objective
print("Objective = %f" % value(m.objective))
print("Total weight = %f" % sum([x[i].varValue*w[i] for i in items]))


""" x_hammer = 1.000000
x_screwdriver = 0.000000
x_towel = 0.000000
x_wrench = 47.000000
Objective = 476.000000
Total weight = 1000.000000 """