""" 

    Loi géométrique ou de pascal - Python géométric law with numpy

    https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.geometric.html

    !!!  Merci à https://stackoverflow.com/users/4238408/quang-hoang  pour l'aide !!!

 """

 # Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problème : 
"""  
Les produits fabriqués par une machine ont un taux de défectueux de 3%. 

Quelle est la probabilité que le cinquième élément soit deffectueux et inspecté ?

"""

result = (np.random.geometric(0.3, size=1000)==5).mean()
print("Le pourcentage de découvrir qu'un produit est défectueux est de ",result * 100, "%");



