# Import des librairies
import numpy as np

#  Une entreprise fore 9 puits d'exploration pétrolière , 
#  chacun avec une probabilité de réussite estimée à 0,1. 
#  Les neuf puits échouent. Quelle est la probabilité que cela se produise ?

# Faisons 20 000 essais du modèle et comptons le nombre qui ne génère aucun résultat positif.


maVariable = sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.

print(maVariable*100,'%')

# réponse = 0.38885, or 38%.

