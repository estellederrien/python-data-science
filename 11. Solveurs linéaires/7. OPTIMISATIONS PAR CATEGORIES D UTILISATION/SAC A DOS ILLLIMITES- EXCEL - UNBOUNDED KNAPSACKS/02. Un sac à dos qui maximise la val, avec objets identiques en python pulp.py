# source https://stackoverflow.com/questions/55193756/select-the-same-item-several-times-in-the-knapsack-problem-pulp
""" 

UNe amée a une budget de 1000, quels objets choisir 



You need to make two very small changes to your code. Firstly you need to remove the upper 
bound you have set on your x variables. At the moments you have binary variables x[i] which can be only one or zero.

Secondly you need to add in the constraints which effectively set a custom upper 
bound for each of the items. Working code and resulting solution below 
- as you can see multiple wrenches (the highest v/w ratio) 
are chosen, with a single hammer to fill up the small amount of space left. 
"""

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