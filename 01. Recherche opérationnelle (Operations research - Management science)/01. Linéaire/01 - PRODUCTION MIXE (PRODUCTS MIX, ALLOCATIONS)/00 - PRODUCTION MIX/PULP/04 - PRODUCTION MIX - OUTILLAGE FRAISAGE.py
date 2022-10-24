# Un fabriquant d’outillage de fraisage fabrique deux types de fraises : A et B. 
# Les fraises de type A se vendent 300 l’unité, et se fabrique à avec 1 unité d’acier,
#  2 unités de carbure amovible et 1 unité de diamant synthétique. 
#  Les fraises de type B se vendent 200 l’unité, et se fabrique à avec 2 unité d’acier, 
#  1 unités de carbure amovible et 1 unité de diamant synthétique. 

# Les stocks sont de 50 unités d’acier, 50 unités de carbure et 20 unités de diamant. 
# Le fabriquant souhaite construire au moins 5 fraises de type A et 5 fraises de type B. 
# Le coût d’entretien de l’usine est de 2500.

#  Comment le fabriquant doit-il répartir sa production pour maximiser son profit, est-ce rentable ?


    # Fonction objectif : z = 300A+200B-2500
    # Contraintes :
    #     A+2B  ≤ 5
    #     2A+B ≤ 5
    #     A+B ≤ 2
    #     A  ≥ 5
    #     B  ≥ 5


# Importer la librairie Pulp 
import pulp 
  
# Créer un programme linéaire de maximisation
model = pulp.LpProblem("Maximiser le profit", pulp.LpMaximize)
  
# Créer les variables du problème 
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')
  
# Function économique objectif
model += 300 * A + 200 * B - 2500, "Profit"

# Contraintes
model += 1 * A + 2 * B <= 50
model += 2 * A + 1 * B <= 50
model += 1 * A + 1 * B <= 20
model += 1 * A  >= 5
model += 1 * B >= 5
  
# Résoudre le problème
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print ("Production of  A = {}".format(A.varValue))
print ("Production of  B = {}".format(B.varValue))
  
# Print our objective function value
print (pulp.value(model.objective))


# Production of  A = 15.0
# Production of  B = 5.0
# 3000.0
