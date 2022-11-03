http://www.inf.ufrgs.br/~svravelo/assets/slides/PLI_14.pdf
1 from pulp import *
2
3 def multipleKnapsack(values, weights, W):
4 x = LpVariable.dicts("x", [(o, i) for o in range(len(values)) for i in range(len(W))],
lowBound = 0, upBound = 1, cat='Integer')↪
5
6 problem = LpProblem("MultipleKnapsack", LpMaximize)
7
8 problem += lpSum(values[o] * x[o, i] for o in range(len(values)) for i in range(len(W))),
"profit"↪
9
10 for i in range(len(W)):
11 problem += lpSum(weights[o] * x[o, i] for o in range(len(values))) <= W[i]
12
13 for o in range(len(W)):
14 problem += lpSum(x[o, i] for i in range(len(W))) <= 1