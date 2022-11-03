#Source :https://www.lindo.com/downloads/LINGO_text/10-Blending_of_Input_Materials.pdf

# Programme pulp créé par Estelle HULEUX
# Intérêt : On a des contraintes en pourcentages, et on sait désormais comment gérer cela.
# Pulp trouve pareil que Lindo ! Donc, le programme linéaire gère bien les pourcentages
# dans le fichier num 8 on va comparer avec un programme EXCEL et voir si on trouve pareil!

import pulp
from pulp import *

# On veut minimiser le cout de 2000 pounds d'alliage # 1 tonne signifie 2000 pounds en Angleterre.
prob = LpProblem("Production 1 tonne",LpMinimize)

# ON crée nos variables de décisions
# Ca veut dire qu'on doitchoisir quels sont les alliages les plus judicieux à choisir et on leur donne un nom à chacun
# C'est le nombre de kg de l’alliage i utilisés.
# vu que la valeur du nombre de kgs peut être décimal, on spécifie que c'est une variable de décision de type décimale en écrivant Continuous:
P1 = LpVariable("P1", lowBound = 0,cat='Continuous')
P2 = LpVariable("P2", lowBound = 0,cat='Continuous')
F1 = LpVariable("F1", lowBound = 0,cat='Continuous')
F2 = LpVariable("F2", lowBound = 0,cat='Continuous')
A1 = LpVariable("A1", lowBound = 0,cat='Continuous')
A2 = LpVariable("A2", lowBound = 0,cat='Continuous')
A3 = LpVariable("A3", lowBound = 0,cat='Continuous')
CB = LpVariable("CB", lowBound = 0,cat='Continuous')
S1 = LpVariable("S1", lowBound = 0,cat='Continuous')
S2 = LpVariable("S2", lowBound = 0,cat='Continuous')
S3 = LpVariable("S3", lowBound = 0,cat='Continuous')

# fonction objectif / min (ci * xi) ou xi est exprimé en cout par pounds et ci est exprimé en dollars
prob += 0.03 * P1 + 0.0645 * P2 + 0.065 * F1 + 0.061 * F2 + 0.1 * A1 +  0.13  *  A2  +  0.119  *  A3  +  0.08  *  CB  +  0.021  *  S1  +  0.02  *  S2  +  0.0195 * S3, "Cout total "

#! On ne peut pas utiliser plus que le STOCK de   matières premières suivantes ( voir le tableau du doc lindo)
prob += CB <= 20; 
prob += S1 <= 200; 
prob += S2 <= 200; 
prob += S3 <= 200; 

#! -------------------- Les requirements qualité -----------------------!
#! Carbon content; Ici, 60 veut dire qu'on a besoin de 3% de 2000 pounds , ça fait  60 ( voir le tableau du doc lindo)
prob += 0.04 * P1 + 0.15 * CB + 0.004 * S1 + 0.001 * S2 + 0.001 * S3 >= 60; 
prob += 0.04 * P1 + 0.15 * CB + 0.004 * S1 + 0.001 * S2 + 0.001 * S3 <= 70; 
##! Chrome content; 
prob += 0.1 * P2 + 0.2 * A2 + 0.08 * A3 >=  6; 
prob += 0.1 * P2 + 0.2 * A2 + 0.08 * A3 <=  9; 
##! Manganese content; 
prob += 0.009 * P1 + 0.045 * P2 + 0.6 * A1 + 0.09 * A2 + 0.33 * A3 + 0.009 * S1 + 0.003 * S2 + 0.003 * S3 >= 27; 
prob += 0.009 * P1 + 0.045 * P2 + 0.6 * A1 + 0.09 * A2 + 0.33 * A3 + 0.009 * S1 + 0.003 * S2 + 0.003 * S3 <= 33; 
#! Silicon content; 
prob +=0.0225 * P1 + 0.15 * P2 + 0.45 * F1 + 0.42 * F2 + 0.18 * A1 + 0.3 * A2 + 0.25 * A3 + 0.3 * CB >=  54; 
prob += 0.0225 * P1 + 0.15 * P2 + 0.45 * F1 + 0.42 * F2 + 0.18 * A1 + 0.3 * A2 + 0.25 * A3 + 0.3 * CB <=  60; 


#! Finish good requirements; 
# On doit spécifier que le total de nos variables de décisions exprimée en pounds doit être égal à 2000 POUNDS soit 1 tonne absolument, c'est donc logique, pas de pourcentages ici.
prob += P1 +  P2 +  F1 +   F2 +  A1 +  A2 +   A3 +  CB + S1 + S2 + S3 ==  2000 , "total"


prob.writeLP("monAlliage.lp")
prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients  = ", value(prob.objective))
