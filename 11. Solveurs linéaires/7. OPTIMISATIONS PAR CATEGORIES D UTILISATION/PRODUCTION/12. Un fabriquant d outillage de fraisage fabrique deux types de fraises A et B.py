"""

https://complex-systems-ai.com/cours-lessons-theory/programmation-lineaire/lp-forme-primale-exercices-solutions/

Un fabriquant d’outillage de fraisage fabrique deux types de fraises : A et B. 
Les fraises de type A se vendent 300 l’unité, et se fabrique à avec 1 unité d’acier, 2 unités de carbure amovible 
et 1 unité de diamant synthétique. Les fraises de type B se vendent 200 l’unité, 
et se fabrique à avec 2 unité d’acier, 1 unités de carbure amovible et 1 unité de diamant synthétique. 
Les stocks sont de 5 unités d’acier, 5 unités de carbure et 2 unités de diamant. 
Le fabriquant souhaite construire au moins 5 fraises de type A et 5 fraises de type B. 
Le coût d’entretien de l’usine est de 2500. Comment le fabriquant doit-il répartir sa production pour maximiser son profit, 
est-ce rentable ?

Dans un premier temps il faut réaliser le programme linéaire :

    Fonction objectif : z = 300A+200B-2500
    Contraintes :
        A+2B  ≤ 5
        2A+B ≤ 5
        A+B ≤ 2
        A  ≥ 5
        B  ≥ 5

        Le programme n’est pas sous forme canonique, il faut le rendre sous cette forme avant de le résoudre.

        Posons x1 = A-5 et x2 = B-5. Le programme linéaire devient le suivant :
        max 300x1 + 200x2
        x1  + 2x2 <=20
        2x1 + x2  <=22
        x1  +  x2 <= 12 
        x1 >= 0
        x2 >= 0

        NOTE : SEUL LE FORME CANONIQUE FONCTIONNE POUR LINSTANT, JE VOIS PAS COMMENT IL TROUVE (15,7) en resultat ensuite 

"""

# Import the PuLP lib
from pulp import *

# Créer le problème linéaire et son type Maximize
prob = LpProblem ("MaximiserProfit", LpMaximize)


#  ---------------------------------------------------- ON CREE NOS DICTIONNAIRES -----------------------------------------------
# La liste de nos elements
elements = ["fraiseA","fraiseB"]

# Le prix par élément
prix = {"fraiseA" : 300, "fraiseB" : 200}

# L'acier nécessaire pour créer un élémenent
acier = {"fraiseA" : 1, "fraiseB" : 2}

# Le carburant amovible nécessaire pour créer un élémenent
carburant = {"fraiseA" : 2, "fraiseB" : 1}

# Le diamant synthétique nécessaire pour créer un élémenent
diamant = {"fraiseA" : 1, "fraiseB" : 1}

# Les stocks 
stocks = {"acier":5,"carburant":5,"diamant":2}

# le cout d'entretien de l'usine :
entretien = 2500

#  ---------------------------------------------------- ON CREE LE PROGRAMME LINEAIRE -----------------------------------------------

# Un raccourcis pour prendre en compte les 2 variables de décision fraiseA et fraiseB
x = LpVariable.dicts("elements", elements , 0)

# **** FONCTION OBJECTIF  : Maximiser le profit. ****
prob += lpSum([prix[i] * x[i] for i in elements ]), "MaximiserProfit"

# Contrainte Acier
prob += lpSum([acier[i] * x[i] for i in  elements]) <= 20,"MaximumUtilisationAcier"

# Contrainte carburant
prob += lpSum([carburant[i] * x[i] for i in  elements]) <= 22,"MaximumUtilisationCarburant"

# Contrainte diamant
prob += lpSum([diamant[i] * x[i] for i in  elements]) <= 12,"MaximumUtilisationDiamant"

# Contrainte de production min fraiseA
prob += x["fraiseA"] >= 0,"MinProdFraiseA"

# Contrainte de production min fraiseB
prob += x["fraiseB"] >= 0,"MinProdFraiseB"

#  ---------------------------------------------------- ON EXECUTE LE PROGRAMME LINEAIRE (SIMPLEXE) -----------------------------------------------

# On écrit aussi le probleme dans un fichier
prob.writeLP ( "ProfitFraises.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le statut de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables elements
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonction objectif est ici :
print ("TotalPrix", value (prob.objective))


""" Status: Optimal
elements_fraiseA = 10.0
elements_fraiseB = 2.0
TotalPrix 3400.0 """