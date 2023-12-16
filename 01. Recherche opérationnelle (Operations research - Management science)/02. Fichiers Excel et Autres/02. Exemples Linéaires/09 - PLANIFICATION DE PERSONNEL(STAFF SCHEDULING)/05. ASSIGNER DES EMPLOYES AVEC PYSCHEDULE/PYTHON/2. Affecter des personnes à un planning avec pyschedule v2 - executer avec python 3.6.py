
# Installer python 3.6 pour windows (3.8 pas compatible pour l'instant)

# Pour exécuter le fichier : 

# py -3.6 lenomdufichier.py


from pyschedule import Scenario, solvers, plotters, alt


# On crée un scénario , la période est en heures dans ce cas
S = Scenario('emploiDeMaison',horizon=10)

# 2 ressources: Alice et Bob
Alice, Bob = S.Resource('Alice'), S.Resource('Bob')

# 3 tâches: cuisiner, nettoyer, and polir

cuisiner = S.Task('cuisiner',1)
nettoyer = S.Task('nettoyer',2)
polir = S.Task('polir',3)

# chaque tache peut être réalisée par Alice ou Bob
cuisiner += Alice | Bob
nettoyer += Alice | Bob
polir += Alice | Bob

# Résoudre et imprimer l'ordonnac
S.use_makespan_objective()
solvers.mip.solve(S,msg=1)
print(S.solution())

# Dans cet exemple, nous utilisons un objectif makespan, 
# ce qui signifie que nous voulons minimiser le temps 
# d'achèvement de la dernière tâche. Par conséquent,
 # Bob devrait faire la cuisine de 0 à 1 puis le lavage de 1 à 3, 
 # tandis qu'Alice ne fera que le nettoyage de 0 à 3. 
 # Cela garantira que les deux sont effectués après trois heures. 
 # Cette représentation du tableau est un peu difficile à lire, 
 # on peut visualiser le plan en utilisant matplotlib:


# Résultat
# INFO: execution time for solving mip (sec) = 0.0533750057220459
# INFO: objective = 3.0
# [(cuisiner, Bob, 0, 1), (polir, Alice, 0, 3), (nettoyer, Bob, 1, 3), (MakeSpan, Alice, 3, 4)]
