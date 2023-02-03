""" Source :

'Apprendre le Machine Learning' de Guillaume Saint-Cirgue.

https://machinelearnia.com/a-propos/ 
"""

import numpy as np   
import matplotlib.pyplot as plt   
from sklearn.datasets import make_regression  
from sklearn.linear_model import SGDRegressor 


# Créer un Dataset 
np.random.seed(0)   
x, y = make_regression(n_samples=100, n_features=1, noise=10)   
plt.scatter(x, y)
plt.show()

# Développer le modèle et l’entraîner 
model = SGDRegressor(max_iter=100, eta0=0.0001)   
model.fit(x,y)   
print('Coeff R2 =', model.score(x, y))   
plt.scatter(x, y)   
plt.plot(x, model.predict(x), c='red', lw = 3) 
plt.show()

# Re-Développer le modèle et l’entraîner afin d'obtenir une meilleure régression linéaire .
model = SGDRegressor(max_iter=1000, eta0=0.001)   
model.fit(x,y)   
print('Coeff R2 =', model.score(x, y))   
plt.scatter(x, y)   
plt.plot(x, model.predict(x), c='red', lw = 3) 
plt.show()

# 𝑅2 = 94%


# Pour rappel: la méthode la plus simple pour réaliser une régression est décrite dans le numéro 1