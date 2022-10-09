''' 

Optimiser le remplissage de camions / Trouvé sur Internet.

Traduit ... Solutions Non confirmées ...

SOURCE :

https://www.linkedin.com/pulse/bin-packing-python-pulp-michael-basilyan

http://www.or.deis.unibo.it/kp/Chapter8.pdf

'''


from pulp import *
import time



# Liste des tuples (nom,poids en kgs)

objets = [("Boite A", 5),
         ("Boite B", 6),
         ("Jouet A", 7),
         ("Jouet B", 32),
         ("Moto A", 2),
         ("Auto A", 32),
         ("Moto B", 5),
         ("Moto C", 7),
         ("Circuit 1", 9),
         ("Circuit 2", 12),
         ("Circuit 3", 11),
         ("Poupee 1", 1),
         ("Poupee 2", 2)]

objetCount = len(objets)

# Nombre maximum de containers autorisé
maxContainers = 32

# Capacité d'un container max 
containerCapacity = 32



# Indicator variable assigned 1 when the bin is used.
# Variable a 1 quand le container est utilisé
y = pulp.LpVariable.dicts('ContainerUtilises', range(maxContainers),
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

# Variable a 1 quand un objet est placé dans un container
possible_ObjetdansContainer = [(objetTuple[0], containerNum) for objetTuple in objets
                                            for containerNum in range(maxContainers)]
x = pulp.LpVariable.dicts('itemInBin', possible_ObjetdansContainer,
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

# Initialiser le probleme comme étant un problème de minimisation
prob = LpProblem("Bin Packing Problem", LpMinimize)

# Ajout de la function objectif à minimiser.
prob += lpSum([y[i] for i in range(maxContainers)]), "Objectif: Minimiser le nombre de containers utilises"

#
# La section des contraintes :
#

# Première contrainte : Pour chaque objet, la somme des containers ou il apparait doit être de 1 
for j in objets:
    prob += lpSum([x[(j[0], i)] for i in range(maxContainers)]) == 1, ("An item can be in only 1 bin -- " + str(j[0]))


# Deuxième contrainte : Pour chaque container, la somme de la pesée des objets ne doit pas excéder la capacité du container i
# Second constraint: For every bin, the number of objetsin the bin cannot exceed the bin capacity
for i in range(maxContainers):
    prob += lpSum([objets[j][1] * x[(objets[j][0], i)] for j in range(objetCount)]) <= containerCapacity*y[i], ("The sum of item sizes must be smaller than the bin -- " + str(i))

# Ecrire le modèle sur le disque
prob.writeLP("BinPack.lp")

# Résoudre l'optimisation
start_time = time.time()
prob.solve()
print("Solved in %s seconds." % (time.time() - start_time))


# Nombre de containers utilisés
print("Containers Utilises: " + str(sum(([y[i].value() for i in range(maxContainers)]))))

# Ce code sert seulement à afficher de jolis résultats
bins = {}
for itemBinPair in x.keys():
    if(x[itemBinPair].value() == 1):
        itemNum = itemBinPair[0]
        containerNum = itemBinPair[1]
        if containerNum in bins:
            bins[containerNum].append(itemNum)
        else:
            bins[containerNum] = [itemNum]

for b in bins.keys():
    print(str(b) + ": " + str(bins[b]))



""" Solved in 0.05271410942077637 seconds.
Containers Utilises: 5.0
0: ['Boite A', 'Boite B', 'Moto A', 'Moto B', 'Circuit 1', 'Poupee 1', 'Poupee 2']
10: ['Jouet A', 'Moto C', 'Circuit 3']
22: ['Jouet B']
12: ['Auto A']
1: ['Circuit 2']
 """