''' Auteur : https://docs.python-mip.com/en/latest/examples.html

Le but de cette optimisation est de minimiser le temps de réalisation d'un projet, 
tout en connaissant la durée de chaque tâches et leurs successeurs et prédécesseurs successifs, 
et sous contrainte du montant des ressources nécessaires à chaque tâche

Les ressources nécessaires ne sont pas présente dans le premier problème du stade du livrae optimisations avec excel de eyrolle, il 
y a donc ici une difficulté complémentaire.


Ordonnancement de projet à ressources limitées

Le problème d'ordonnancement de projet à contraintes de ressources (RCPSP) est un problème d'optimisation combinatoire qui consiste à trouver un ordonnancement réalisable pour un ensemble de n

emplois soumis à des contraintes de ressources et de préséance. Chaque travail a un temps de traitement, un ensemble de travaux successeurs et une quantité requise de ressources différentes. Les ressources peuvent être rares mais sont renouvelables à chaque période. Les contraintes de priorité entre les travaux signifient qu'aucun travail ne peut démarrer avant que tous ses prédécesseurs ne soient terminés. Les jobs doivent être planifiés de manière non préemptive, c'est-à-dire qu'une fois démarrés, leur traitement ne peut pas être interrompu.

Le RCPSP dispose des données d'entrée suivantes :

J       : ensemble de tâches
R       : ensemble de ressources renouvelables
S       : ensemble de précédences entre les emplois (i,j)∈J×J
T       : horizon de planification : ensemble des délais de traitement possibles pour les travaux
pj      : temps de traitement du travail j
u(j,r)  : quantité de ressource r requis pour le traitement de la tâche j
cr      : capacité de ressource renouvelable r

En plus des travaux qui appartiennent au projet, l'ensemble J
contient les jobs 0 et n+1, qui sont des jobs fictifs qui représentent respectivement le début et la fin de la planification. Le temps de traitement des travaux fictifs est toujours nul et ces travaux ne consomment pas de ressources.


'''

from itertools import product
from mip import Model, xsum, BINARY

n = 10  # note there will be exactly 12 jobs (n=10 jobs plus the two 'dummy' ones)

p = [0, 3, 2, 5, 4, 2, 3, 4, 2, 4, 6, 0] # Durée de chque tâche

u = [[0, 0], [5, 1], [0, 4], [1, 4], [1, 3], [3, 2], [3, 1], [2, 4],
     [4, 0], [5, 2], [2, 5], [0, 0]] # quantité de ressource r requise pour le traitement de la tâche j

c = [6, 8] # capacité de ressource renouvelable r (?)

S = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 9], [2, 10], [3, 8], [4, 6],
     [4, 7], [5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [8, 11], [9, 11], [10, 11]] # successeurs des nodes [node, successeur]

(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

model = Model()

x = [[model.add_var(name="x({},{})".format(j, t), var_type=BINARY) for t in T] for j in J]

model.objective = xsum(t * x[n + 1][t] for t in T)

for j in J:
    model += xsum(x[j][t] for t in T) == 1

for (r, t) in product(R, T):
    model += (
        xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
        <= c[r])

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

model.optimize()

print("Schedule: ")
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))
print("Makespan = {}".format(model.objective_value))