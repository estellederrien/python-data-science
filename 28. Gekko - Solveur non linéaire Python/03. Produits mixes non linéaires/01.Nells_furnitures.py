from gekko import GEKKO

m = GEKKO(remote=False) # Initialize gekko

#The example problem that you referenced uses the default IPOPT solver. To get a binary or integer solution, switch to the APOPT solver.
m.options.SOLVER = 1

# Initialize variables
x1 = m.Var(value=1,lb=0,ub=1000,integer=True)
x2 = m.Var(value=1,lb=0,ub=1000,integer=True)

# Equations
m.Equation(2 * x1 + 3 * x2 <= 800)
m.Equation(2 * x1 + x2 <= 500)

# Objective
m.Maximize((160 - (0.4 * x1)) * x1 + (135 - (0.2 * x2 )) * x2) 


m.options.IMODE = 3 # Steady state optimization

m.solve(disp=False) # Solve

print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('Objective: ' + str(m.options.objfcnval))

# Les résultats sont identiques au fichier EXCEL, sauf le profit un peu différent, surement parceque excel n'est pas paramétré en integer (entiers).
# Results
# x1: [144.0]
# x2: [170.0]
# Objective: -31915.6



