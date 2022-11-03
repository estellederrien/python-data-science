""" 
    Loi binomiale

    https://docs.scipy.org/doc/numpy-1.9.2/reference/generated/numpy.random.binomial.html

    + 
    
    Tous_les_algorithmes_-_Programmation_avec_Algobox_et_Python

 """

# Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problème : 
"""  
Dans une urne, il y a 4 boules rouges, 6 boules vertes et 10 boules noires. 
On tire 5 fois avec remise une boule dans l'urne.
A chauqe étape, on considère comme succès qu'une boule verte apparaisse.

Les paramêtres de la loi binomiale sont donc : n = 5 et p = 6/20 = 0.3


On répéte les 5 tirages 100 fois. 

"""

# On exécute la loi binomiale sur nos paramêtres précéndents ...
resultat = np.random.binomial(5, 0.3,100)

print(resultat);

""" [2 1 2 3 2 0 1 2 2 2 1 1 4 1 1 1 1 2 2 3 1 2 2 0 4 1 2 2 3 3 1 1 0 2 1 1 1
 1 1 1 2 1 1 1 1 2 1 2 0 0 3 1 0 1 1 1 3 0 1 1 3 2 2 3 4 3 1 2 0 2 2 2 1 2
 1 1 3 3 1 1 0 1 2 1 1 2 2 1 0 1 1 3 2 0 0 4 1 1 1 2] """

#  Ce tableau veut dire : la première répétition, on a eu 2 boules vertes sur les 5 essais, 
# la seconde répétition, on a eu 1 boule verte sur les 5 essais; la 3 ème répétition, 
# on a eu 2 boules vertes sur les 5 essais, 
# le 4ème répétiton on a 3 boules vertes sur les 5 essais etc pour les 100 répétitions ...

# Il est aléatoire, c'est à dire que si on relance le programme, 
# on aura pas trop les même chiffres, mais si on répéte la loi 100000 fois, 
# la loi des grands nombres fait qu'on se rapproche d'une stat globale.

# Maintenant, on va faire 1000 répétitions des 5 tirages et calculer la probabilité d'obtenir zéro boules vertes

resultat  = sum(np.random.binomial(5,0.3,1000)==0)/1000.
print("La chance d'avoir zéro boules vertes est de ",resultat * 100 ,"%");

# réponse  = 0.195, ou 19.5 %

# Maintenant, on va faire 1000 répétitions des 5 tirages et calculer la probabilité d'obtenir au moins 3 boules vertes

resultat  = sum(np.random.binomial(5,0.3,1000) >=  3)/1000.
print("La chance d'avoir au moins 3 boules vertes est de ",resultat * 100 ,"%");

# réponse  = 0.169, ou 16.9 %

# Maintenant, on va faire 1000 répétitions des 5 tirages et calculer la probabilité d'obtenir  5 boules vertes

resultat  = sum(np.random.binomial(5,0.3,1000) ==  5)/1000.
print("La chance d'avoir 5 boules vertes est de ",resultat * 100 ,"%");

# réponse  = 0.002, ou 0.2 %


