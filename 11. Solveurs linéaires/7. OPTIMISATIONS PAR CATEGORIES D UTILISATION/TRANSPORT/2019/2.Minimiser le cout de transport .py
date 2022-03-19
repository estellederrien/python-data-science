"""
Script de solveur linéaire pour optimiser le transport d'acier entre les fournisseurs et les usines.
Problème linéaire de 'supply Chain'.

Source :
The American Steel Problem for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell  2007

"""

# 1. On importe les librairies
from pulp import *

# 2. On liste les noeuds : Les usines fournisseurs ET les magasins.
Nodes = ["Paris",
         "Lille",
         "Rennes",
         "Strasbourg",
         "Lorient",
         "Nice",
         "Bordeaux",
         "Bruxelles",
         "Toulouse"]

# 3. On spécifie la quantité d'acier disponible et la demande en quantité des noeuds.
nodeData = {# NODE          Disponible Demande
         "Paris":           [10000,0],
         "Lille":           [15000,0],
         "Rennes":          [0,0],
         "Strasbourg":      [0,0],
         "Lorient":         [0,0],
         "Nice":            [0,3000],
         "Bordeaux":        [0,7000],
         "Bruxelles":       [0,4000],
         "Toulouse":        [0,6000]}

# Liste des arrêtes entre les noeuds
Arcs = [("Paris","Nice"),
        ("Paris","Rennes"),
        ("Paris","Strasbourg"),
        ("Paris","Lorient"),
        ("Lille","Rennes"),
        ("Lille","Strasbourg"),
        ("Lille","Lorient"),
        ("Lille","Toulouse"),
        ("Rennes","Nice"),
        ("Rennes","Bordeaux"),
        ("Strasbourg","Bordeaux"),
        ("Strasbourg","Bruxelles"),
        ("Lorient","Bruxelles"),
        ("Lorient","Toulouse")]

# On value les arrêtes par un cout, et la quantité de matière qui peut y transiter.
arcData = { #      ARC                Cout Min Max
        ("Paris","Nice"):             [0.5,0,1000],
        ("Paris","Rennes"):           [0.35,0,3000],
        ("Paris","Strasbourg"):       [0.45,1000,5000],
        ("Paris","Lorient"):          [0.375,0,5000],
        ("Lille","Rennes"):           [0.35,0,2000],
        ("Lille","Strasbourg"):       [0.45,2000,3000],
        ("Lille","Lorient"):          [0.4,0,4000],
        ("Lille","Toulouse"):         [0.45,0,2000],
        ("Rennes","Nice"):            [0.35,1000,5000],
        ("Rennes","Bordeaux"):        [0.55,0,6000],
        ("Strasbourg","Bordeaux"):    [0.375,0,4000],
        ("Strasbourg","Bruxelles"):   [0.65,0,4000],
        ("Lorient","Bruxelles"):      [0.6,0,2000],
        ("Lorient","Toulouse"):       [0.12,0,4000]}

# On sépare les dictionnaires pour que ce soit mieux compréhensible.
(supply, demand) = splitDict(nodeData)
(costs, mins, maxs) = splitDict(arcData)

# On spécifie que les variables sont au format integer
# Creates the boundless Variables as Integers
vars = LpVariable.dicts("Route",Arcs,None,None,LpInteger)

# Crée les limites supérieure et inférieure des variables (?)
for a in Arcs:
    vars[a].bounds(mins[a], maxs[a])

# On spécifie que c'est un problème de minimisation 
prob = LpProblem("Probleme de transport acier",LpMinimize)

# La fonction objectif est diminuer le cout total du transport , tout en saturant la demande des noeuds des magasins.
prob += lpSum([vars[a]* costs[a] for a in Arcs]), "Coût total du transport"

# Crée toutes les contraintes du problème - cela garantit que le montant entrant dans chaque nœud est au moins égal au montant restant. (?)
# la loi de conservation du flot : https://fr.wikipedia.org/wiki/Lois_de_Kirchhoff
for n in Nodes:
    prob += (supply[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if j == n]) >=
             demand[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if i == n])), "Conservation du flot d'acier dans le nœud %s"%n

# On écrite le résumé du LP dans un fichier.
prob.writeLP("TransportProblem.lp")

# On résouds le problème en utilisant le soolveur de notre choix en paramêtre.
prob.solve()

# Le status de la solution est imprimé à l'écran .
print("Statut:", LpStatus[prob.status])

# Chaque variable est affichée avec son statut maximal.
for v in prob.variables():
    print(v.name, "=", v.varValue)

# La valeur de la fonction objectif optimisée est imprimée à l'écran 
print("Le cout total du transport est de  = ", value(prob.objective))