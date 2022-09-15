# Source : 
# https://stackoverflow.com/questions/42450533/bin-packing-python-query-with-variable-bin-cost-and-sizes

 #https://www.py4u.net/discuss/203834

from pulp import *

items = [("a", 5), ("b", 6), ("c", 7)]

itemCount = len(items)
maxBins = 3
binCapacity = [11, 15, 10]
binCost = [10, 30, 20]

y = pulp.LpVariable.dicts('BinUsed', range(maxBins), lowBound = 0, upBound = 1,  cat='Integer')
possible_ItemInBin = [(itemTuple[0], binNum) for itemTuple in items for binNum in range(maxBins)]
x = pulp.LpVariable.dicts('itemInBin', possible_ItemInBin, lowBound = 0, upBound = 1,  cat='Integer')

# Model formulation
prob = LpProblem("Bin Packing Problem", LpMinimize)

# Objective
prob += lpSum([binCost[i] * y[i] for i in range(maxBins)])

# Constraints
for j in items:
    prob += lpSum([x[(j[0], i)] for i in range(maxBins)]) == 1
for i in range(maxBins):
    prob += lpSum([items[j][1] * x[(items[j][0], i)] for j in range(itemCount)]) <= binCapacity[i]*y[i]
prob.solve()

print("Bins used: " + str(sum(([y[i].value() for i in range(maxBins)]))))
for i in x.keys():
    if x[i].value() == 1:
        print("Item {} is packed in bin {}.".format(*i))