# https://www.linkedin.com/pulse/bin-packing-python-pulp-michael-basilyan

# Bin packing as a LP problem:
# http://www.or.deis.unibo.it/kp/Chapter8.pdf
#
# Requisite Wiki Article:
# https://en.wikipedia.org/wiki/Bin_packing_problem
#
# PuLP Library:
# https://pythonhosted.org/PuLP/index.html
#

''' 
Traduction : 

Motivé par l'envie d'apprendre python et par la lecture de l'article Wikipedia sur le bin packaging 

(c'est un sujet fascinant, vraiment), j'ai décidé de passer une soirée à construire un solveur Bin Packing 

en utilisant Python. Le problème du Bin Packing est simple à expliquer : 

vous avez une liste d'articles de différents poids (ou tailles) et vous souhaitez les emballer 

dans le plus petit nombre de bacs possible. Les bacs sont finis et de même taille.

L'emballage des bacs est un problème NP-difficile et sa résolution 

se fait généralement avec des heuristiques personnalisées 

(couvertes à de nombreux endroits sur le Web, y compris l'article wiki.) 

Pour mes besoins, j'ai décidé de l'exprimer comme un programme linéaire entier et d'utiliser un solveur existant. Pour faire du LP en Python, j'ai choisi PuLP.

Cette page a une bonne description de la façon d'exprimer le 1D Bin Packing en tant qu'ILP. 

Je vais le résumer ici.

(Note latérale : voici le code sur GitHub avec des commentaires détaillés.) 



**Variables**

Tout d'abord, nous devons avoir quelques variables qui peuvent être utilisées pour décrire les contraintes 

et l'objectif du problème.

    y[i] = 1 si un bin i est utilisé, 0 sinon.
    x[(i, j)] = 1 si l'élément j est placé dans le bac i, 0 sinon
    z = nombre de bacs réellement utilisés
    n = nombre d'articles
    c = capacité d'un seul bac
    w[j] = poids (ou taille) de l'article j

**Objectif**

Minimiser le nombre de bacs utilisés

**contraintes**

    Un article peut exister dans un et un seul bac :
    La somme des éléments d'un bac ne peut pas dépasser sa capacité s'il est utilisé,
     sinon elle ne peut pas dépasser 0 puisqu'il n'est pas utilisé :

Maintenant, tout ce que nous avons à faire est de le convertir dans le langage de PuLP. 

Commençons par configurer quelques exemples d'éléments et des bacs. 

Je vais exprimer les éléments sous forme de liste de tuples : un nom et un poids/taille.



'''



from pulp import *
import time

#
# Une liste de tuples d'éléments (nom, poids) -- le nom n'a de sens que pour les humains.
# Le poids et la taille sont utilisés de manière interchangeable ici et ailleurs.
#
items = [("a", 5),
         ("b", 6),
         ("c", 7),
         ("d", 32),
         ("e", 2),
         ("f", 32),
         ("g", 5),
         ("h", 7),
         ("i", 9),
         ("k", 12),
         ("l", 11),
         ("m", 1),
         ("n", 2)]

itemCount = len(items)

# Nombre de bacs maximum 
maxBins = 32

# Taille d'un bac
binCapacity = 32

''' Vient ensuite la partie un peu délicate : 

déclarer des variables dans le langage de PuLP.

La fonction LpVariable.dicts prend une chaîne de nom et une liste. 

Il crée ensuite un dictionnaire dont les clés sont le nom concaténé avec chacun des éléments de la liste. 

Chaque clé de dictionnaire est l'une des variables utilisées dans les contraintes et l'objectif. 

Il prend également une borne inférieure sur les valeurs, une borne supérieure et la catégorie de variable. 

Dans notre exemple, nous n'avons que des variables entières à indicateur 0/1.
 '''


# Variable indicatrice affectée à 1 lorsque le bac est utilisé.
y = pulp.LpVariable.dicts('BinUsed', range(maxBins),
                            lowBound = 0,
                            upBound = 1,
                            cat = "Integer")

# Une variable indicatrice qui est affectée à 1 lorsque l'élément est placé dans binNum
possible_ItemInBin = [(itemTuple[0], binNum) for itemTuple in items
                                            for binNum in range(maxBins)]
x = pulp.LpVariable.dicts('itemInBin', possible_ItemInBin,
                            lowBound = 0,
                            upBound = 1,
                            cat = "Integer")

# Initialiser le problème
prob = LpProblem("Bin Packing Problem", LpMinimize)

''' L'objectif est le premier élément ajouté au prob. 

Vous remarquerez qu'il s'agit simplement d'une somme sur LpVariable y et que c'est l'objectif mathématique 

traduit en Python/PuLP.

De même, les contraintes sont simplement l'expression mathématique des contraintes 

traduites en Python/PuLP. 

Dans la première contrainte, nous parcourons tous les éléments j 

et spécifions que pour chaque élément, la somme des variables indicatrices xij 

sur les cases 0..i...n-1 doit être 1 pour l'élément j. '''



# Ajoutez la fonction objectif.
prob += lpSum([y[i] for i in range(maxBins)]), "Objective: Minimize Bins Used"

#
# Ceci est la section des contraintes.
#

# Première contrainte : Un objet ne peut être que dans un seul bac
for j in items:
    prob += lpSum([x[(j[0], i)] for i in range(maxBins)]) == 1, ("An item can be in only 1 bin -- " + str(j[0]))

# Deuxième contrainte : Pour chaque bac, le nombre d'articles dans le bac ne peut pas dépasser la capacité du bac
for i in range(maxBins):
    prob += lpSum([items[j][1] * x[(items[j][0], i)] for j in range(itemCount)]) <= binCapacity*y[i], ("The sum of item sizes must be smaller than the bin -- " + str(i))

# Ecrire le modèle sur le disque
prob.writeLP("BinPack.lp")

# Résoudre l'optimisation
start_time = time.time()
prob.solve()
print("Solved in %s seconds." % (time.time() - start_time))


# Les bacs utilisés
print("Bins used: " + str(sum(([y[i].value() for i in range(maxBins)]))))

# Améliorer l'aspect des résultats.
bins = {}
for itemBinPair in x.keys():
    if(x[itemBinPair].value() == 1):
        itemNum = itemBinPair[0]
        binNum = itemBinPair[1]
        if binNum in bins:
            bins[binNum].append(itemNum)
        else:
            bins[binNum] = [itemNum]

for b in bins.keys():
    print(str(b) + ": " + str(bins[b]))

'''     Une fois que c'est terminé, nous pouvons examiner les valeurs de x pour voir quel article, 
    
    les paires de bacs sont définies sur 1, indiquant que l'article a été placé dans le bac.

Voici le code complet sur GitHub. '''