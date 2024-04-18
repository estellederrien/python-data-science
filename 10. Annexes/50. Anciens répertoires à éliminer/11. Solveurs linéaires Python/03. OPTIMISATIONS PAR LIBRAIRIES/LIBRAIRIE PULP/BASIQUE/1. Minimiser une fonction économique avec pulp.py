# Minimiser :  Z = 3x + 5y
# Sous les contraintes : 
# 2x + 3y >= 12
# -x + y <= 3
# x >= 4
# y <= 3
# x, y >= 0


# Importer la librairie Pulp sous le pseudo p
import pulp as p 
  
# Créer un programme linéaire de minimisation
Lp_prob = p.LpProblem('Problem', p.LpMinimize)  
  
# Créer les variables du problème 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
  
# Ecrire la fonction objectif
Lp_prob += 3 * x + 5 * y    
  
# Les contraintes : 
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3
  
# Afficher le problème
print(Lp_prob) 
  
status = Lp_prob.solve()   # Exécuter le solver
print(p.LpStatus[status])   # Le statut de la solution
  
# PAfficher la solution :
print(p.value(x), p.value(y), p.value(Lp_prob.objective))   

# LES SOLUTIONS POUR MINIMISER la fonction économique Lp_prob sont x=6.0 et y=0.0
