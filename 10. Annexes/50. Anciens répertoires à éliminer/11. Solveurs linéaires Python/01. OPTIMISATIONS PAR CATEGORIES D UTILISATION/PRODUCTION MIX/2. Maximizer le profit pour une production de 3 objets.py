# Maximiser notre profit sous les contraintes de production .

# On vends 

# 1 mixeur à purée qui coute 10.5 euros.
# 1 batteur à gateau qui coute 8.5 euros.
# 1 Ventilateur qui coute 18.5 euros.

# 3 employés sont sur les chaines de travail .
# Temps de travail pour le mixeur : 3h 
# Temps de travail pour le batteur : 3h
# Temps de travail pour le ventilateur : 2h
# Les employés travaillent 35 h * 4 semaines par mois, soit 140h soit, pour les 3 420 heures au total

# Il faut produire au minimum 100 mixeurs , 10 batteurs et 10 ventilateurs par mois pour les fournisseurs.

# Maximiser  :  Z = 10.5x + 8.5y + 18.5z
# Sous les contraintes : 
# 1x + 1.5y + 2z <= 140
# x  >= 100 et x >= 0 
# y  >= 10  et y >= 0 
# z  >= 10  et z >= 0 

# Importer la librairie Pulp sous le pseudo p
import pulp as p 
  
# Créer un programme linéaire de minimisation
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
# Créer les variables du problème 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
z = p.LpVariable("z", lowBound = 0)   # Create a variable z >= 0 
  
# Ecrire la fonction objectif à maximizer qui nous donne un résultat en Euros 
Lp_prob +=  10.5 * x + 8.5 * y + 18.5 * z
  
# Les contraintes : 

# Heures de travail au mois , plus il est grand, plus le prfoit augmente, moins le temps de travail sur un objet est long, plus on en produit et le profit augmente 
Lp_prob += 3 * x + 3 * y + 2 * z <= 420

# Il faut produire au minimum ce nombre d'éléments  :
Lp_prob += x  >= 100
Lp_prob += y  >= 10
Lp_prob += z  >= 10
  
# Afficher le problème
print(Lp_prob) 
  
status = Lp_prob.solve()   # Exécuter le solver
print(p.LpStatus[status])   # Le statut de la solution
  
# Afficher la solution :
print( p.value(x)," de Mixeurs à produire")
print(p.value(y) , "de  Batteurs à produire"  )
print(p.value(z) , "de Ventilateurs à produire"  )
print(p.value(Lp_prob.objective) ,"Euros de profits " )



