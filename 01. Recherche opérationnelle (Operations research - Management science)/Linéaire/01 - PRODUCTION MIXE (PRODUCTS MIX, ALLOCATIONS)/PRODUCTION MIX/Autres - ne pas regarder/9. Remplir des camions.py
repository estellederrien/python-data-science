# A étudier
# 3D bin packing
# https://stackoverflow.com/questions/54709977/how-can-i-change-my-script-so-it-minimizes-the-cost-and-at-the-same-time-calcul
# see also pyshipping and https://bitbucket.org/kent37/python-tutor-samples/src/f657aeba5328/BinPacking.py

from pulp import *
import numpy as np

# Item masses, volumes
item_mass = [16, 10, 5]
item_vol = [25, 12, 1]
n_items = len(item_vol)
set_items = range(n_items)

# Mass & volume capacities of trucks
truck_mass = [7, 15, 15, 15, 18, 38, 64, 100]
truck_vol = [25, 50, 50, 50, 100, 125, 250, 500]

# Cost of using each truck
truck_cost = [7, 1.5, 1.5, 1.5, 18, 380, 640, 1000]

n_trucks = len(truck_cost)
set_trucks = range(n_trucks)

y = pulp.LpVariable.dicts('truckUsed', set_trucks,
    lowBound=0, upBound=1, cat=LpInteger)

x = pulp.LpVariable.dicts('itemInTruck', (set_items, set_trucks), 
    lowBound=0, upBound=1, cat=LpInteger)

# Model formulation
prob = LpProblem("Truck allocation problem", LpMinimize)

# Objective
prob += lpSum([truck_cost[i] * y[i] for i in set_trucks])

# Constraints
for j in set_items:
    # Every item must be taken in one truck
    prob += lpSum([x[j][i] for i in set_trucks]) == 1

for i in set_trucks:
    # Respect the mass constraint of trucks
    prob += lpSum([item_mass[j] * x[j][i] for j in set_items]) <= truck_mass[i]*y[i]

    # Respect the volume constraint of trucks
    prob += lpSum([item_vol[j] * x[j][i] for j in set_items]) <= truck_vol[i]*y[i]

# Ensure y variables have to be set to make use of x variables:
for j in set_items:
    for i in set_trucks:
        x[j][i] <= y[i]


prob.solve()

x_soln = np.array([[x[i][j].varValue for i in set_items] for j in set_trucks])
y_soln = np.array([y[i].varValue for i in set_trucks])

print (("Status:"), LpStatus[prob.status])
print ("Total Cost is: ", value(prob.objective))
print("x_soln"); print(x_soln)
print("y_soln"); print(y_soln)

print("Trucks used: " + str(sum(([y_soln[i] for i in set_trucks]))))

for i in set_items:
    for j in set_trucks:
        if x[i][j].value() == 1:
            print("Item " + str(i) + " is packed in vehicle "+ str(j))

totalitemvol = sum(item_vol)

totaltruckvol = sum([y[i].value() * truck_vol[i] for i in set_trucks])
print("Volume of used trucks is " + str(totaltruckvol))

if(totaltruckvol >= totalitemvol):
  print("Trucks are sufficient")
else:
  print("Items cannot fit")