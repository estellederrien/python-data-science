

# Importer la librairie Pulp 
import pulp 
  
# Créer un programme linéaire de maximisation
model = pulp.LpProblem("Maximize", pulp.LpMaximize)
  
# Créer les variables du problème 
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
  
# Function économique objectif
model +=  2 * x1 + 1 * x2, "Profit"

# Contraintes
model += 2 * x1 + 3 * x2 <= 800
model += 2 * x1 + x2 <= 500

# Résoudre le problème
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print ("x1 = {}".format(x1.varValue))
print ("x2 = {}".format(x2.varValue))
  
# Print our objective function value
print (pulp.value(model.objective))

