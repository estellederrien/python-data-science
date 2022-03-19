"""
Programmation linéaire avec EXCEL
Page 97

Mining and metals

We make steel with raw materials, we want to reduce the cost of producing this steel
to make more money, but still respecting the minimum characteristics of quality steel


*** ESSAI 2 : ***

Vu que le résultat ne correspond pas au résultat du livre et du solveur excel, 
Je simplifie en commançant par minimiser le prix de seulement 1kg d'acier .
Je ne tiens donc pas, pour l'instant, compte des stocks.

1. Elimination de la contrainte de production minimale de 5000 kgs.
2. On convertit tout les pourcentages par des valeurs en kgs On enlève les % .
3. Minimisation du prix de 1kg d'acier.


"""

# Minimize the cost of metal alloys.
# Characteristics of the steel to be made

"""Element      kgMinimum       kgMax   
   Carbon       0.020           0.030     
   Copper       0.004           0.006   
   Manganese    0.012           0.0165  

"""

# Characteristics, stocks and purchase price of alloys
"""
Alloy          C kg     Cu kg   Mn kg    Stocks kg Price € / kg
Iron alloy     0.025    0.000   0.013    4000      1.20
Iron alloy     0.030    0.000   0.008    3000      1.50
Iron alloy     0.000    0.003   0.000    6000      0.90
Copper alloy   0.000    0.900   0.000    5000      1.30
Copper alloy   0.000    0.960   0.040    2000      1.45
Aluminum alloy 0.000    0.004   0.012    3000      1.20
Aluminum alloy 0.000    0.006   0.000    2500      1.00
"""

# Import the PuLP lib
from pulp import *

# Create the problem variable
prob = LpProblem ("MinimiserLpAlliage", LpMinimize)

# Problem Data
input_mats = ["iron_1", "iron_2", "iron_3",
              "cu_1", "cu_2",
              "al_1", "al_2"]

input_costs = {"iron_1": 1.20, "iron_2": 1.50, "iron_3": 0.90,
               "cu_1":   1.30, "cu_2": 1.45,
               "al_1":   1.20, "al_2":   1.00}

#                               C%   Cu%   Mn%
input_composition = {"iron_1": [0.025,0.000,0.013],
                     "iron_2": [0.030,0.000,0.008],
                     "iron_3": [0.000,0.003,0.000],
                     "cu_1":   [0.000,0.900,0.000],
                     "cu_2":   [0.000,0.960,0.040],
                     "al_1":   [0.000,0.004,0.012],
                     "al_2":   [0.000,0.006,0.000]}

input_stock = {"iron_1": 4000, "iron_2": 3000, "iron_3": 6000,
               "cu_1": 5000, "cu_2":  2000,
               "al_1": 3000, "al_2": 2500}

# request_quantity = 5000

# Problem variables - amount in kg of each input
x = LpVariable.dicts("input_mat", input_mats, 0)

# The objective function is to minimize the total cost of the alloys in EUROS for a given quantity in KGS
prob += lpSum([input_costs[i]*x[i] for i in input_mats]), "AlliageCost"

# Quantity constraint in KGS.
# prob += lpSum([x[i] for i in input_mats]) == 5000, "RequestedQuantity"

# La production totale est de 1 kg
prob += lpSum([x[i] for i in input_mats]) == 1,"conservation"

# MIN/MAX constraint of carbon in resultant steel
prob += lpSum([x[i]*input_composition[i][0] for i in input_mats]) >= 0.020, "MinCarbon"
prob += lpSum([x[i]*input_composition[i][0] for i in input_mats]) <= 0.030, "MaxCarbon"

# MIN/MAX constraints of copper in resultant steel
prob += lpSum([x[i]*input_composition[i][1] for i in input_mats]) >= 0.004, "MinCu"
prob += lpSum([x[i]*input_composition[i][1] for i in input_mats]) <= 0.006, "MaxCu"

# MIN/MAX constraints of manganese in resultant steel
prob += lpSum([x[i]*input_composition[i][2] for i in input_mats]) >= 0.0120, "MinMn"
prob += lpSum([x[i]*input_composition[i][2] for i in input_mats]) <= 0.0165, "MaxMn"


# MAX constraints of available stock
# for i in input_mats:
#     prob += x[i] <= input_stock[i], ("MaxStock_" + i)


# The problem data is written to an .lp file
prob.writeLP ( "SteelModel.lp")

# We use the solver
prob.solve()

# The status of the solution
print ("Status:", LpStatus [prob.status])

# Dislay the optimums of each var
for v in prob.variables ():
    print (v.name, "=", v.varValue)

# Display mat'l compositions
""" Carbon_value = 100*(sum([x[i].varValue*input_composition[i][0] for i in input_mats])/request_quantity)
Cu_value = 100*(sum([x[i].varValue*input_composition[i][1] for i in input_mats])/request_quantity)
Mn_value = 100*(sum([x[i].varValue*input_composition[i][2] for i in input_mats])/request_quantity) """
""" 
print ("Carbon content: " + str(Carbon_value))
print ("Copper content: " + str(Cu_value))
print ("Manganese content: " + str(Mn_value)) """

# The result of the objective function is here
print ("Total en euros pour 1kg d'acier", value (prob.objective), "EUROS")



""" Status: Optimal
input_mat_al_1 = 0.0
input_mat_al_2 = 0.0
input_mat_cu_1 = 0.0
input_mat_cu_2 = 0.0059708622
input_mat_iron_1 = 0.90470504
input_mat_iron_2 = 0.0
input_mat_iron_3 = 0.089324098
Total en euros 1.1746954863899999 EUROS """