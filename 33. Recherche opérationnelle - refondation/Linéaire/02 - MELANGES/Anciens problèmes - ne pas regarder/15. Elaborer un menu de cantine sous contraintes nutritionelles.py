""" 
Traduction et analyse de l'article de Tirthajyoti Sarkar en Français

Minimiser le cout de production du menu d'une école, sous contraintes nutritionelles.


Phase 2 : Analyse et tests du script + passage en français complet.

Tentative d'ajouter au moins 2 légumes en min, avec sa méthode .

Source 

https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99


"""
import pandas as pd
import pulp
from pulp import *

print ('je suis bien le bon2 ')
# ON déclare le problème de minimisation.
prob = LpProblem("Je minimise",LpMinimize)

# Lire les premières lignes du fichier EXCEL
# Ne pas lire les contraintes
df = pd.read_excel("datasets/mon-menu-de-cantine.xls",nrows=17)

# Créer une liste des aliments
aliments = list(df['Aliments'])

# Créer un dictionnaire des couts de chaque aliment
costs = dict(zip(aliments,df['Prix/Unitaire']))

# Créer une dictionnaire des calories de chaque aliment
calories = dict(zip(aliments,df['Calories']))

# Créer une dictionnaire du gras total de chaque aliment
gras = dict(zip(aliments,df['Gras (g)']))

# Créer un dictionnaire des carbohydrates de chaque aliment
carbohydrates = dict(zip(aliments,df['Carbohydrates (g)']))

# Créer un dictionnaire des fibres de chaque aliment
fibres = dict(zip(aliments,df['Fibres (g)']))

# Créer un dictionnaire des protéines de chaque aliment
proteines = dict(zip(aliments,df['Proteines (g)']))

# Créer un dictionnaire bool si cest un légume ou pas
legumes = dict(zip(aliments,df['Legume (bool)']))


# On crée ensuite nos variables
aliments_vars = LpVariable.dicts("aliment",aliments,lowBound=0,cat='Integer')

legumes_vars = LpVariable.dicts("Legume (bool)",aliments,0,1,cat='Integer')


# Fonction objectif : Minimiser le cout du repas.
prob += lpSum([costs[i]*aliments_vars[i] for i in aliments])

# legumes bool

# On ajoute une contrainte pour quil y ait au moins 3 légumes :
# prob += lpSum([legumes[f] * aliments_vars[f] for f in aliments]) >= 3, "legumesMinimum"

# for p in aliments:
#   prob += aliments_vars[p] <= legumes[p], f"min legumes  {p}"


# Les contraintes en calorie
prob += lpSum([calories[f] * aliments_vars[f] for f in aliments]) >= 800.0
prob += lpSum([calories[f] * aliments_vars[f] for f in aliments]) <= 2500.0

# Les contraintes spécifiques
# Gras
prob += lpSum([gras[f] * aliments_vars[f] for f in aliments]) >= 60.0, "grasMinimum"
prob += lpSum([gras[f] * aliments_vars[f] for f in aliments]) <= 80.0, "grasMaximum"

# carbohydrates
prob += lpSum([carbohydrates[f] * aliments_vars[f] for f in aliments]) >= 130.0, "carbohydratesMinimum"
prob += lpSum([carbohydrates[f] * aliments_vars[f] for f in aliments]) <= 200.0, "carbohydratesMaximum"

# Fibres
prob += lpSum([fibres[f] * aliments_vars[f] for f in aliments]) >= 120.0, "fibresMinimum"
prob += lpSum([fibres[f] * aliments_vars[f] for f in aliments]) <= 150.0, "fibresMaximum"

# proteines
prob += lpSum([proteines[f] * aliments_vars[f] for f in aliments]) >= 80.0, "proteinesMinimum"
prob += lpSum([proteines[f] * aliments_vars[f] for f in aliments]) <= 150.0, "proteinesMaximum"

#legumes

for f in aliments:
    prob += aliments_vars[f] >= legumes_vars[f]*0.1
    prob += aliments_vars[f] <= legumes_vars[f]*1e5

prob += legumes_vars['Mais']+legumes_vars['Haricots'] >= 2

prob.writeLP("problemeCantine.lp")

prob.solve()

# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chaque variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
     if v.varValue>0:
        print(v.name, "=", v.varValue)

# On affiche le prix du repas
obj = value(prob.objective)
print("Le cout total de ce repas est de : Euros{}".format(round(obj,2)))



""" 
Status: Infeasible
Legume_(bool)_Broccolis = 0.00014056471
Legume_(bool)_Bœuf = 3.7420065e-05
Legume_(bool)_Haricots = 1.0
Legume_(bool)_Mais = 1.0
Legume_(bool)_Œufs_pochés = 1.0645752e-06
aliment_Broccolis = 14.056471
aliment_Bœuf = 3.7420065
aliment_Haricots = 0.1
aliment_Mais = 0.1
aliment_Œufs_pochés = 0.10645752
Le cout total de ce repas est de : Euros9.84
 """


