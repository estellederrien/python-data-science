Python pulp package: Codes
# Import Library
from pulp import *
# Lsit (TimePeriods from january to june)
t = [0,1,2,3,4,5,6
# Import Library
from pulp import *
# Lsit (TimePeriods)
t = [0,1,2,3,4,5,6]
# Parameters and Data
demand = {1:110, 2:110, 3:120, 4:210,
5:160, 6:110}
# Demand data
UPC = {1:8, 2:7, 3:7, 4:9, 5:6, 6:9}
# Unit Production Cost (Excluding Labor)
UHC = {1:2, 2:5, 3:5, 4:3, 5:4, 6:3}
# Unit Holding Cost
UBC = {1:15, 2:20, 3:25, 4:30, 5:25, 6:15}
# Unit Back order cost
URLC = {1:18, 2:17, 3:19, 4:17, 5:15, 6:17}
# Unit Regular Labor Cost
UOLC = {1:23.5, 2:24.5, 3:28, 4:28, 5:23.5, 6:23.5}
# Unit Overtime Labor Cost
HC = {1:22, 2:22, 3:22, 4:22, 5:22, 6:22}
# hiring cost
FC = {1:20, 2:20, 3:20, 4:20, 5:20, 6:15}
#firing cost
# Setting the Problem
prob = LpProblem("Aggregate Production
Planning: Variable Work Force Model",
LpMinimize)
# Decision Variables
Xt = LpVariable.dicts("Quantity Produced",
t, 0, None, LpInteger)
It = LpVariable.dicts("Inventory", t, 0)
Bt = LpVariable.dicts("Backorder", t, 0)
Rt = LpVariable.dicts("R_Labor Used", t, 0)
Ot = LpVariable.dicts("O_Labor Used", t, 0)
Ht = LpVariable.dicts("Labours Hired", t, 0)
Ft = LpVariable.dicts("Labours Fired", t, 0)
# Objective Function
prob + = lpSum(UPC[i]*Xt[i]
for i in t[1:]) + lpSum(UHC[i]*It[i]
for i in t[1:]) + lpSum(UBC[i]*Bt[i]
for i in t[1:]) + lpSum(URLC[i]*Rt[i]
for i in t[1:]) + lpSum(UOLC[i]*Ot[i]
for i in t[1:]) + lpSum(HC[i]*Ht[i]
for i in t[1:]) + lpSum(FC[i]*Ft[i]
for i in t[1:])
# Constraints
It[0] = 4
Rt[0] = 0
Bt[0] = 0
for i in t[1:]:
prob + = (Xt[i] + It[i−1] − It[i] −
Bt[i−1] + Bt[i]) = demand[i]
# Inventory-Balancing Constraints

for i in t[1:]:
prob + = Xt[i] − 1*(Rt[i] + Ot[i])
<= 0
# Time Required to produce products
for i in t[1:]:
prob + = Rt[i] − Rt[i−1] − Ht[i] + Ft[i] = 0
# Regular Time Required
for i in t[1:]:prob + = (Ot[i] − 0.25*Rt[i]) <= 0
# Regular Time Required
# Solving the problem
prob.solve()
print("Solution Status =", LpStatus[prob.status])
# Print the solution of the Decision Variables
for v in prob.variables():
if v.varValue>0:
print(v.name, "=", v.varValue)
# Print Optimal solution
print("Total Production Plan Cost = ",
value(prob.objective)