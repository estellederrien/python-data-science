"""
Problème linéaire de Raffinerie 6

Expérimental (non corrigé- non confirmé)

"""

# Création de Fuel .

# HISTOIRE :
# On veut créer 100 litres d'essence, en mélangeant 3 bruts différents ayant des caractéristiques différentes .
#On veut payer le moins cher possible les 100 litres d'essence, tout en respectant les contraintes de production et de commande .


# CARACTERISTIQUES DE 1 LITRE DE BRUT 
# Elément 	Benzène         Plomb	   
# brut1  	0.02 litres	    0.08 litres             
# brut2 	0.05 litres	    0.06 litres        
# brut3 	0.03 litres	    0.01 litres  

# Le prix du brut1  est de 1.025 euros par litres
# Le prix du brut2  est de 1.085 euros par litres, il est plus cher
# Le prix du brut2  est de 1.075 euros par litres

#  100 litres d'essence créés doivent contenir au moins 1,1 l de bunzène (soit 1,1%)
#  100 litres d'essence créés doivent contenir moins de 3,5 l de Plomb (soit 3,5%)

# Importer la lib PuLP 
from pulp import *

#Créer la variable du problème
prob = LpProblem("lp",LpMinimize)

# Les 3 vars ont une limite en zéro , ce sont des unités de litres
x1=LpVariable("brut1Enlitres",lowBound = 0, cat='Continuous')
x2=LpVariable("brut2Enlitres",lowBound = 0, cat='Continuous')
x3=LpVariable("brut3Enlitres",lowBound = 0, cat='Continuous')

# La fonction objectif est de minimiser le prix en EUROS 
prob += 1.025*x1 + 1.085*x2 + 1.075*x3  , "Cout"

# contraintes en LITRES

# On veut commander 100 litres
prob += x1 + x2 + x3 == 100, "Litres"

# Sur ces 100 litres, un minimum de 1.1 litres de benzène, et un maximum de 3.5 litres de plombs , ce sont des contraintes qualité
prob += 0.02 * x1  + 0.05 * x2 + 0.03 * x3  >= 1.1, "benzeneMin"
prob += 0.08 * x1  + 0.06 * x2 + 0.01 * x3  <= 3.5, "PlombMax"

# ON doit commander au minimum 10 litres aux fournisseurs , ce sont des contraintes de commande
prob += x1  >= 10, "commandex1MinimaleEnLitres"
prob += x2  >= 10, "commandex2MinimaleEnLitres"
prob += x2  >= 10, "commandex3MinimaleEnLitres"

prob.writeLP("essence.lp")

# On utilise le solveur
prob.solve(solvers.PULP_CBC_CMD(fracGap=0.01))

# Le statut de la solution
print ("Status:", LpStatus[prob.status])

# On loupe et affiche les optimums de chaque var
for v in prob.variables():
    print (v.name, "=", v.varValue)
    
# Le resultat de la function objectif est ici
print ("Total de la fonction économique en EUROS", value(prob.objective))


# Status: Optimal
# brut1Enlitres = 28.571429
# brut2Enlitres = 10.0
# brut3Enlitres = 61.428571
# Total en EUROS 106.17142855