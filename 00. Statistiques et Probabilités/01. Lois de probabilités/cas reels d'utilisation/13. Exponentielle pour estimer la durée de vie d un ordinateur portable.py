""" 

Source : EICNAM 
U.E : RCP 103 
LA LOI EXPONENTIELLE / LOI CONTINUE


Soit X une variable aléatoire suivant la loi exponentielle de paramètre λ (se dit "lambda"), 
et a et b deux réels positis ou nuls, alors on a : 

P(X<=a) = 1 - ⅇ ^-λa
-> Veut dire " La probabilité que la variable aléatoire soies inférieure à a est égale à : 1 - exponentielle ^ -λ * a.

P(X>=a) = ⅇ ^-λa
-> Veut dire " La probabilité que la variable aléatoire soies supérieure ou égale  à : exponentielle ^ -λ * a.

P(a <= X <= b) = ⅇ ^-λa  - ⅇ ^-λb
-> Veut dire " La probabilité que la variable aléatoire soies comprise entre a et b est égale  à : exponentielle ^ -λ * a - exponentielle ^ -Λ * b.

E(x) = 1 /λ
-> Veut dire l'espérance de la probabilité de x est de 1 divisé par lambda  
-> Cela permet de calculer Λ, car souvent, on nous donne une durée de vie moyenne (E(x)).


La distribution exponentielle est la seule distribution continue qui possède la propriété sans mémoire.
Pour tout t >= 0 et tout a >= 0 On a P X>=a(X>=a+t) = P(X>=t) 
Autrement dit, on ne tient pas pas compte de a (qui représente Le passé) 
Le passé n'influe pas sur le futur.

Λ (SE DIT LAMBDA) se lit en lisant la valeur de l'ordonnée sur le schéma.

Autre excellent lien : 
http://www.jaicompris.com/lycee/math/probabilite/loi-exponentielle.php
http://www.jybaudot.fr/Probas/propriexpo.html

"""

import math

# La durée de vie d'un ordi portable exprimée en années est une variable aléatoire X suivant la loi exponentielle de paramètre Λ = 0.125
# La probabilité que la vie de cet ordi  dépasse 5 ans est :
# p(x > 5) = e ^ - 0.125 * 5

pb = math.exp(- 0.125 * 5 )   
print(pb)
# 0.5352614285189903

# La durée de vie d'un ordi portable exprimée en années est une variable aléatoire X suivant la loi exponentielle 
# de paramètre λ = 0.125
# La probabilité que la vie de cet ordi soit inférieure à 3 ans est :
# p(x <= 3) = 1 - e ^ 0.125 * 3

pb = 1 - math.exp(- 0.125 * 3 )   
print(pb)
# 0.31271072120902776

# La durée de vie d'un ordi exprimée en années est une variable aléatoire X suivant la loi exponentielle de paramètre λ = 0.125

""" Quelle est la pb que la durée de vie de cet ordinateur portable dépasse 5 ans sachant qu'il fonctionne déjà depuis 2 ans ? """

# -> On ne s'occupe pas des 2 ans, car pas de mémoire
# P x<=2(X>=5) = P(X>=3) = e ^ -0.125*3 = 0.687

pb = math.exp(- 0.125 * 3 )   
print(pb)
# 0.6872892787909722