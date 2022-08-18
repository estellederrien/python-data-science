from gekko import GEKKO

m = GEKKO(remote=False) # Initialize gekko

# Use IPOPT solver (default)
m.options.SOLVER = 3

# Initialize variables
x1 = m.Var(value=1,lb=1,ub=1000)
x2 = m.Var(value=1,lb=1,ub=1000)

# Equations
m.Equation(2 * x1 + 3 * x2 <= 800)
m.Equation(2 * x1 + x2 <= 500)

# Objective
m.Maximize( 2 * x1 + 1 * x2) 
# m.Obj((160 - 0,4 * x1) * x1 + (135 - 0,2 * x2 ) * x2) 

m.options.IMODE = 3 # Steady state optimization

m.solve(disp=False) # Solve

print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('Objective: ' + str(m.options.objfcnval))