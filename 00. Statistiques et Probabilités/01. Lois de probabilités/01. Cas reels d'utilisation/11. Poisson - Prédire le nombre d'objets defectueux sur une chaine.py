
# https://stattrek.com/probability-distributions/poisson.aspx
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

""" Calculer des probabilités de masse OU cumulatives avec la loi de poisson.
1. calculer la probabilité d'avoir EXACTEMENT un résultat-> pmf(k, mu, loc=0)Probability mass function.
2. calculer la probabilité d'avoir MOINS d'un résultat ->  cdf(k, mu, loc=0) Cumulative distribution function.

"""

# Import des librairies
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

"""   

CAS NUMERO 1 

Exemple de distribution de Poisson

Le nombre moyen de logements vendus par la société Acme Realty est de 2 logements par jour. Quelle est la probabilité de vendre exactement 3 maisons demain?

Solution: Il s'agit d'une expérience de Poisson dans laquelle nous savons ce qui suit:

    μ = 2; puisque 2 logements sont vendus par jour, en moyenne.
    x = 3; car nous voulons trouver la probabilité que 3 maisons soient vendues demain.
    e = 2,71828; puisque e est une constante égale à environ 2,71828.

"""


# 1. Quelle est la probabilité qu'il y en ait ***EXACTEMENT*** 3 ventes demain

ma_probabilite =  poisson.pmf(3,2)

print("proba: ", ma_probabilite * 100 , '%')


"""   

CAS NUMERO 2 

Le nombre moyen d'occurrences dans un intervalle de temps fixé est λ

Sur une chaine de production, il y a en moyenne 8 objets défectueux par mois.

donc 96 objets défectueux en moyenne sur 12 mois.

NOTE : CONSERVER TOUJOURS LA MEME UNITE DE TEMPS , LA, CEST DES MOIS DONC ON NE CONVERTIT PAS EN ANNEES APRES !!
DE même, si lambda est basé sur 12 mois, on établit la pb sur les 12 mois suivants .
"""

# 1. Quelle est la probabilité qu'il y en ait ***MOINS *** de 6 défectueux le mois prochain
# donc on ADDITIONNE LES PROBABILITES 
#  P(x < 6, 8) = P(0; 8) + P(1; 8) + P(2; 8) + P(3; 8) + P(4; 8) + P(5; 8) + P(6; 8) 

# On se sert de la function cumulative de SCIPI :
ma_probabilite =  poisson.cdf(6,8)

print("proba: ", ma_probabilite * 100 , '%')
# proba:  31.337427753639773 %

# 2. Quelle est la probabilité qu'il y en ait moins de 50 objets defectueux dans les 12 mois suivants.
#  P(x < 50, 96) = P(0; 96) + ....+ P(50; 96) 
ma_probabilite =  poisson.cdf(90,96)
# proba:  29.128520883025814 %

print("proba: ", ma_probabilite * 100 , '%')


"""   

CAS NUMERO 3 

Exemple de Poisson cumulé

Supposons que le nombre moyen de lions vus lors d'un safari d'une journée soit de 5. 
Quelle est la probabilité que les touristes voient moins de quatre lions lors du prochain safari d'une journée?

Solution: Il s'agit d'une expérience de Poisson dans laquelle nous savons ce qui suit:

    μ = 5; puisque 5 lions sont vus par safari, en moyenne.
    x = 0, 1, 2 ou 3; car nous voulons trouver la probabilité que les touristes voient moins de 4 lions; c'est-à-dire que nous voulons la probabilité qu'ils voient 0, 1, 2 ou 3 lions.
    e = 2,71828; puisque e est une constante égale à environ 2,71828.

Pour résoudre ce problème, nous devons trouver la probabilité que les touristes voient 0, 1, 2 ou 3 lions. Ainsi, nous devons calculer la somme de quatre probabilités: P (0; 5) + P (1; 5) + P (2; 5) + P (3; 5). Pour calculer cette somme, nous utilisons la formule de Poisson:


"""

# On se sert de la function cumulative de SCIPI :
ma_probabilite =  poisson.cdf(3,5)
print("proba: ", ma_probabilite * 100 , '%')
# proba:  44.049328506521256 % 


# Quelle est la probabilité que les touristes voient moins de 15 lions lors du prochain safari d'une journée?
ma_probabilite =  poisson.cdf(15,5)
print("proba: ", ma_probabilite * 100 , '%')
# proba:  99.99309917581444 % Normal, il ne peuvent pas voir plus de 15 lions alors que la moyenne est de 5 lions

# Les variables random montrent qu'on ne voit évidemment jamais 15 lions, sur 50 jours différents alors que la moyenne est de 5 !'
ma_probabilite =  poisson.rvs(5,size=50)
print("proba: ", ma_probabilite )
""" proba:  [ 7  5  6  7  7  7  4  2  6  8  1  2  5  4  2  5  6  4  4  2  6  1  4  1
  2  3  7  6  6  3  6  5  7  2  6  7 10  7  6  6  5  5  4  7  8  4  1 10
 14  4] """

