""" 
Calculer l'évolution de la population future avec la loi exponentielle.

Source :

http://www.algebralab.org/lessons/lesson.aspx?file=Algebra_ExponentsApps.xml

"""

import math
import numpy as np
import matplotlib.pyplot as plt

""" 
PROBLEME : 

La population d'une ville est P = 250 342e ^ 0,012 * t où t = 0 représente la population en l'an 2000.

Trouvez la population de la ville en 2010.

Pour trouver la population en 2010, nous devons substituer t par 10 dans notre équation . 


"""

population = 250342
exp = math.exp(0.12)
resultat = population * exp
print(resultat)  
# Affiche 282259.8168180841

# Puisque nous avons affaire à la population d'une ville, nous arrondissons normalement à un nombre entier, en l'occurrence 282 260 personnes.

""" 
Trouvez maintenant la population de la ville en 2015.

Pour retrouver la population en 2015, il substituer t par 15 dans notre équation . 

"""

# P = 250,342e ^ 0.012(15) = 250,342e ^ 0.18 = 299,713.8 

population = 250342
exp = math.exp(0.18)
resultat = population * exp
print(resultat)  
# Affiche 299,713.8 

""" 
Trouvez maintenant quand la population de la ville sera de 320 000 .

Equation :

320000 / 250342  = e0.012 * t

ou , réecrit : 

ln(320000 / 250 342 ) / 0.012 = t

(resultat = t)
"""
population = 250342
prevision = 320000

resultat = math.log(prevision / 250342) / 0.012
print(resultat)


# 20.457751065919258
# Dans 20.45 ans, la population va grandir à 320 000



""" Autres essais """
""" in_array = np.arange(1,320000)
out_array = np.exp(in_array) 

plt.plot(in_array, y, color = 'blue', marker = "*") 

plt.plot(x,y)
plt.show() """