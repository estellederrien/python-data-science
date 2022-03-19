

'''
Lien : https://blog.sommer-forst.de/2013/04/06/solving-the-minimum-cost-flow-problem-4-pulp/


Minimum Cost Flow Problem Solver with PuLP
Adapted from:
https://code.google.com/p/pulp-or/wiki/ATransshipmentProblem
The American Steel Problem for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell   2007
 
'''
 
# Import PuLP modeller functions
from pulp import *
 
# list of nodes
nodes = [1,2,3,4]
 
# supply or demand of nodes
            #NodeID : [Supply,Demand]
nodeData = {1:[4,0],
            2:[0,0],
            3:[0,0],
            4:[0,4]}
 
# arcs list
arcs = [ (1,2),
         (1,3),
         (2,3),
         (2,4),
         (3,4)]
 
# arcs cost, lower bound and capacity
            #Arc : [Cost,MinFlow,MaxFlow]
arcData = { (1,2):[2,0,4],
            (1,3):[2,0,2],
            (2,3):[1,0,2],
            (2,4):[3,0,3],
            (3,4):[1,0,5] }
 
# Splits the dictionaries to be more understandable
(supply, demand) = splitDict(nodeData)
(costs, mins, maxs) = splitDict(arcData)
 
# Creates the boundless Variables as Integers
vars = LpVariable.dicts("Route",arcs,None,None,LpInteger)
 
# Creates the upper and lower bounds on the variables
for a in arcs:
    vars[a].bounds(mins[a], maxs[a])
 
# Creates the 'prob' variable to contain the problem data    
prob = LpProblem("Minimum Cost Flow Problem Sample",LpMinimize)
 
# Creates the objective function
prob += lpSum([vars[a]* costs[a] for a in arcs]), "Total Cost of Transport"
 
# Creates all problem constraints - this ensures the amount going into each node is 
# at least equal to the amount leaving
for n in nodes:
    prob += (supply[n]+ lpSum([vars[(i,j)] for (i,j) in arcs if j == n]) >=
             demand[n]+ lpSum([vars[(i,j)] for (i,j) in arcs if i == n])), \
            "Flow Conservation in Node %s"%n
 
# The problem data is written to an .lp file
prob.writeLP("simple_MCFP.lp")
 
# The problem is solved using PuLP's choice of Solver
prob.solve()
 
# The optimised objective function value is printed to the screen    
print "Total Cost of Transportation = ", value(prob.objective)