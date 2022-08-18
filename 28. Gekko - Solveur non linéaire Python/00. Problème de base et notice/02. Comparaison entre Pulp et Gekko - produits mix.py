""" 
https://stackoverflow.com/questions/73409787/gekko-and-pulp-results-differs-but-both-are-valid-why
Gekko and Pulp results differs but both are valid, why?
Asked today
Modified today
Viewed 23 times
0

I have this simple product mix linear program, Pulp and Gekko results differs but results are both valid.

I wonder why and how should I get exactly the same result using both solvers ?

Let's say x1 is the amount of car 1, and x2 the amount of car 2, for example (A simple product mix linear program)... I need to know which cars I need to construct, to maximize my profit.
 """
    from gekko import GEKKO
    m = GEKKO(remote=False) 
    m.options.SOLVER = 1
    
    # Initialize variables
    x1 = m.Var(value=1,lb=0,ub=1000,integer=True)
    x2 = m.Var(value=1,lb=0,ub=1000,integer=True)
    
    # Equations
    m.Equation(2 * x1 + 3 * x2 <= 800)
    m.Equation(2 * x1 + x2 <= 500)
    
    # Objective
    m.Maximize( 2 * x1 + 1 * x2) 
    
    # Steady state optimization
    m.options.IMODE = 3 
    
    # Solve
    m.solve(disp=False) 
    
    print('Results')
    print('x1: ' + str(x1.value))
    print('x2: ' + str(x2.value))
    print('Objective: ' + str(m.options.objfcnval))
    
    Results
    x1: [184.0]
    x2: [132.0]
    Objective: -500.0

# And, next, this is my Python Pulp code, You will notice that Python Pulp only choose the x1 variable, while Gekko seems to balance between the x1 and the x2 variables ; both results are valid, and constraints does not get exceeded:

import pulp 
  
model = pulp.LpProblem("Maximize", pulp.LpMaximize)
  
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
  
model +=  2 * x1 + 1 * x2, "Profit"

model += 2 * x1 + 3 * x2 <= 800
model += 2 * x1 + x2 <= 500

model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print ("x1 = {}".format(x1.varValue))
print ("x2 = {}".format(x2.varValue))
  
# Print our objective function value
print (pulp.value(model.objective))

Results
x1 = 250.0
x2 = 0.0
500.0

# Can somebody please tell me if that is a normal behavior, and how should I get the same behavior on both solvers ?

# ( Secondary question : I don't know why the Gekko objective result is negative ... )
