#https://github.com/hakeemrehman/Python-PuLP-/blob/master/Giapetto%20LP%20Problem.ipynb

# Import PuLP modeler functions
from pulp import *



# Create a LP maximization problem
prob = LpProblem("Giapetto", LpMaximize)  





# LpVariable(variable name, lower Bound=None, uppper Bound=None, catagory='Continuous')
x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Create another variable x2 >= 0



# Objective Function
prob += 20*x1 + 30*x2  
# prob += 20*x1 + 30*x2, "obj"

# Constraints
prob += 1*x1 + 2*x2 <= 100  # Finishing hours
prob += 2*x1 + 1*x2 <= 100  # Carpentry hours

# prob += 1*x1 + 2*x2 <= 100,"Finishing hours"
# prob += 2*x1 + 1*x2 <= 100,"Carpentry hours"



# Display the LP problem
prob



# Solve with the default solver
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Show the solution (1st Approach)
value(x1), value(x2), value(prob.objective) 

# Show the solution (2nd Approach)
for v in prob.variables():
    print (v.name, "=", v.varValue, "\tReduced Cost =", v.dj)

print ("objective=", value(prob.objective))


print ("\nSensitivity Analysis\nConstraint\t\tShadow Price\tSlack")
for name, c in prob.constraints.items():
    print (name, ":", c, "\t", c.pi, "\t\t", c.slack)
