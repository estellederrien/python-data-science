# On a 4 usines et on veut maximiser le nombre de voitures produites.
# CODE A VERIFIER

""" Voici les ressources employées pour produire une voiture identique
        Main d'oeuvre  materiel  pollution
usine x  2 heures           5         15
usine y  3 heures           6         10
usine z  4 heures           5         9
usine k  3 heures           2         7

On doit produire au minimum 100 voitures à l'usine z selon le directeur.
On a 3300 heures de travail disponible au total, et 4000 unités de matériel disponible.
On a le droit a 12000 unités de pollution.
Au final, on veut maximiser le nombre de voitures produites . """


# Importer la librairie Pulp sous le pseudo p
import pulp as p 
  
# Créer un programme linéaire de minimisation
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
# Créer les variables du problème 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
z = p.LpVariable("z", lowBound = 0)   # Create a variable z >= 0 
k = p.LpVariable("k", lowBound = 0)   # Create a variable k >= 0 
  
# Ecrire la fonction objectif à maximizer qui nous donne un résultat en nombre de voitures produites par usines .
Lp_prob +=  x + y + z + k 
  
# Les contraintes : 

# L'usine z doit produire au minimum  100 voitures 
Lp_prob +=  z >= 100


# Le nombre total d"heure travaillé est au maximum de 3300 heures, plus le nombre est petit, mieux c'est.
Lp_prob +=  2 * x + 3 * y + 4 * z + 3 * k <= 3300

# Il y  a 4000 unités de matériel disponible au maximum
Lp_prob +=  5 * x + 6 * y + 5 * z + 2 * k <= 4000

# On a le droit à 12 000 unités de pollution maximum, plus le nombre est petit , mieux c'est.
Lp_prob +=  15 * x + 10 * y + 9 * z + 7 * k <= 12000


  
# Afficher le problème
print(Lp_prob) 
  
status = Lp_prob.solve()   # Exécuter le solver
print(p.LpStatus[status])   # Le statut de la solution
  
# Afficher la solution :
print( p.value(x)," Voitures produites dans l'usine x")
print(p.value(y) , " Voitures produites dans l'usine y"  )
print(p.value(z) , " Voitures produites dans l'usine z"  )
print(p.value(k) , " Voitures produites dans l'usine k" )
print(p.value(Lp_prob.objective) ," est le Nombre total optimisé de voitures produites pour 3300 heures de travail" )



