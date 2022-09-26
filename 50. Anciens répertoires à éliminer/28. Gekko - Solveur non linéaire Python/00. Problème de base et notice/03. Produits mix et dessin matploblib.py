# https://stackoverflow.com/questions/73409787/gekko-and-pulp-results-differs-but-both-are-valid-why
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
m.Maximize( 2 * x1 + 1 * x2) 
# m.Obj((160 - 0,4 * x1) * x1 + (135 - 0,2 * x2 ) * x2) 

m.options.IMODE = 3 # Steady state optimization

m.solve(disp=False) # Solve

print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('Objective: ' + str(m.options.objfcnval))




# There are an infinite number of potential solutions because the profit objective and constraint 2 are co-linear so the objective contour is along constraint 2.

# m.Equation(2*x1 + 1*x2 <= 500)
# m.Maximize(2*x1 + 1*x2)

# contour

# This is apparent with a contour plot that shows the constraints (blue and red) and objective contours (green). The optimal solutions are along the blue line constraint (#2) until it intersects with the red line constraint (#1).

# Generate a contour plot

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Design variables at mesh points
x = np.arange(-1.0, 401, 5)
y = np.arange(-1.0, 501, 5)
x1, x2 = np.meshgrid(x,y)

# Equations and Constraints
profit = 2.0 * x1 + 1.0 * x2
c1 = 2.0 * x1 + 3.0 * x2
c2 = 2.0 * x1 + 1.0 * x2

# Create a contour plot
plt.figure()
# Profit contours
lines = np.linspace(100.0,800.0,4)
CS = plt.contour(x1,x2,profit,lines,colors='g')
plt.clabel(CS, inline=1, fontsize=10)
# Car 1 <= 800
CS = plt.contour(x1,x2,c1,[760.0, 780.0, 800.0],colors='r',linewidths=[0.5,0.5,4.0])
plt.clabel(CS, inline=1, fontsize=10)
# Car 2 < 500
CS = plt.contour(x1, x2,c2,[460.0,480.0,500.0],colors='b',linewidths=[0.5,0.5,4.0])
plt.clabel(CS, inline=1, fontsize=10)
# 0 <= Car 1 <= 1000
CS = plt.contour(x1, x2,x1 ,[0.0, 5.0, 10.0],colors='k',linewidths=[1.0,0.5,0.5])
plt.clabel(CS, inline=1, fontsize=10)
# 0 <= Car 2 <= 100
CS = plt.contour(x1, x2,x2 ,[0.0, 5.0, 10.0],colors='k',linewidths=[4.0,0.5,0.5])
plt.clabel(CS, inline=1, fontsize=10)
plt.xlabel('Car 1 Units'); plt.ylabel('Car 2 Units'); plt.show()
