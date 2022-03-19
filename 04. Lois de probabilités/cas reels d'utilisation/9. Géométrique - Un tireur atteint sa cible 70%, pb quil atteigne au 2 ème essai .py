""" 

    Loi géométrique ou de pascal - Python géométric law with numpy

    https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.geometric.html

 """

 # Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problème : 
"""  
Un tireur atteint sa cible 70 % du temps , 

Quelle est la probabilité qu'il l'atteigne au 2ème coup ?

Formule P(X = x) = q  **x-1 * p


"""

# P(X=2) = 0.3 **1 * 0.7 = 0.21
result = (np.random.geometric(0.7, size=1000)==2).mean()
print("Le pourcentage qu'il atteigne sa cible au bout du deuxième coup est de  ",result * 100, "%");


# Trouver la moyenne et l'écart type
# M = 1/p  = 1/0.7 = 1.43

# Ecart type = racine de 2 sur p au carré 
# = 0.3 / 0.7 ** 2 = 0.78
