# https://stackoverflow.com/questions/43124589/how-use-indices-and-import-data-for-python-pulp-mathematical-optimization
# Traveling Salesman Problem (TSP) Simplified Model
# Date: 2017-03-30
# """

# # Import PuLP modeler functions
from pulp import *

# # Create the 'prob' variable to contain the problem data
prob = LpProblem("The TSP Problem1",LpMinimize)


# Formulation summary
#   The decision variable x is equal to 1 or 0, whether the path is chosen
#   Each path has a cost associated with it
#   The objective is to choose the shortest path
#   The constraint, essentially, is that each location is visited

# The LpVariable class has four parameters
    # the first is an arbitrary name
    # the second is the lower bound
    # the third is the upper bound
    # the fourth is the type of data, discrete or continuous
x12=LpVariable("flow12",0,None,LpInteger)
x13=LpVariable("flow13",0,None,LpInteger)
x21=LpVariable("flow21",0,None,LpInteger)
x23=LpVariable("flow23",0,None,LpInteger)
x31=LpVariable("flow31",0,None,LpInteger)
x32=LpVariable("flow32",0,None,LpInteger)

# The objective function is added to 'prob' first
# the objective is to minimize the total distance traveled 
# the numbers represent the distances between two variables

prob += 30*x12 + 5*x13 +25*x21 + 1*x23 + 5*x31 + 8*x32, "Total Distance Traveled"


# The constraints: 

# each location needs to be on the route but only once
prob += x12 + x32 == 1.0, "Location2 is visited"
prob += x13 + x23 == 1.0, "Location3 is visited"
prob += x21 + x31 == 1.0, "Location1 is visited"

# each location is departed exactly once
prob += x31 + x32 == 1.0, "Location3 is departed"
prob += x21 + x23 == 1.0, "Location2 is departed"
prob += x12 + x13 == 1.0, "Location is departed"

# The problem data is written to an .lp file
prob.writeLP("SupplyChainAssignment.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimized objective function value is printed to the screen
print "Total Cost TSP Assignment = ", value(prob.objective)