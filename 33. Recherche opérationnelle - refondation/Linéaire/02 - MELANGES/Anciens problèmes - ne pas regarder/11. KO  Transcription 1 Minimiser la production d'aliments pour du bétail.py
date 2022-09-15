""" 
Source du programme linéaire original : 
Livre "Programmation linéaire avec Excel" Page 101 . 

Copyright Eyrolle .

Production d'aliments pour du bétail.

Tentative de Transcription de son programme linéaire de Excel solveur, à Python PULP .

Note 1 : Dans le livre, les teneurs en nutriments sont exprimées en %, je les convertis ici en kgs .
Note 2 : Le programme traite de 2 aliments fabriqués en même temps pour une quantité différente, on ne sait pas pourquoi, c'est très compliqué .

Ingredient Protéines    Lipides    Glucides    prix achat       Qté dispo     
            (kg/kg)     (kg/kg)     (kg/kg)    (CentimesE/kg)    kgs
Avoine       0.136      0.071      0.07        0.8               11900
Mais         0.041      0.024      0.003       1                 23500
Melasse      0.05       0.03       0.25        0.75              750

Contraintes :

Protéines > 9.5 % ou 0.095 g    pour un kg
Lipides   > 2 % ou 0.002 g      pour un kg
Glucides  < 6 % ou 0.006 g      pour un kg

Couts (CentimesE/kg): 
broyage mélange granulation tamisage
    1.50    0.30    2.50        1

Question:
On doit fabriquer 9 tonnes de granulés, et 12 tonnes de farine, 
Quelles sont les quantités de matières premieres à acheter et les compositions des deux types d'aliments , 
de façon à minimiser le cout total ?


La Fonction économique objectif à minimiser:
naf = aliments fabriqués (granulé, farine)
nmp  = matieres premieres
nnu = nutriments
nop = opérations de processus de fabrication ( broyage mélange granulation tamisage )

La première contrainte : 
∑ (naf)*(npm)PAj Xij -> c'est les couts des matières premières donc ca doit être (9000granule * 0.80 + 9000granule * 1 + 9000granule * 0.75) + (12 000farine * 0.80 + 12 000farine * 1 + 12 000farine * 0.75) 
+
La 2ème contrainte
∑ (naf)*(npm-1)C1 Xij -> c'est les couts de broyage de l'avoine et du maîs seulement, donc ça doit être ( 9000granule * 1.50 + 9000granule * 1.50) + (12 000farine * 1.50 + 12 000farine * 1.50 )

La 3ème contrainte 
∑ (naf)*(npm)C2 Xij -> c'est le cout de mélange , donc je suppose que c'est ( 9000granule * 0.30 + 12 000 faribe * 0.30)

La 4ème contrainte ( INCOMPREHENSIBLE)
∑ (npm)C3 Xij -> c'est le cout de granulation , donc je suppose que c'est ( 9000granule * 2.50 ), hors, npm est la matrice des matières premières, je ne vois pas le sens du modèle.


La 5ème contrainte ( INCOMPREHENSIBLE)
∑ (npm)C4 Xij -> les couts de tamisage pour la farine , je suppose que c'est (12 000farine * 1 ), hors, npm est la matrice des matières premières, je ne vois pas le sens du modèle.


RESULTAT:
A cause des 2 aliments fabriqués, on ne comprends pas le modèle. C'est trop compliqué.
Je vais essayer de le refaire dans le fichier 12, sans les 2 aliments fabriqués, mais avec un seul.

"""

import pulp
from pulp import *

# Liste des ingrédients
Ingredients = ['AVOINE','MAIS','MELASSE']

# cout d'un ingrédient (cents/kg) 
couts = {
           'AVOINE': 0.8, 
            'MAIS': 1,
            'MELASSE':0.75
        }

# couts de production (cents/kg) 
couts-production = {
           'BROYAGE': 1.50, 
            'MELANGE': 0.30,
            'GRANULATION':2.50,
            'TAMISAGE':1
        }


# grammes de calcium  (kg/kg) 
proteines = {
            'AVOINE': 0.136, 
            'MAIS': 0.041,
            'MELASSE':0.05
              }

# grammes de protéines (kg/kg) 
lipides = {
           'AVOINE': 0.071, 
            'MAIS': 0.024,
            'MELASSE':0.03
            }

# grammes de fibres (kg/kg) 
glucides = {
           'AVOINE': 0.07, 
            'MAIS': 0.003,
            'MELASSE':0.25
            }


# On veut minimiser nos couts
prob = LpProblem("Probleme alimentaire", LpMinimize)

# On se sert du dictionnaire Ingredients pour créer nos variables
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)

# Notre function objectif s'exprime en euros ou en dollars
prob += lpSum([costs[i]*ingredient_vars[i] for i in Ingredients]), "Cout total des ingrédients par boite de conserve de 1kg"

# La production totale est de 1 kg
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 1 ,"conservation"

# On spécifie au solveur PULP Nos contraintes de qualité pour ne pas créer un paté de mauvaise qualité ...
prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.008, "calciumRequirementMin"
prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) <= 0.012, "calciumRequirementMax"
prob += lpSum([protein[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.22,  "proteinRequirementMin"
prob += lpSum([fiber[i]      * ingredient_vars[i] for i in Ingredients]) <= 0.05,  "fiberRequirementMax"

# POSSIBILITE Utilisation minimale en g par element
# for p in Ingredients:
#    prob += ingredient_vars[p] >= 10, f"min  for product {p}"


prob.writeLP("problemAlimentaire.lp")
prob.solve()
# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chauqe variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
    print (v.name, "=", v.varValue)

# Le résultat de la fonction objectif :
print ("Cout total des ingrédients par boite de conserve de 1kg = ", value(prob.objective), "Centimes")


""" 
Status: Optimal
Ingr_FARINE = 0.028170826
Ingr_MAIS = 0.64857216
Ingr_SOJA = 0.32325701
Cout total des ingrédients par boite de conserve de 1kg =  49.15629004

 """


