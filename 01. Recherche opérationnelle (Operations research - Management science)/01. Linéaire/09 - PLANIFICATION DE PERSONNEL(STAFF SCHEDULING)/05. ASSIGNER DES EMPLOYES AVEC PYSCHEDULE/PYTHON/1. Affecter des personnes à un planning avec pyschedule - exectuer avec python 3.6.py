
# Installer python 3.6 pour windows (3.8 pas compatible pour l'instant)

# Pour exécuter le fichier : 

# py -3.6 lenomdufichier.py


from pyschedule import Scenario, solvers, plotters, alt


# On crée un scénario , la période est en heures dans ce cas
S = Scenario('emploiDeMaison',horizon=10)

# 2 ressources: Alice et Bob
Alice, Bob = S.Resource('Alice'), S.Resource('Bob')

# 3 tâches: cuisiner, nettoyer, and polir
# length : durée en heure, delay_cost = cout
cuisiner = S.Task('cuisiner',length=1,delay_cost=1)
nettoyer = S.Task('nettoyer',length=2,delay_cost=1)
polir = S.Task('polir',length=3,delay_cost=2)



# chaque tache peut être réalisée par Alice ou Bob
cuisiner += Alice | Bob
nettoyer += Alice | Bob
polir += Alice | Bob

# Résoudre et imprimer l'ordonnacement des tâches 
solvers.mip.solve(S,msg=1)
print(S.solution())


# Résultat
# INFO: execution time for solving mip (sec) = 0.04697251319885254
# INFO: objective = 1.0
# [(cuisiner, Alice, 0, 1), (polir, Bob, 0, 3), (nettoyer, Alice, 1, 3)]

# Ca veut dire que Alice cuisine de 0h à 1h Bob polit de 0h à 3h et Alice nettoyer de 1h à 3h

# plotters.matplotlib.plot(S,img_filename='pics/household.png')

