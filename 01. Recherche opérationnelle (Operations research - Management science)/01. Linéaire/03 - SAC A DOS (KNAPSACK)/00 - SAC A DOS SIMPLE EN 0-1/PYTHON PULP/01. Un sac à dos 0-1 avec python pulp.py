# Example of use of the Pulp libray for 15-382
# Modeling and solution of a simple knapsack problem
# Gianni A. Di Caro 
#
from pulp import *
import time

# https://pythonhosted.org/PuLP/pulp.html

#
# A list of tuples of items (value, weight)
#
items = [(20,5), (30,6), (10,7), (90,32), (10,2), (40,5), (100,7), (60,9), (70,12), (50,11), (30,1), (20,2)]

# number of items
itemCount = len(items)

# Knapsack max weight capacity
binCapacity = 32


# Decision variables (array), x[i] gets 1 when item i is included in the solution
x = pulp.LpVariable.dicts('item', range(itemCount),
                            lowBound = 0,
                            upBound = 1,
                            cat = 'Integer')

# Initialize the problem and specify the type
problem = LpProblem("Knapsack Problem", LpMaximize)

# Add the objective function
problem += lpSum([ x[i] * (items[i])[0] for i in range(itemCount) ]), "Objective: Maximize profit"

# Capacity constraint: the sum of the weights must be less than the capacity
problem += lpSum([ x[i] * (items[i])[1] for i in range(itemCount) ]) <= binCapacity, "Constraint: Max capacity"

#print problem.constraints

# Write the model to disk, not necessary
problem.writeLP("Knapsack.lp")

# Solve the optimization problem
start_time = time.time()
problem.solve()
print("Solved in %s seconds." % (time.time() - start_time))

# Was the problem solved to optimality?
print("Status:", LpStatus[problem.status])

# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total profit = ", value(problem.objective))

# Some more info about the solution (only variables / items that are selected)
used_cap = 0.0
print "Used items:"
for i in range(itemCount):
    if x[i].value() == 1:
        print i, items[i]
        used_cap += items[i][1]
print "Profit: %d - Used capacity: %d (/ %d)" % (value(problem.objective), used_cap, binCapacity)

