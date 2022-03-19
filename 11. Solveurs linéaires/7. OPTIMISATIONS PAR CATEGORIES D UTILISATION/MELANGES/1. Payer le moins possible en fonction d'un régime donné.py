# Soit 2 aliments x pain et y fromage contenant chacun 2 éléments mesurés en calories et en grammes
# Pain 1000 calories 20 grammes de protéines
# Fromage 2000 calories 80 grammes de protéines
# Le régime alimentaire minimum qui doit être atteint est de 3000 cal et 80g de protéines par jour.
# Le prix du pain est de 1 euros par livre et le prix du fromage est de 2 euros par livre.
# Comment effectuer ses achats pour minimiser sa dépense totale.


# Minimiser  :  Z = 1x + 2y
# Sous les contraintes : 
# 1000x + 2000y <= 3000
# 20x + 80y <= 100
# x, y >= 0


# Importer la librairie Pulp sous le pseudo p
import pulp as p 
  
# Créer un programme linéaire de minimisation
Lp_prob = p.LpProblem('Problem', p.LpMinimize)  
  
# Créer les variables du problème 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
  
# Ecrire la fonction objectif en Euros 
Lp_prob += 1 * x + 2 * y    
  
# Les contraintes : 

# Calories 
Lp_prob += 1000 * x + 2000 * y >= 3000 

# Protéines : Il faut manger au minimum  
Lp_prob += 20 * x + 80 * y >= 80

  
# Afficher le problème
print(Lp_prob) 
  
status = Lp_prob.solve()   # Exécuter le solver
print(p.LpStatus[status])   # Le statut de la solution
  
# Afficher la solution :
print( p.value(x)," euros de pain")
print(p.value(y) , " euros de fromage"  )
print(p.value(Lp_prob.objective) ," de somme principale en euros, cette somme est la somme minimale à payer pour satisfaire à nos objectifs de 3000 calories et 80 de protéines, si on change les objectifs, la somme minimum change également " )



