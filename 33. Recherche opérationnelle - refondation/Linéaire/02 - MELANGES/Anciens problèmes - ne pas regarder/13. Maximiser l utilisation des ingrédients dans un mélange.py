""" 
Traduction et analyse de l'article de Ram Narasimhan en Français
Note : Seulement traduit et stocké, résultat et code à vérifier .


Ici, on ne veut pas maximiser notre gain en euros, mais
maximiser l'utilisation des ingrédients dans un mélange, 
à l'aide de la function économique.



Source :
https://stackoverflow.com/questions/51438018/pulp-objective-function-adding-multiple-lpsum-in-a-loop

"""
import pandas as pd
import pulp
from pulp import *


ELEMENTS = ['Iron', 'Mercury', 'Silver']


Max_Per_Elem = {'Iron': 35, 
         'Mercury': 17, 
         'Silver': 28
               }

# A dictionary of the Iron percent in each of the CONCs
IronPercent = {'CONC_1': 20, 'CONC_2': 10, 'CONC_3': 25}

# A dictionary of the Hg percent in each of the CONCs
MercPercent = {'CONC_1': 15, 'CONC_2': 18, 'CONC_3': 12}

# A dictionary of the Silver percent in each of the CONCs
SilverPercent = {'CONC_1': 30,  'CONC_2': 40, 'CONC_3': 20}

CONCENTRATE_DIC = {'Iron': IronPercent,
              'Mercury': MercPercent,
              'Silver': SilverPercent              
              }

# Creates a list of Decision Variables
concs = ['CONC_1', 'CONC_2', 'CONC_3']


# Maintenant, nous sommes prêts à appeler les fonctions puLP.

conc_vars = LpVariable.dicts("Util", concs, 0, 1.0)

# On spécifie que l'on veut maximiser la fonction économique.
prob = LpProblem("Elements Concentration Problem", LpMaximize)

# La fonction objectif.
prob += lpSum([conc_vars[i] for i in concs]), "Total Utilization is maximized"

for elem in ELEMENTS:
    prob += lpSum([CONCENTRATE_DIC[elem][i]/Max_Per_Elem[elem] * conc_vars[i] for i in concs]) <= Max_Per_Elem[elem]/100, elem+"Percent"

# Pour vérifier, vous pouvez imprimer le problème pour voir à quoi il ressemble:

""" Elements Concentration Problem:
MAXIMIZE
1*Util_CONC_1 + 1*Util_CONC_2 + 1*Util_CONC_3 + 0
SUBJECT TO
IronPercent: 0.571428571429 Util_CONC_1 + 0.285714285714 Util_CONC_2
 + 0.714285714286 Util_CONC_3 <= 0.35

MercuryPercent: 0.882352941176 Util_CONC_1 + 1.05882352941 Util_CONC_2
 + 0.705882352941 Util_CONC_3 <= 0.17

SilverPercent: 1.07142857143 Util_CONC_1 + 1.42857142857 Util_CONC_2
 + 0.714285714286 Util_CONC_3 <= 0.28

VARIABLES
Util_CONC_1 <= 1 Continuous
Util_CONC_2 <= 1 Continuous
Util_CONC_3 <= 1 Continuous """

# Une fois que vous êtes satisfait de la formulation, résolvez le problème.

prob.writeLP("ElemUtiliztionModel.lp")
prob.solve()

print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)


""" Status: Optimal
Util_CONC_1 = 0.0
Util_CONC_2 = 0.0
Util_CONC_3 = 0.24083333 """