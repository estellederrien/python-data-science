# https://towardsdatascience.com/fun-with-the-binomial-distribution-96a5ecabf65b

# Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" L'employé typique d'un centre d'appels effectue en moyenne 50 appels par jour.
    La probabilité d'une conversion (achat) pour chaque appel est de 4%.
    Le revenu moyen de votre entreprise pour chaque conversion est de 100 euros.
    Le centre d'appels que vous analysez compte 100 employés.
    Chaque employé reçoit 200 Euros par jour de travail. 
"""

""" 
Nous pouvons considérer chaque employé comme une variable aléatoire à distribution binomiale avec les paramètres suivants:

    n = 50

    p = 4% 
    
"""

# ***** Quelle est la probabilité de profit pour l'entreprise, sur une journée ? *****
# ***** Les profits peuvent être négatifs parfois ! *****

# Simulation du centre d'appels

# Nombre d'employés à simuler :
employes = 100

# Salaire par employé par jour de travail, en euros 
salaire = 200

# Nombre d'appels indépendants paassés par l'employé, par jour
n = 50

# Probabilité de succès (achat) pour chaque appel
p = 0.04

# Gain pour un appel gagnant, en euros
gain = 100

# On exécute la loi binomiale sur nos paramêtres précéndents ...
conversions = np.random.binomial(n, p, size=employes)

# Imprimer les métriques importants de notre centre d'appels, certains jours on gagne, d'autres on perds ...
print('Taux de Conversion moyen par employé : ' + str(round(np.mean(conversions), 2)))
print('Standard Deviation of Conversions per Employee: ' + str(round(np.std(conversions), 2)))
print('Total des conversions: ' + str(np.sum(conversions)))
print('Total des gains: ' + str(np.sum(conversions)*gain))
print('Total des salaires : ' + str(employes*salaire))
print('Total du Profit: ' + str(np.sum(conversions) * gain - employes * salaire))