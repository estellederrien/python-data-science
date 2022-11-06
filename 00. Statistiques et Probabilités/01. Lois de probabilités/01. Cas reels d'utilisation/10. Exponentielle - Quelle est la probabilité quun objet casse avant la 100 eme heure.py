""" 

    Loi exponentielle de paramêtre lambda.

   Source :
   YVAN MONKA 
   https://www.youtube.com/watch?v=ZS_sW8yq-94&list=LLbfwcLDelivztPdafMQ42WQ&index=5&t=0s

   STANFORD
   http://web.stanford.edu/class/archive/cs/cs109/cs109.1192/handouts/pythonForProbability.html

	Merci à 
	https://stackoverflow.com/users/67579/willem-van-onsem
	pour la correction SCIPY 
 """

 # Problème : 
"""  
La durée de vie, en heures, d'un composant électronique est une variable aléatoire 
qui suit une loi exponentielle de paramètre Lambda =  0.0035

1. Quelle est la probabilité qu'il casse avant 100 heures ?

Formule : P(X < 100) = 1 - e ** -0.0035 * 100 = 0.3 = 30%

2. Quelle est sa durée moyenne de vie ?

Formule : 1 \ 0.0035 = 286 heures

"""

 # Import des librairies
from scipy import stats
import math   # This will import math module

# CALCUL PRIMAIRE AVEC LA LIB MATH

lambdaCalcul = - 0.0035 * 100
MaProbabiliteExponentielle = 1 - math.exp(lambdaCalcul)

print("J'ai calculé avec un calcul primaire ma probabilité ",MaProbabiliteExponentielle * 100 , "%");

# J'ai calculé avec un calcul primaire ma probabilité  29.531191028128656 %


# ESSAI DE CALCUL AVEC SCIPY =
#  This example declares B∼Exp(λ=0.0035)

B = stats.expon(scale=1/0.0035)   # Merci https://stackoverflow.com/users/67579/willem-van-onsem pour le scale !
print(B.pdf(1))       # f(1), the probability density at 1
print(B.cdf(100))     # F(2) which is also P(B < 100) -> Voici ma probabilité
print(B.rvs())        # Get a random sample from B


# B.cdf(100) = 0.2953119102812866
