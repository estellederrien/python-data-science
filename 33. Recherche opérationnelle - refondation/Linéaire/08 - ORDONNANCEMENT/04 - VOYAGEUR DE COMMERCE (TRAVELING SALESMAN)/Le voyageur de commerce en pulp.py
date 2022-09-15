import pulp as op
import numpy as np
import itertools as it

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Combinatorial-Optimization-in-Python
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Combinatorial-Optimization-in-Python
#============================================================================#

def model(N,U,c,dispmodel="y",solve="y", dispresult="y"):
    m = op.LpProblem("TravelingSalesmanProblem", op.LpMinimize)
    x = {(i,j): op.LpVariable(f"x{i}{j}", 0,1, op.LpBinary) for i,j in it.product(N,N)}
    u = {i: op.LpVariable(f"u{i}", 0,len(N)-1, op.LpInteger) for i in N}
    objs = {0: sum(c[i][j]*x[(i,j)]  for i,j in it.product(N,N))}
    cons = {0: {j: (sum(x[(i,j)] for i in N if i!=j ) == 1, f"eq1_{j}") for j in N},
            1: {i: (sum(x[(i,j)] for j in N if j!=i ) == 1, f"eq2_{i}") for i in N},
            2: {(i,j): (u[i] - u[j] + x[(i,j)] * len(N) <= len(N)-1 , f"eq3_{i}{j}") for i,j in it.product(U,N) if i!=j}}
    m += objs[0]
    for keys1 in cons:
        for keys2 in cons[keys1]: m += cons[keys1][keys2]
    if dispmodel == "y":
        print("Model --- \n",m)
    if solve == "y":
        result = m.solve(op.PULP_CBC_CMD(timeLimit=None))
        print(op.LpStatus[result])
    if dispresult=="y" and  op.LpStatus[result] =='Optimal':
        print("Objective --- \n", op.value(m.objective))
        print("Decision --- \n", [(variables.name,variables.varValue) for variables in m.variables() if variables.varValue!=0])
        print("Slack --- \n", [(name,constraint.slack) for name, constraint in m.constraints.items() if constraint.slack!=0])
    return m

np.random.seed(0) #Fixing the seed for random number generator

N = range(5) #Set of cities (nodes)
U = range(1,len(N)) #Set of dummy variables for sub-tour elimination constraint
c = np.random.randint(1,10, size=(len(N),len(N))) 
for (i,j) in it.product(N,N):
    c[i][i]=0                           #Cost (distance) matrix 
    c[i][j]=c[j][i]
    
m = model(N,U,c) #Model and solve the problem