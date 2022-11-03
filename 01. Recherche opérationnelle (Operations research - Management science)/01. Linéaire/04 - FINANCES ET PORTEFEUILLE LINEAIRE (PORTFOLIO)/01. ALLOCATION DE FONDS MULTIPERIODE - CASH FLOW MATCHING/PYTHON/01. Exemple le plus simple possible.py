# Source : https://coral.ise.lehigh.edu/~ted/files/ie447/lectures/Lecture3.pdf


""" 
L'histoire : 

Un gestionnaire de portefeuille  dispose de 100 000 Euros à allouer à deux actions différentes.

actions rendement Maturité Evaluation
A           4           3       A (2)
B           3           4       Aaa (1)

• L'objectif est de maximiser le rendement total sous réserve des limites suivantes:
- La note moyenne doit être au maximum de 1,5 (la plus basse est la meilleure).
- La maturité moyenne doit être au maximum de 3,6 ans.
- Tout argent non investi sera conservé dans un compte ne portant pas intérêt et
   est supposé avoir une note implicite de 0 (pas de risque). 
   
   """

from pulp import LpProblem, LpVariable, lpSum, LpMaximize, value

bonds = {"A": {"yield": 4,
               "rating": 2,
               "maturity": 3, },
         "B": {"yield": 3,
               "rating": 1,
               "maturity": 4, },
         }
max_cash = 100
max_rating = 1.5
max_maturity = 3.6


prob = LpProblem("Dedication Model", LpMaximize)

buy = LpVariable.dicts("bonds", bonds, 0, None)

for f in features:
    if sense[f] == "Max":
        prob += lpSum(bond_data[b, f] * buy[b] for b in bonds)
    elif sense[f] == "Max":
        prob += lpSum(-bond_data[b, f] * buy[b] for b in bonds)
    elif sense[f] == ">":
        prob += (lpSum(bond_data[b, f] * buy[b] for b in bonds) >= max_cash*limits[f], f)
    else:
        prob += (lpSum(bond_data[b, f] * buy[b] for b in bonds) <= max_cash*limits[f], f)
        prob += lpSum(buy[b] for b in bonds) <= max_cash, "cash"

#status = prob.solve()
prob.solve()
print("Optimal total cost is: ", value(prob.objective))
print("X1 :", X1.varValue)
print("X2 :", X2.varValue)
