"""
https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

The Simplified Whiskas Model Python Formulation for the PuLP Modeller

Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Création de paté sous contrainte nutritionelles .

# Elément 	Proteines 	Gras 	Fibre 	Sel
# Poulet 	0.100 		0.080 	0.001 	0.002
# Steak 	0.200 		0.100 	0.005 	0.005

# Le prix du poulet est de 0.013 euros par grammes
# Le prix du steak est de 0.008 euros par grammes

# Importer la lib PuLP 
from pulp import *

#Créer la variable du problème
prob = LpProblem("TheWhiskasProblem",LpMinimize)

# Les 2 vars ont une limite en zéro
x1=LpVariable("PouletPercent",0,None,LpInteger)
x2=LpVariable("SteakPercent",0)

# La fonction objectif est de minimiser le prix 
prob += 0.013*x1 + 0.008*x2, "Cout"

# Les 5 contraintes sont entrées .
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100*x1 + 0.200*x2 >= 8.0, "ProteinRequirement"
prob += 0.080*x1 + 0.100*x2 >= 6.0, "FatRequirement"
prob += 0.001*x1 + 0.005*x2 <= 2.0, "FibreRequirement"
prob += 0.002*x1 + 0.005*x2 <= 0.4, "SaltRequirement"

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

# On utilise le solveur
prob.solve()

# Le statut de la solution
print ("Status:", LpStatus[prob.status])

# On loupe et affiche les optimums de chaque var
for v in prob.variables():
    print (v.name, "=", v.varValue)
    
# Le resultat de la function objectif est ici
print ("Total", value(prob.objective))
