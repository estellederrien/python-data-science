"""
Une raffinerie produit 3 sortes d'essence  A, B et C .

"""

# Minimiser le cout d'alliages de métaux .
# Caractéristiques de l'acier à faire	

""" 
Fournisseur
Constituant 	Disponibilité Prix au baril	
1          	       20000 	        80	
2	               40000	        90 	
3       	       30000 	        100 
 """
# 3 Types d'essence Que notre usine produit
""" 
Essence     Composition             Prix/Baril
A           Au moins de 30% de 1        130
            Pas plus de 50% de 2
            Au moins de 20% de 3
B           Pas plus de 40% de 1        150
B           Pas moins de 20% de 2
C           Pas plus de 60% de 1        140 
          
"""
# Importer la lib PuLP 
from pulp import *

#Créer la variable du problème
prob = LpProblem("MaximiserProfit",LpMaximize)

# Les 7 vars ont une limite en zéro
x1A = LpVariable("NbBarilsConstituant1EssenceA",lowBound = 0)
x1B = LpVariable("NbBarilsConstituant1EssenceB",lowBound = 0)
x1C = LpVariable("NbBarilsConstituant1EssenceC",lowBound = 0)
x2A = LpVariable("NbBarilsConstituant2EssenceA",lowBound = 0)
x2B = LpVariable("NbBarilsConstituant2EssenceB",lowBound = 0)
x2C = LpVariable("NbBarilsConstituant2EssenceC",lowBound = 0)
x3A = LpVariable("NbBarilsConstituant3EssenceA",lowBound = 0)
x3B = LpVariable("NbBarilsConstituant3EssenceB",lowBound = 0)
x3C = LpVariable("NbBarilsConstituant3EssenceC",lowBound = 0)

# La fonction objectif est de maximiser le profit

# prob += 130(x1A +  x2A + x3A) + 150(x1B +  x2B + x3B) + 140(x1C +  x2C + x3C) - 80(x1A +  x1B + x1C) - 90(x2A +  x2B + x2C) - 100(x3A +  x3B + x3C) , "Profit"

prob += 50 * x1A + 40 * x2A + 30 * x3A + 70 * x1B + 60 * x2B + 50 * x3B + 60 * x1C + 50 * x2C + 40 * x3C  , "Profit"

# Contraintes
prob += x1A + x1B + x1C <= 20000, "disponibilite1"
prob += x2A + x2B + x2C <= 40000, "disponibilite2"
prob += x3A + x3B + x3C <= 30000, "disponibilite3"

prob += -0.7 * x1A + 0.3 * x2A + 0.3 * x3A  <= 0, "compositionA1"
prob += -0.5 * x1A + 0.5 * x2A - 0.5 * x3A  <= 0, "compositionA2"
prob += 0.2  * x1A + 0.2 * x2A - 0.8 * x3A  <= 0, "compositionA3"
prob += 0.6 *  x1B - 0.4 * x2B - 0.4 * x3B  <= 0, "compositionB1"
prob += 0.2 *  x1B - 0.8 * x2B + 0.2 * x3B  <= 0, "compositionB2"
prob += 0.4 *  x1C - 0.6 * x2C + 0.6 * x3C  <= 0, "compositionC"

prob += x1A >= 0
prob += x1B >= 0
prob += x1C >= 0
prob += x2A >= 0
prob += x2B >= 0
prob += x2C >= 0
prob += x3A >= 0
prob += x3B >= 0
prob += x3C >= 0

# The problem data is written to an .lp file
prob.writeLP("melange.lp")

# On utilise le solveur
prob.solve()

# Le statut de la solution
print ("Status:", LpStatus[prob.status])

# On loupe et affiche les optimums de chaque var
for v in prob.variables():
    print (v.name, "=", v.varValue)
    
# Le resultat de la function objectif est ici
print ("Total", value(prob.objective))
