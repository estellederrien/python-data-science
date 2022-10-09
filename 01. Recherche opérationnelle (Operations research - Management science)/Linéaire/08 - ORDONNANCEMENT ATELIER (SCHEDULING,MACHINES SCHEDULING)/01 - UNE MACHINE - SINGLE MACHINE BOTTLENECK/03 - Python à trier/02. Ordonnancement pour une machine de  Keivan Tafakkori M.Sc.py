## Source : https://www.supplychaindataanalytics.com/single-machine-scheduling-with-pulp-in-python/
# Copyright :  Keivan Tafakkori M.Sc.

import pulp as op
import itertools as it

#Developer: @KeivanTafakkori, 8 March 2022

def model(I,J,p,s,dispmodel="y",solve="y", dispresult="y"):
    m = op.LpProblem("SingleMachineSchedulingProblem", op.LpMinimize)
    x = {(i,j): op.LpVariable(f"x{i}{j}", 0,1, op.LpBinary) for i,j in it.product(I, J)}
    c = {j: op.LpVariable(f"c{j}", 0, None, op.LpContinuous) for j in J}
    objs = {0: sum(w[j]*c[j] for j in J)} 
    cons = {0: {i: (sum(x[(i,j)] for j in J) == 1, f"eq1_{i}") for i in I},
            1: {j: (sum(x[(i,j)] for i in I) == 1, f"eq2_{j}") for j in J},
            2: {j: (c[j] >= c[j-1] + sum(x[(i,j)]*p[i] for i in I), f"eq3_{j}") for j in J if j!=0},
            3: {0: (c[0] == s + sum(x[(i,0)]*p[i] for i in I), "eq4_")}}
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
p = [  7,   3,    9,    4] #Processing time of each job
s = 5 #Setup time of the machine
I = range(len(p)) #Set of jobs
J = range(len(I)) #Set of positions

m, c, x = model(I,J,p,s) #Model and solve the problem

# DATA VIZ
seq = []
for j in J:
    for i in I:
        if x[(i,j)].varValue==1:
            seq.append(i+1)
print(seq)

import matplotlib.pyplot as plt
import numpy as np

fig, gnt = plt.subplots()
gnt.set_xlabel('Minutes since start')
gnt.set_ylabel('Machine')
gnt.set_xlim(0, c[len(J)-1].varValue)
gnt.set_ylim(0, 50)
gnt.set_yticks([15, 25, 35])
gnt.set_yticklabels(['', '1', ''])
gnt.grid(True,color='k',linestyle='-.', alpha=0.2)

process = [(c[j-1].varValue,c[j].varValue) for j in J if j!=0] 
process.insert(0, (0,s))
process.insert(1, (s,c[0].varValue))

np.random.seed(3)
l = []
for j in J:
    l.append(tuple(np.random.choice(range(0, 2), size=3)))
     
gnt.broken_barh(process, (20, 9),color=l)
for j in J:
    if j!=0:
        for i in I:
            if x[(i,j-1)].varValue==1:
                gnt.annotate(f"J{i+1}", (process[j][0],15))
    else:
        gnt.annotate("Setup", (0,15))

for i in I:
    if x[(i,len(J)-1)].varValue==1:
        gnt.annotate(f"J{i+1}", (process[len(J)][0],15))
        
gnt.annotate(["TWCT",sum(w[j]*c[j].varValue for j in J)], ((c[len(J)-1].varValue-s)/2,10))
plt.savefig("gantt1.png")