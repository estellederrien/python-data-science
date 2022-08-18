from gekko import GEKKO
m = GEKKO(remote=False) # Initialize gekko sans faire appel au serveur, en local

# Use IPOPT solver (default)
m.options.SOLVER = 3

# Change to parallel linear solver
# m.solver_options = ['linear_solver']
# Explication : SOLVER sélectionne le solveur à utiliser pour tenter de trouver une solution. 
# Il existe des solveurs gratuits : 1 : APOPT, 2 : BPOPT, 3 : IPOPT distribués avec la version publique du logiciel.
#  Il existe des solveurs supplémentaires qui ne sont pas inclus dans la version publique et nécessitent 
#  une licence commerciale. IPOPT est généralement le meilleur pour les problèmes avec un grand nombre 
#  de degrés de liberté ou lors d'un démarrage sans une bonne estimation initiale. BPOPT s'est avéré être 
#  le meilleur pour les applications de biologie des systèmes. APOPT est généralement le meilleur lors 
#  d'un démarrage à chaud à partir d'une solution précédente ou lorsque le nombre de degrés de liberté 
#  (nombre de variables - nombre d'équations) est inférieur à 2000. APOPT est également le seul solveur 
#  qui gère les problèmes d'entiers mixtes. Utilisez l'option 0 pour comparer tous les solveurs disponibles.
#   Certains solveurs et options de solveur ne sont pas disponibles lors du passage à remote=False
#    en raison des exigences de licence. Il existe des informations supplémentaires sur les options du solveur.




# Initialiser variables
x1 = m.Var(value=1,lb=1,ub=5) # value est la valeur par défaut lb veut dire lower bound, ub veut dire upper bound 
x2 = m.Var(value=5,lb=1,ub=5)
x3 = m.Var(value=5,lb=1,ub=5)
x4 = m.Var(value=1,lb=1,ub=5)

# Equations
m.Equation(x1*x2*x3*x4>=25)
m.Equation(x1**2+x2**2+x3**2+x4**2==40) # ** veut dire 'puissance de '

# fonction Objectif
m.Obj(x1*x4*(x1+x2+x3)+x3) 
m.options.IMODE = 3 # Steady state optimization

m.solve(disp=False) # Solve

# Affichage des resultats 
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))
print('Objective: ' + str(m.options.objfcnval))