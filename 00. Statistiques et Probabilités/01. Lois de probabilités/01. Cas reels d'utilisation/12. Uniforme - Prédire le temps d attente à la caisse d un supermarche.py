
""" 

Énoncé (d'après un exercice de bac)


Dans un supermarché, le temps d'attente X à la caisse, exprimé en minutes, suit la loi uniforme sur l'intervalle [1;11]

1) Déterminer la fonction de densité de probabilité f de la loi de X.

2) Quelle est la probabilité que le temps d'attente soit compris entre trois et cinq minutes ?

3) Quelle est la probabilité qu'un client attende plus de huit minutes à la caisse ?

4) Préciser le temps d'attente moyen à la caisse.

Liens : 
https://www.profexpress.com/soutien-scolaire/mathematiques/exercices-en-ligne/110
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html
http://mathematiques.daval.free.fr/IMG/pdf/s19_cours_loi_uniforme_tes.pdf

"""


# 1. Déterminer la fonction de densité de probabilité f de la loi de X.
debut = 1
fin = 11

fx = debut / (fin - debut)

print("Densité: ", fx  )

#  2. Quelle est la probabilité que le temps d'attente soit compris entre trois et cinq minutes ? p(3=< X =< 5)

min = 3
max = 5
intervalle = 10

probabilite = (max - min) / intervalle
print("Probabilité: ", probabilite * 100, " %" )
# Probabilité:  20.0  %

#  3. Quelle est la probabilité qu'un client attende plus de huit minutes à la caisse : P(x>8)?
min = 8
max = 11
intervalle = 10

probabilite = (max - min) / intervalle
print("Probabilité: ", probabilite * 100, " %" )
# Probabilité:  30.0  %

# 4) Préciser le temps d'attente moyen à la caisse. a+b / 2

debut = 1
fin = 11

esperance = (debut + fin) / 2

print("Espérance: ", esperance, "  minutes" )


