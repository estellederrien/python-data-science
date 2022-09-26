from gekko import GEKKO

m = GEKKO(remote=False) # Initialize gekko


m.options.SOLVER = 1

# Initialize variables
x1 = m.Var(value=1,lb=0,ub=1000,integer=False)
x2 = m.Var(value=1,lb=0,ub=1000,integer=False)

# Equations
m.Equation(1 * x1 + 2 * x2 == 40)


# Objective
# maximize Z = (4 - 0.1x1)x1 + (5 - 0.2x2) x2

m.Maximize((4 - (0.1 * x1)) * x1 + (5 - (0.2 * x2 )) * x2) 


m.options.IMODE = 3 # Steady state optimization

m.solve(disp=False) # Solve

print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('Objective: ' + str(m.options.objfcnval))

# Les résultats sont identiques au fichier EXCEL
# Results
# x1: [18.333333333]
# x2: [10.833333333]
# Objective: -70.416666667



