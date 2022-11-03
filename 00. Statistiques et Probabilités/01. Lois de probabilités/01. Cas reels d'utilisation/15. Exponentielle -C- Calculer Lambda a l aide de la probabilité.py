""" 

Source : EICNAM 
U.E : RCP 103 
LA LOI EXPONENTIELLE / LOI CONTINUE

Trouver la valeur de λ Lambda, à l'aide d'une probabilité déjà donnée'. 

Autre excellent lien : 
http://www.jaicompris.com/lycee/math/probabilite/loi-exponentielle.php
http://www.jybaudot.fr/Probas/propriexpo.html

"""

import math

# ** TROUVER λ GRACE AU TEXTE **
# Le temps d'attente exprimé en minutes au guichet d'une banque est une variable aléatoire T
# suivant la loi exponentielle de paramètre λ  (lambda). 
# On sait que la probabilité qu'un client attende moins de 8 minutes 
# est égale à 0.7 (Ou de 70 %)

""" 
1. Calculer une valeur approchée à 0.0001 de λ  (lambda). 
-> ON a P(T <= 8) = 0,7 
donc on substitue à l'aide de notre formule du fichier 13 :
 1 - e ^-8λ = 0.7
 ce qui fait e ^-8λ = 0.3 (qui est la pb inverse) et donc 
λ = ln(0.3) / -8 = 0.1505
"""

LAMBDA = math.log(0.3) / -8
print(LAMBDA)
# 0.15049660054074201

# 2. Maintenant que tu as trouvé LAMBDA, calcule la probabilité qu'un client attende entre 15 et 20 minutes.
# On se sert de la formule du fichier numéro 13 .
# P(15<=T<=20) = e ^ -0.1505 * 15 - e ^ -01505 * 20 = 0.055

probabilite =  math.exp( -0.1505 * 15 ) - math.exp( -0.1505 * 20 )
print(probabilite)
# 0.05532000857337062
