"""
Problème linéaire de Raffinerie 7

Ajout d'une disponibilité maximale chez les 3 fournisseurs des 3 bruts et du cout de transport au litre .

** Les variables de décision sont en LITRES **

** Expérimental (non corrigé- non confirmé) ** 
"""

# Création de Fuel .

# HISTOIRE :
# On veut créer 1000 litres d'essence, en mélangeant 3 bruts différents ayant des caractéristiques différentes .
#On veut payer le moins cher possible les 1000 litres d'essence, tout en respectant les contraintes de production et de commande .
# La direction ne veut pas que le cout de transport dépasse 65 euros pour 1000 litres d'essence 
# (pourtant, on remarque que le cout de la fonction objectif globale diminue si on augmente la valeur de la contrainte de cout de transport à 100, 
# ca veut donc dire que c'est une fausse économie à cause du prix du litre de vouloir économiser sur le trajet)

# CARACTERISTIQUES DE 1 LITRE DE BRUT 
# Elément 	Benzène         Plomb	        Prix     Disponibilité maxi  Cout de transport en euros 
# brut1  	0.02 litres	    0.08 litres     1.025       450              0.1  E par litre soit 100 E pour 1000 litres
# brut2 	0.05 litres	    0.06 litres     1.030       500              0.09  E par litre soit 90 E  pour 1000 litres
# brut3 	0.03 litres	    0.01 litres     1.075       1000             0.03  E par litre soit 30 E  pour 1000 litres  

# Le prix du brut1  est de 1.025 euros par litres
# Le prix du brut2  est de 1.085 euros par litres, il est plus cher
# Le prix du brut2  est de 1.075 euros par litres

# Importer la lib PuLP 
from pulp import *

#Créer la variable du problème
prob = LpProblem("lp",LpMinimize)

# Les 3 vars ont une limite en zéro , ce sont des unités de litres
x1=LpVariable("brut1Enlitres",lowBound = 0, cat='Continuous')
x2=LpVariable("brut2Enlitres",lowBound = 0, cat='Continuous')
x3=LpVariable("brut3Enlitres",lowBound = 0, cat='Continuous')

# La fonction objectif est de minimiser le prix en EUROS 
prob += 1.025*x1 + 1.030*x2 + 1.075*x3  , "Cout"

# contraintes en LITRES

# On veut commander 1000 litres
prob += x1 + x2 + x3 == 1000, "Litres"

# Disponibilité chez les fournisseurs
prob += x1  <= 450, "disponibiliteFournisseur1"
prob += x2  <= 500, "disponibiliteFournisseur2"
prob += x3  <= 1000, "disponibiliteFournisseur3"

# Cout de transport 
prob += 0.1 * x1 + 0.09 * x2 + 0.03 * x3 <= 65, "CoutTransportMaxiEnEuros"

# ON doit commander au minimum 100 litres aux fournisseurs , ce sont des contraintes de commande
prob += x1  >= 100, "commandex1MinimaleEnLitres1"
prob += x2  >= 100, "commandex2MinimaleEnLitres2"
prob += x2  >= 100, "commandex3MinimaleEnLitres3"

# Sur ces 1000 litres, un minimum de 11 litres de benzène, et un maximum de 35 litres de plombs , ce sont des contraintes qualité
# prob += 0.02 * x1  + 0.05 * x2 + 0.03 * x3  >= 11, "benzeneMin"
# prob += 0.08 * x1  + 0.06 * x2 + 0.01 * x3  <= 35, "PlombMax"

prob.writeLP("essence2.lp")

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
# brut1Enlitres = 100.0
# brut2Enlitres = 466.66667
# brut3Enlitres = 433.33333
# Total de la fonction économique en EUROS 1048.99999985