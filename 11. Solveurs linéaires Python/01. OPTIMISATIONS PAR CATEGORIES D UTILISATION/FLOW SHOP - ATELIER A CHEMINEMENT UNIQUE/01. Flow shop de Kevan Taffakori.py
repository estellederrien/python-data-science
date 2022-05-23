import pulp as op
import itertools as it

#Developer: @KeivanTafakkori, 14 March 2022
#https://www.supplychaindataanalytics.com/flow-shop-scheduling-with-pulp-in-python/

def model(I,J,K,p,s,dispmodel="n",solve="y", dispresult="y"):
    m    = op.LpProblem("FlowShopSchedulingProblem", op.LpMinimize)
    x    = {(i,j): op.LpVariable(f"x{i}{j}", 0,1, op.LpBinary) for i,j in it.product(I, J)}
    c    = {(j,k): op.LpVariable(f"c{j}{k}", 0, None, op.LpContinuous) for j,k in it.product(J, K)}
    maxi = {(j,k): op.LpVariable(f"maxi{j}{k}", 0, None, op.LpContinuous) for j,k in it.product(J, K)}
    objs = {0: sum(w[j]*c[(j,1)] for j in J)}
    cons = {0: {i: (sum(x[(i,j)] for j in J) == 1, f"eq0_{i}") for i in I},
            1: {j: (sum(x[(i,j)] for i in I) == 1, f"eq1_{j}") for j in K},
            2: {j: (c[(j,1)] >= sum(x[(i,j)]*p[1][i] for i in I) + maxi[(j,1)], f"eq2_{j}") for j in J if j!=0},
            3: {0: (c[(0,1)] == s[1] + sum(x[(i,0)]*p[1][i] for i in I) + c[(0,0)], "eq3_")},
            4: {j: (c[(j,0)] >= c[(j-1,0)] + sum(x[(i,j)]*p[0][i] for i in I), f"eq4_{j}") for j in J if j!=0},
            5: {0: (c[(0,0)] == s[0] + sum(x[(i,0)]*p[0][i] for i in I), "eq5_")},
            6: {j: (maxi[(j,1)] >= c[(j-1,1)], f"eq6_{j}") for j in J if j!=0},
            7: {j: (maxi[(j,1)] >= c[(j,0)], f"eq7_{j}") for j in J}}
    m += objs[0]
    for keys1 in cons: 
        for keys2 in cons[keys1]: m += cons[keys1][keys2]
        if dispmodel=="y":
            print("Model --- \n",m)
        if solve == "y":
            result = m.solve(op.PULP_CBC_CMD(timeLimit=None))
            print("Status --- \n", op.LpStatus[result])
            if dispresult == "y" and op.LpStatus[result] =='Optimal':
                print("Objective --- \n", op.value(m.objective))
                print("Decision --- \n", [(variables.name,variables.varValue) for variables in m.variables() if variables.varValue!=0])
    return m, c, x

w = [0.1, 0.4, 0.15, 0.35] #Priority weight of each job
p = [[  7,   3,    9,    4],
     [  7,   3,    9,    4]] #Processing time of each job on each machine
s = [5, 2] #Setup times of the machines
I = range(len(p[0])) #Set of jobs
J = range(len(I)) #Set of positions
K = range(len(p)) #Set of machines


m, c, x = model(I,J,K,p,s) #Model and solve the problem