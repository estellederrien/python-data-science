""" 

Résoudre un programme linéaire comprenant 2 objectifs .

Source Copyright : 
http://www.supplychaindataanalytics.com/multi-objective-linear-optimization-with-pulp-in-python/


On a ce p.l avec 2 objectifs différents:

max (x1,x2) 2x1 + 3x2
max (x1,x2) 4x1 - 2x2

Sous les contraintes : 
x1 + x2 <=  10
2x1 + x2 <=  15
x1,x2 >= 0
x1,x2 appartient à R 

"""
""" 
En supposant que dans l'énoncé du problème ci-dessus, les deux fonctions objectives représentent deux objectifs différents, tels que par ex. niveau de service et marge bénéficiaire de certains portefeuilles de produits, je teste deux approches alternatives pour résoudre ce problème.

La première approche consistera à résoudre l'un des objectifs, puis à fixer le problème au résultat optimal de ce premier problème en ajoutant une contrainte supplémentaire à un deuxième cycle d'optimisation où je maximiserai ensuite la deuxième fonction objectif (sous la contrainte de garder la valeur objective optimale pour le premier sous-problème).

La deuxième approche consistera à additionner les deux objectifs ensemble, c'est-à-dire à les fusionner en une seule fonction objectif en appliquant des pondérations. En échantillonnant les poids et en résolvant le problème combiné pour chaque poids échantillonné, le résultat optimal peut être examiné en fonction des poids.
Approche 1: Maximiser pour un objectif, puis l'ajouter en tant que contrainte et résoudre l'autre objectif

En utilisant PuLP, je maximise d'abord le premier objectif, puis j'ajoute cette fonction objectif en tant que contrainte au problème d'origine et maximise le deuxième objectif soumis à toutes les contraintes, y compris cette contrainte supplémentaire.

Dans la syntaxe mathématique, le problème que nous résolvons en premier peut être énoncé comme suit:

 """

# import PuLP
import pulp

# C'est une maximizaiton
linearProblem = pulp.LpProblem("Maximizing for first objective",pulp.LpMaximize)

# Déclarer les variables de décision
x1 = pulp.LpVariable("x1",lowBound = 0) 
x2 = pulp.LpVariable("x2",lowBound = 0) 

# Ajouter la première fonction objectif
linearProblem += 2*x1 + 3*x2 

# Ajouter les contraintes
linearProblem += x1 + x2 <= 10
linearProblem += 2*x1 + x2 <= 15

# Résoudre avec le solver par défaut 
solution = linearProblem.solve()

# Imprimer l'info si l'optimum a été trouvé, la valeur max de l'objectif
# output information if optimum was found, what the maximal objective value is and what the optimal point is
print(str(pulp.LpStatus[solution])+" ; max value = "+str(pulp.value(linearProblem.objective))+
      " ; x1_opt = "+str(pulp.value(x1))+
      " ; x2_opt = "+str(pulp.value(x2)))
# Réponse : Optimal ; max value = 30.0 ; x1_opt = 0.0 ; x2_opt = 10.0


""" Maintenant, je reformule le problème original de telle sorte que la deuxième fonction objectif 
soit maximisée sous réserve d'une contrainte supplémentaire. Cette contrainte supplémentaire 
demande que le premier objectif soit d'au moins 30. En utilisant la syntaxe mathématique, 
le problème que je résous maintenant peut être énoncé comme suit:


max (x1,x2) 4x1 - 2x2

Sous les contraintes : 
x1 + x2 <=  10
2x1 + x2 <=  15
2x1 + 3x2 >= 30 // On reconnait bien la première contrainte et son résultat , qu'on ajoute dans ce nouveau programme linéaire
x1,x2 >= 0
x1,x2 appartient à R 



 """
# remodel the problem statement
linearProblem = pulp.LpProblem("Maximize second objective",pulp.LpMaximize)
linearProblem += 4*x1 - 2*x2
linearProblem += x1 + x2 <= 10
linearProblem += 2*x1 + x2 <= 15
linearProblem += 2*x1 + 3*x2 >= 30

# review problem statement after remodelling
""" linearProblem

Maximize_second_objective:
MAXIMIZE
4*x1 + -2*x2 + 0
SUBJECT TO
_C1: x1 + x2 <= 10

_C2: 2 x1 + x2 <= 15

_C3: 2 x1 + 3 x2 >= 30

VARIABLES
x1 Continuous
x2 Continuous """

# Maintenant, je résous ce problème, en utilisant le solveur par défaut dans PuLP:
# apply default solver
solution = linearProblem.solve()

# output a string summarizing whether optimum was found, and if so what the optimal solution 
print(str(pulp.LpStatus[solution])+" ; max value = "+str(pulp.value(linearProblem.objective))+
      " ; x1_opt = "+str(pulp.value(x1))+
      " ; x2_opt = "+str(pulp.value(x2)))

#Optimal ; max value = -19.999999999995993 ; x1_opt = 1.0018653e-12 ; x2_opt = 10.0

# This approach suggests that x1 = 0 and x2 = 10 is the the optimal solution. 
# The optimal objective values would be 30 for objective one, and -20 for objective two.