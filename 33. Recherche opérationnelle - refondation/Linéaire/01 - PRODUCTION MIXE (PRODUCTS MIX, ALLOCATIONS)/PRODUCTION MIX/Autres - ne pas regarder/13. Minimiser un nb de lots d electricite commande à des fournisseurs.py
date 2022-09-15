"""

https://complex-systems-ai.com/cours-lessons-theory/programmation-lineaire/lp-forme-primale-exercices-solutions/

Un brooker a besoin, pour sa clientèle, de 108 MWh d’électricité pour la ville 1 et de 96 MWh d’électricité pour la ville 2. 
Cependant, les lois de Kirchhoff ne permettent pas à un distributeur de cibler une ville unique pour le transit énergétique. 
Deux distributeurs desservent ces villes : le Distributeur A peut envoyer 12 MWh à la ville 1 et 8MWh à la ville 2 par lot 
acheté; le Distributeur B peut envoyer 9 MWh à la ville 1 et 12 MWh à la ville 2 par lot acheté. 
Les distributeur ont tous le même prix. 
Combien de lots doit acheter le brooker pour combler la demande énergétique des deux villes ? Résoudre par méthode graphique.

Dans un premier temps il faut réaliser le programme linéaire :


        min 1x1 + 1x2
        12x1  + 9x2 >= 108
        8x1   + 12 x2 >=96
        x1 >= 0
        x2 >= 0

      

"""

# Import the PuLP lib
from pulp import *

# Créer le problème linéaire et son type Minimize
prob = LpProblem ("MinimiserDemande", LpMinimize)


#  ---------------------------------------------------- ON CREE NOS DICTIONNAIRES -----------------------------------------------
# La liste de nos distributeurs
distributeurs = ["distributeur1","distributeur2"]
 


# Les besoins par ville en MW/h
besoins = {"villeA" : 108, "villeB" : 96}

# Les fournisseurs peuvent founir cela par distributeur pour la ville A en MW/h
villeA = {"distributeur1" : 12, "distributeur2" : 9}

# Les fournisseurs peuvent founir cela par distributeur pour la ville B en MW/h
villeB = {"distributeur1" : 8, "distributeur2" : 12}


#  ---------------------------------------------------- ON CREE LE PROGRAMME LINEAIRE -----------------------------------------------

# Un raccourcis pour prendre en compte les 2 variables de décision 
x = LpVariable.dicts("distributeur",distributeurs, cat='Integer')

# **** FONCTION OBJECTIF  : Minimiser le nombre de lots achetés. ****
prob += lpSum([1 * x[i] for i in distributeurs]), "MinimiserNbLots"

# Contrainte VilleA
prob += lpSum([villeA[i] * x[i] for i in distributeurs]) >= besoins["villeA"],"contrainteMinVilleA"

# Contrainte VilleB
prob += lpSum([villeB[i] * x[i] for i in distributeurs]) >= besoins["villeB"],"contrainteMinVilleB"

# Contrainte d'achat minimum distributeur 1
prob += x["distributeur1"] >= 0,"MinNbDistributeur1"

# Contrainte d'achat minimum distributeur 2
prob += x["distributeur2"] >= 0,"MinNbDistributeur2"

#  ---------------------------------------------------- ON EXECUTE LE PROGRAMME LINEAIRE (SIMPLEXE) -----------------------------------------------

# On écrit aussi le probleme dans un fichier
prob.writeLP ( "MinimiserNbDistributeur.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le statut de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables elements
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonction objectif est ici :
print ("TotalDesLotsaAcheter", value (prob.objective))


""" Status: Optimal
distributeur_distributeur1 = 6.0
distributeur_distributeur2 = 4.0
TotalDesLotsaAcheter 10.0 """