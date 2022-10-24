# # Import all classes of PuLP module
from pulp import *

workers=[1,2,3,4]
jobs=[1,2,3,4]

# Cost Matrix
costs=[[1,2,1,9],
      [4,5,2,2],
      [7,3,9,3],
      [2,3,5,1]]

prob = LpProblem("Assignment Problem", LpMinimize) 

# The cost data is made into a dictionary
costs= makeDict([workers, jobs], costs, 0)

# Creates a list of tuples containing all the possible assignments
assign = [(w, j) for w in workers for j in jobs]

# A dictionary called 'Vars' is created to contain the referenced variables
vars = LpVariable.dicts("Assign", (workers, jobs), 0, None, LpBinary)

# The objective function is added to 'prob' first
prob += (
    lpSum([vars[w][j] * costs[w][j] for (w, j) in assign]),
    "Sum_of_Assignment_Costs",
)

# There are row constraints. Each job can be assigned to only one employee.
for j in jobs:
    prob+= lpSum(vars[w][j] for w in workers) == 1

# There are column constraints. Each employee can be assigned to only one job.
for w in workers:
    prob+= lpSum(vars[w][j] for j in jobs) == 1

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Print the variables optimized value
for v in prob.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(prob.objective))


# Output:
# Assign_1_1 = 1.0
# Assign_1_2 = 0.0
# Assign_1_3 = 0.0
# Assign_1_4 = 0.0
# Assign_2_1 = 0.0
# Assign_2_2 = 0.0
# Assign_2_3 = 1.0
# Assign_2_4 = 0.0
# Assign_3_1 = 0.0
# Assign_3_2 = 1.0
# Assign_3_3 = 0.0
# Assign_3_4 = 0.0
# Assign_4_1 = 0.0
# Assign_4_2 = 0.0
# Assign_4_3 = 0.0
# Assign_4_4 = 1.0
# Value of Objective Function =  7.0