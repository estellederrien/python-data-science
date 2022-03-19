""" 
cf : Recherche opérationnelle pour ingénieurs I (de Werra, Liebling, Hˆeche) ; page 33
documentation 5 en français sur nicolas15000 github

Code PULP Réalisé par Nicolas Estel HULEUX

Un fabricant doit produire 120 kg d’un alliage comportant 30 % de plomb, 30 % de zinc et 40 % d’´etain.
Sur le marché, on trouve les alliages suivants :

alliage     1   2   3   4   5   6   7   8   9
% plomb     10  10  40  60  30  30  30  50  20
% zinc      10  30  50  30  30  40  20  40  30
% étain     80  60  10  10  40  30  50  10  50
coût/kg     4.1 4.3 5.8 6.0 7.6 7.5 7.3 6.9 7.3

Comment obtenir un alliage de la composition voulue dont le cout est minimum ? 

Formuler ce problème sous forme de programme linéaire. 

"""

# Solution :
# Notons 
# pi le pourcentage de plomb dans l’alliage i.
# zi le pourcentage de zinc dans l’alliage i.
# ei le pourcentage d’étain dans l’alliage i.
# ci le coût unitaire de production de l’alliage i.
# Introduisons les variables suivantes : xi = le nombre de kg de l’alliage i utilisés.
# 


# Notre fonction objectif est de réduire le cout de 120 kgs d'un alliage
# Comme on a affaire à une matrice, on va pas réecrire chaque variable de décision et chaque valeur de cout 
# On réduit cela comme ça :
# Et le comme le nb de variables de décision est forcément de neuf donc de x1 ... à x9
# min (ci * xi)

# Sous les contraintes  

# Notre teneur en plomb
# (30% = 0.30 de plomb, et 120 , c'est les 120 kgs nécessaires) ,
# Cette contrainte comprends donc une valeur de type "pourcentage" et une valeur de type "unitaire" mixée ensemble 
# tout simplement, 30% de 120kgs, peut aussi s'écrire 0.30 * 120 afin d'éliminer la fraction pour simplifier le programme linéaire (niveau CM2 - école primaire)
# On le vérifie car 30 * 120 / 100 = 36 , et 0.30 * 120 = 36 , c'est PAREIL
# et donc 0.30 * 120 veut dire qu'on veut absolument que 30% du total de notre mélange soit du plomb, ce qui veut dire 36 kgs: 
# Σ (pi * xi) = 0.30 * 120 


# Notre teneur en zinc
# Σ (zi * xi) = 0.30 * 120 

# Notre teneur en étain
# Σ (ei * xi) = 0.40 * 120 

# La somme des variables de décision est supérieure à 0
# xi >= 0

""" Maintenant, on essaye de résoudre avec PULP : 

on prends pour exemple le whiskas model simplifié
"""

import pulp
from pulp import *

# On veut minimiser le cout de 120kgs d'alliage
prob = LpProblem("Production 120kgs",LpMinimize)

# ON crée nos variables de décisions, il y en a 9
# Ca veut dire qu'on doitchoisir quels sont les alliages les plus judicieux à choisir et on leur donne un nom à chacun
# C'est le nombre de kg de l’alliage i utilisés.
# vu que la valeur du nombre de kgs peut être décimal, on spécifie que c'est une variable de décision de type décimale en écrivant Continuous:
x1 = LpVariable("Alliage1", lowBound = 0,cat='Continuous')
x2 = LpVariable("Alliage2", lowBound = 0,cat='Continuous')
x3 = LpVariable("Alliage3", lowBound = 0,cat='Continuous')
x4 = LpVariable("Alliage4", lowBound = 0,cat='Continuous')
x5 = LpVariable("Alliage5", lowBound = 0,cat='Continuous')
x6 = LpVariable("Alliage6", lowBound = 0,cat='Continuous')
x7 = LpVariable("Alliage7", lowBound = 0,cat='Continuous')
x8 = LpVariable("Alliage8", lowBound = 0,cat='Continuous')
x9 = LpVariable("Alliage9", lowBound = 0,cat='Continuous')

# min (ci * xi) ou xi est exprimé en décimales de kgs et ci est exprimé en euros
prob += 4.1*x1 + 4.3*x2 + 5.8*x3 + 6.0*x4 + 7.6*x5 + 7.5*x6 + 7.3*x7 + 6.9*x8 + 7.3*x9 , "Cout total des ingrédients"


# On doit spécifier que le total de nos variables de décisions exprimée en kg doit être égal à 120 kgs absolument, c'est donc logique, pas de pourcentages ici.
prob += x1 +  x2 +  x3 +   x4 +  x5 +  x6 +   x7 +  x8 + x9 ==  120 , "total"


# Σ (pi * xi) = 0.30 * 120 
# % plomb     10  10  40  60  30  30  30  50  20
# On veut que la somme soit égale à 36 kgs , 30% de 120 kgs est = à 36 kgs (0.30 * 120 = 36 kgs)
# 0.10 * x1 veut dire qu'on a 10% de la variable de décision x1 exprimée en kgs décimales.
prob += 0.10*x1 +  0.10*x2 +  0.40*x3 +   0.60*x4 +  0.30*x5 +  0.30*x6 +   0.30*x7 +  0.50*x8 + 0.20*x9 == 0.30 * 120 , "plomb"

# Σ (zi * xi) = 0.30 * 120 
# % zinc      10 30  50  30  30  40  20  40  30
prob += 0.10*x1 +  0.30*x2 +  0.50*x3 +   0.30*x4 +  0.30*x5 +  0.40*x6 +   0.20*x7 +  0.40*x8 + 0.30*x9 == 0.30 * 120 , "zinc"

# Σ (ei * xi) = 0.40 * 120 
# % étain     80  60  10  10  40  30  50  10  50
prob += 0.80*x1 +  0.60*x2 +  0.10*x3 +   0.10*x4 +  0.40*x5 +  0.30*x6 +   0.50*x7 +  0.10*x8 + 0.50*x9 == 0.40 * 120 , "etain"




""" 
note importante, si on écrit les contraintes sous la forme  : 
prob += 10*x1 +  10*x2 +  40*x3 +   60*x4 +  30*x5 +  30*x6 +   30*x7 +  50*x8 + 20*x9 == 30 * 120 , "plomb"
fonctionne aussi et donne le même résultat !

C'est à ce niveau que je trouve cela bizarre à gérer, donc certes on a un resultat plausible, mais
Je trouve ce mix de pourcentages étrange, il faut donc trouver des tas de programmes linéaires y compris excel
et vérifier que cette méthode fonctionne réellement et que le résultat est correct.

 """


prob.writeLP("monAlliage.lp")
prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients  = ", value(prob.objective))


""" 
Status: Optimal
Alliage1 = 0.0
Alliage2 = 72.0
Alliage3 = 0.0
Alliage4 = 48.0
Alliage5 = 0.0
Alliage6 = 0.0
Alliage7 = 0.0
Alliage8 = 0.0
Alliage9 = 0.0
Total Cost of Ingredients  =  597.5999999999999

Donc : Si ce premier essai est bon , ça voudrait dire qu'on doit acheter 

72 kgs d'alliage 2 , et 48kgs d'alliage 4 pour obtenir nos 
120 kgs d'alliage, sous contrainte de pourcentage de zinc, etain et plomb exprimées en %
afin de minimiser notre cout .
Notre cout global de 120 kgs d'alliage sera donc de 597.59999 euros !


Comment vérifier si c'est bon ? 

Déjà, on voit que 72kgs + 48kgs = 120kgs , donc là, on est bon pour notre contrainte de poids exprimée en kgs.

Vérification de la function objectif : 
pour le cout total : substituer les valeurs trouvées pour les vars de décision
 dans la function objectif et voir si c'est bon, mais il n'est pas du genre à faire des erreurs de calcul à cet endroit lol , 
 la question est : A-t-il vraiment minimisé ?.

Vérification des contraintes :
On peut aussi substituer nos valeurs obtenues dans les contraintes exprimées en pourcents pour voir si 
nos contraintes sont réellement respectées:

Par exemple la contrainte plomb 
72*0.10 + 48*0.60  est il égal à 30 % de plomb soit 36 kgs dans notre cas ?
On voit que ça fait 36 ! Miracle ! Donc notre 1ère contrainte est bien respectée, hourra !
La puissance de calcul est DINGUE !


"""


