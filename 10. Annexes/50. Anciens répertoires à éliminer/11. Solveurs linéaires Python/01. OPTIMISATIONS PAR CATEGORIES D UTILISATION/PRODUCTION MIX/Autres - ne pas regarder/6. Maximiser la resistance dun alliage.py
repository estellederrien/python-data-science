"""
Usine de Feraille

UNe entreprise propose un alliage comprenant du cuivre, du zinc et de l'argent .
Trouver l'alliage le plus solide sous contrainte de conductivité électrique minimale pour 100 kgs.

Ensuite, trouver l'alliage le plus solide sous contrainte de conductivité électrique minimale et le moins cher automatiquement.


1 kg        solidité   conductivité (siemens factice )

cuivre              2           6

zinc                3           1

argent              1           4 

"""

# Import the PuLP lib
from pulp import *

# Créer le problème linéaire et son type Maximize
prob = LpProblem ("MaximiserResistance", LpMaximize)

# La liste de nos elements
elements = ["cuivre", "zinc","argent"]

# La solidité par elements
solidite        = {"cuivre": 2, "zinc": 3, "argent": 1}

# La conductivité par elements (en siemens factice)
conductivite    = {"cuivre": 4, "zinc": 1, "argent": 3}

# Un raccourcis pour prendre en compte les 3 variables de décision "cuivre", "zinc","argent" ,leur unité est le kilo
x = LpVariable.dicts("elements ", elements , 0)

# **** FONCTION OBJECTIF  : Maximiser la solidité totale de l'alliage. ****
prob += lpSum([solidite[i] * x[i] for i in elements ]), "MaximiserSolidite"

# Il faut respecter la contrainte de conduction électrique minimum pour 100kgs (en siemens factice)
prob += lpSum([conductivite[i] * x[i] for i in  elements]) >= 250,"MinimumConductivite"

# La production totale est de 100kgs
prob += lpSum([x[i] for i in elements]) == 100 ,"MinProdObjs"

# Utilisation minimale en kgs par element
for p in elements:
   prob += x[p] >= 10, f"min production units for product {p}"

# On écrit aussi le probleme dans un fichier
prob.writeLP ( "ResistanceAlliage.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables elements qui s'exprime en unité construites, soit en kilos
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonction objectif est ici :
print ("TotalResistance", value (prob.objective))


""" Status: Optimal
elements__argent = 10.0
elements__cuivre = 26.666667
elements__zinc = 63.333333
TotalResistance 253.333333 """