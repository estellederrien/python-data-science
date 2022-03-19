#

""" 
Ici , on va tenter de trouver le meme résultat avec pulp que le problème du SOLVEUR EXCEL suivant :

Source : Programmation linéaire avec Excel - Eyrolles - Page 96 - Industries Minières et de process …

Auteur : Marc Sevaux - Christian Prins 

Acheter le livre : Fnac 

# Programme pulp élaboré par Nicolas-Estelle HULEUX pour ensuite le rendre générique pour mon app https://www.solvgraph.com

Ce problème étant probablement tiré d'un exemple similaire en Anglais comme celui ci : #Source :https://www.lindo.com/downloads/LINGO_text/10-Blending_of_Input_Materials.pdf
Si on utilise exactement la même technique que LINDO, on doit trouver pareil que le résultat excel de l'exemple Excel de Marc Sevaux.

L'histoire : 

Une entreprise a reçu une commande de 5 tonnes d'acier pour bateau ,

Il doit avoir les caractéristiques suivantes :
Elément chimique	Pourcentage Minimal	Pourcentage Maximal
Carbone(C)	        2	                3
Cuivre(Cu)	        0.4	                0.6
Manganèse(Mn)	    1.2	                1.65

 

Pour fabriquer cet acier, l'entreprise dispose de 7 matières premières :

 
Matière première	    C%	    Cu%	    Mn%	    Stocks disponibles (kgs)	Coûts(Euros/kilos)
Alliage de fer 1	    2.5	    0	    1.3	    4000	                    1.20
Alliage de fer 2	    3	    0	    0.8	    3000	                    1.50
Alliage de fer 3	    0	    0.3	    0	    6000	                    0.90
Alliage de cuivre 1     0	    90	    0	    5000	                    1.30
Alliage de cuivre 2     0	    96	    4	    2000	                    1.45
Alliage d'Aluminium 1   0	    0.4	    1.2	    3000	                    1.20
Alliage d'Aluminium 2   0	    0.6		0       2500	                    1 


"""

import pulp
from pulp import *

# On veut minimiser le cout de 5 tonnes d'alliage #
prob = LpProblem("Production 5 tonnes",LpMinimize)

# On crée nos variables de décisions
# Ca veut dire qu'on doitchoisir quels sont les alliages les plus judicieux à choisir et on leur donne un nom à chacun
# C'est le nombre de kg de l’alliage i utilisés.
# vu que la valeur du nombre de kgs peut être décimal, on spécifie que c'est une variable de décision de type décimale en écrivant Continuous:
F1 = LpVariable("F1", lowBound = 0,cat='Continuous')
F2 = LpVariable("F2", lowBound = 0,cat='Continuous')
F3 = LpVariable("F3", lowBound = 0,cat='Continuous')
CU1 = LpVariable("CU1", lowBound = 0,cat='Continuous')
CU2 = LpVariable("CU2", lowBound = 0,cat='Continuous')
AL1 = LpVariable("AL1", lowBound = 0,cat='Continuous')
AL2 = LpVariable("AL2", lowBound = 0,cat='Continuous')

# Fonction objectif / min (ci * xi) ou ci est exprimé en cout unitaire par kilo 
prob += 1.20 * F1 + 1.50 * F2 + 0.90 * F3 + 1.30 * CU1 + 1.45 * CU2 +  1.20  *  AL1  +  1  *  AL2 , "Cout total"

#! On ne peut pas utiliser plus que le STOCK exprimé en kgs de  matières premières suivantes ( voir la colonne stock du 2 second tableau)
prob += F1 <= 4000; 
prob += F2 <= 3000; 
prob += F3 <= 6000; 
prob += CU1 <= 5000; 
prob += CU2 <= 2000; 
prob += AL1 <= 3000; 
prob += AL2 <= 2500; 


#! -------------------- Les requirements qualité -----------------------!

#! Carbon content; 
# Ici, 100 veut dire qu'on a un besoin en taux carbone mainimal de 2% de 5000 kgs  , ça fait  100 kgs ( voir aussi la doc lindo du fchier 7 de ce rep)
# par contre, les pourcentages dans la partie gauche sont maintenus au format décimal (idem LINDO et l'exemple du fichier  3 aussi )!
prob += 0.025 * F1 + 0.03 * F2 >= 100; 
prob += 0.025 * F1 + 0.03 * F2 <= 150; 

##! Cuivre content; 
prob += 0.003 * F3 + 0.90 * CU1 + 0.96 * CU2 + 0.004 * AL1 + 0.006 * AL2  >=  20; 
prob += 0.003 * F3 + 0.90 * CU1 + 0.96 * CU2 + 0.004 * AL1 + 0.006 * AL2  <=  30; 

##! Manganese content; Ici, 60 veut dire 1,2% de 5000 kgs est égal à 60 kgs, on trouve la même technique chez LINDO et l'exmple 3 de ce rep
prob += 0.013 * F1 + 0.008 * F2 + 0.04 * CU2 + 0.012 * AL1   >=  60; 
prob += 0.013 * F1 + 0.008 * F2 + 0.04 * CU2 + 0.012 * AL1   <=  82.5;  


#! Finish good requirements; 
# On doit spécifier que le total de nos variables de décisions exprimée en kgs doit être égal à 5000 kgs soit 5 tonnes absolument, c'est donc logique, pas de pourcentages ici.
prob += F1 +  F2 +   F3 +  CU1 +  CU2 +   AL1 +  AL2 ==  5000 , "total"

# On affiche notre résultat dans la console :
prob.writeLP("monAlliage.lp")
prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients  = ", value(prob.objective))


""" Hourra ! Le résultat est le même que dans le livre de Marc Sevaux !!
Pulp trouve exactement pareil que EXCEL !!
Il ne reste plus qu'à créer le code FULL STACK dans mon app SolvGraph.com maintenant, pour rendre tout cela facile comme un jeu  !

Status: Optimal
AL1 = 574.62426
AL2 = 0.0
CU1 = 0.0
CU2 = 27.612723
F1 = 4000.0
F2 = 0.0
F3 = 397.76302
Total Cost of Ingredients  =  5887.57427835 """


