""" 

Source : EICNAM / Kamel Barkaoui
U.E : RCP 103 
LA LOI UNIFORME / LOI CONTINUE

Prédire le temps d'attente à un arrêt d'autobus.

Note: Voir aussi le fichier 12 pour comparer.
"""

import math

# Dans une ville idéale, les autobus passent à  chaque arrêt exactement toutes les 20 minutes.
# On appelle X le temps d'attente en minutes d'un autobus à un arrêt.
# X est une variable aléatoire suivant une loi uniforme sur l'intervalle [0;20], on a donc :

# La probabilité d'attendre entre 5 et 18 minutes est de  :
# P(5 <= X <= 18) = 18-5 / 20 = 13 /20

min = 5
max = 18
intervalle = 20

probabilite = (max - min) / intervalle
print("Probabilité: ", probabilite * 100, " %" )
# Probabilité: 65 %

# # La probabilité d'attendre plus de 8 minutes est de :
# P( X >= 12 ) = P(12 <= X <= 20) = 20 - 12 / 20 = 8 / 20

min = 12
max = 20
intervalle = 20

probabilite = (max - min) / intervalle
print("Probabilité: ", probabilite * 100, " %" )
# Probabilité: 40 %

