""" 
Traduction et analyse de l'article de Tirthajyoti Sarkar en Français

Minimiser le cout de production du menu d'une école, sous contraintes nutritionelles.


Note : Ce qui est bien dans cet exemple, c'est l'import EXCEL.


Minimiser ∑ Ci.fi
Sous contrainte calorieinferieure < ∑ Cal i.fi < caloriesuperieure
Sous contrainte proteineinferieure < ∑ Pro i.fi < proteinesuperieure




Source 

https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99


"""
import pandas as pd
import pulp
from pulp import *


# ON déclare le problème de minimisation.
prob = LpProblem("Simple Diet Problem",LpMinimize)

# Lire les premières lignes du fichier EXCEL
# Ne pas lire les contraintes
df = pd.read_excel("datasets/diet - medium.xls",nrows=17)

# Créer une liste des aliments
food_items = list(df['Foods'])

# Créer une dictionnaire des couts de chaque aliment
costs = dict(zip(food_items,df['Price/Serving']))

# Créer une dictionnaire des calories de chaque aliment
calories = dict(zip(food_items,df['Calories']))

# Créer une dictionnaire du gras total de chaque aliment
fat = dict(zip(food_items,df['Total_Fat (g)']))

# Créer une dictionnaire des carbohydrates de chaque aliment
carbs = dict(zip(food_items,df['Carbohydrates (g)']))

# Créer une dictionnaire des fibres de chaque aliment
fiber = dict(zip(food_items,df['Dietary_Fiber (g)']))

# On crée ensuite nos variables
food_vars = LpVariable.dicts("Food",food_items,lowBound=0,cat='Continuous')

# Fonction objectif
prob += lpSum([costs[i]*food_vars[i] for i in food_items])

# Les contraintes en calorie
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= 800.0
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) <= 1300.0

# Les contraintes spécifiques
# Gras
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 20.0, "FatMinimum"
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= 50.0, "FatMaximum"

# Carbs
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130.0, "CarbsMinimum"
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 200.0, "CarbsMaximum"

# Fibres
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 60.0, "FiberMinimum"
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 125.0, "FiberMaximum"

# Proteines
""" prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 100.0, "ProteinMinimum"
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= 150.0, "ProteinMaximum" """


prob.writeLP("problemeCantine.lp")

prob.solve()

# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chaque variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
     if v.varValue>0:
        print(v.name, "=", v.varValue)



""" 
Status: Optimal
Food_Chocolate_Chip_Cookies = 3.1941723
Food_Frozen_Broccoli = 6.981301
Food__Baked_Potatoes = 0.2059191
 """


