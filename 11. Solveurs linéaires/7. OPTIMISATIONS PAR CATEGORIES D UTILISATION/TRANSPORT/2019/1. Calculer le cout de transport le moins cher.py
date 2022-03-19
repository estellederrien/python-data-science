# https://www.coin-or.org/PuLP/CaseStudies/a_transportation_problem.html
# https://stackoverflow.com/questions/49218316/transport-optimization-pulp
# 2 Fournisseurs A et B fournissent 1000 et 4000 unités
# 5 Bars recquierent 500,900,1800,200,700 unités

# Cout du transport par chemion des fournisseurs aux bars 
# 							A 	B
# 1 						2 	3
# 2 						4 	1
# 3 						5 	3
# 4 						2 	2
# 5 						1 	3


# Minimiser le cout de transport

# Constraints :

    # A1 + A2 + A3 + A4 + A5 <= 1000
    # B1 + B2 + B3 + B4 + B5 <= 4000
	
	
    # A1 + B1 >= 500
    # A2 + B2 >= 900
    # A3 + B3 >= 1800
    # A4 + B4 >= 200
    # A5 + B5 >= 700

"""
The Beer Distribution Problem for the PuLP Modeller

Authors: Antony Phillips, Dr Stuart Mitchell    2007
"""

# Import PuLP modeller functions
from pulp import *

# Liste des fournisseurs
Warehouses = ["A","B"]

# Créer un dictionnaire de Nombre d'unités fournies par les fournisseurs
supply = {"A": 1000,"B": 4000}

# Créer une liste des bars qui ont une demande en livraison d'unités
Bars = ["1", "2", "3", "4", "5"]

# Créer un dictionnaire de la demande des bars
demand = {"1": 500,"2": 900,"3": 1800,"4": 200,"5": 700}


# Créer une liste des couts de chaque chemins
costs = { "A" : {"1" : 2, "2" : 4, "3" : 5, "4" : 2, "5" : 1 },
          "B" : {"1" : 3, "2" : 1, "3" : 3, "4" : 2, "5" : 3 }}


# Creates the prob variable to contain the problem data
prob = LpProblem("Problème de Distribution de bière ",LpMinimize)

# Créer un liste de tuples  qui contiennent toutes les routes possibles.
Routes = [(w,b) for w in Warehouses for b in Bars]

# A dictionary called route_vars is created to contain the referenced variables (the routes)
route_vars = LpVariable.dicts("Route",(Warehouses,Bars),0,None,LpInteger)

# The objective function is added to prob first
prob += lpSum([route_vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum of Transporting Costs"

# The supply maximum constraints are added to prob for each supply node (warehouse)
for w in Warehouses:
	prob += lpSum([route_vars[w][b] for b in Bars]) <= supply[w], "Sum of Products out of Warehouse %s"%w

# The demand minimum constraints are added to prob for each demand node (bar)
for b in Bars:
	prob += lpSum([route_vars[w][b] for w in Warehouses]) >= demand[b], "Sum of Products into Bars %s"%b


prob.writeLP("TranportModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Le status de la solution s'affiche à l'écran
print ("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print (v.name, "=", v.varValue)
	
# The optimised objective function value is printed to the screen
print ("Cout total = ", value(prob.objective))	