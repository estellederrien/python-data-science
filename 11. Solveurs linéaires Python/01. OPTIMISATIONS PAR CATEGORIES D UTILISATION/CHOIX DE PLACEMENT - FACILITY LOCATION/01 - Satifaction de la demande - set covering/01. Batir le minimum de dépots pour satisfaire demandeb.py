"""
Batir le minimum de batiments tout en comblant l'intégralité de la demande
https://www.coursera.org/learn/operations-research-modeling/lecture/gAB39/3-5-facility-location-covering
"""

# Import PuLP modeler functions
from pulp import *

# SET OF LOCATIONS J
Locations = ["A", "B"]

# SET OF DEMANDS I
Demands = ["1", "2", "3", "4", "5"]

#  SET OF DISTANCES ij
distances = [  # Demands I
    # 1 2 3 4 5
    [2, 23, 5, 2, 1],  # A   Locations J
    [3, 1, 10, 2, 3],  # B
]

# Min value to get covered
s = 5

covered = [[
    [1,0,1,1,1],
    [1,1,0,1,1]
]]

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Set covering", LpMinimize)

# # Problem variables 
I = LpVariable.dicts("locations", Locations, cat='Binary')
J = LpVariable.dicts("demand", Demands, cat='Binary')


# The distance data is made into a dictionary
distances = makeDict([Locations, Demands], distances, 0)

print("--------------------distances-------------------------------------")
print(distances)
print("--------------------distances-------------------------------------")

# Creates a list of tuples containing all the possible routes for transport
Routes = [(w, b) for w in Locations for b in Demands]
print("--------------------routes-------------------------------------")
print(Routes)
print("--------------------routes-------------------------------------")

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route", (Locations, Demands), 0, None, LpInteger)
print("--------------------vars-------------------------------------")
print(vars)
print("--------------------vars-------------------------------------")

# The objective function is added to 'prob' first
prob += lpSum(I)

# The supply maximum constraints are added to prob for each supply node (warehouse)
# for w in Locations:
# prob += (
#     lpSum([vars[w][b] for b in Demands]) <= 1,
#     "Sum_of_Products_out_of_Warehouse_%s" % w,
# )

# The demand minimum constraints are added to prob for each demand node (bar)
# for b in Demands:
#     prob += (
#         lpSum([vars[w][b] for w in Locations]) >= demand[b],
#         "Sum_of_Products_into_Bar%s" % b,
#     )




# The problem data is written to an .lp file
prob.writeLP("SetCovering.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Locations  = ", value(prob.objective))

