# Minimiser :  Z = 84u + 24w
# Sous les contraintes : 
# 4u + 2w >= 6
# 8u + 2w >= 8
# u, w >= 0


# Importer la librairie Pulp sous le pseudo p
import pulp as p 
  
# Créer un programme linéaire de minimisation
Lp_prob = p.LpProblem('Problem', p.LpMinimize)  
  
# Créer les variables du problème 
u = p.LpVariable("u", lowBound = 0)   # Create a variable u >= 0 
w = p.LpVariable("w", lowBound = 0)   # Create a variable w >= 0 
  
# Ecrire la fonction objectif
Lp_prob += 84 * u + 24 * w   
  
# Les contraintes : 
Lp_prob += 4 * u + 2 * w >= 6
Lp_prob += 8 * u + 2 * w >= 8

# Afficher le problème
print(Lp_prob) 
  
status = Lp_prob.solve()   # Exécuter le solver
print(p.LpStatus[status])   # Le statut de la solution
  
# PAfficher la solution :
print(p.value(u), p.value(w), p.value(Lp_prob.objective))   

# LES SOLUTIONS POUR MINIMISER la fonction économique Lp_prob sont x=6.0 et y=0.0
