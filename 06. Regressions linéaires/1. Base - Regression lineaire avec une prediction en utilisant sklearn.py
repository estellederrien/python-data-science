
""" 

Réaliser une prédiction unique à l'aide d'une régression linéaire sur un dataset X , Y.

on peut aussi réaliser un tableau de prédictions.

****** Code le plus simplifié possible, sans import EXCEL préalable. *****

On nous donne une valeur X, on peut alors prédire la valeur Y, par ce que l'on connait les ANCIENNES VALEURS dans le temps, et que SKLEARN 

dispose de l'algo de régression linéaire .

# Sources
https://www.geeksforgeeks.org/linear-regression-python-implementation/
https://stackoverflow.com/questions/50090767/single-prediction-with-linear-regression

"""

# 1. On charge les librairies
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. On charge nos données en abscysse et ordonnées
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# 2. On appelle le script de regression .
model = LinearRegression()

# 3. On entraine notre modèle, qui est tout petit, donc pas fiable, mais c'est pour l'exemple.
model.fit(x, y)

# 4. On veut prédire notre valeur y, en lui fournissant une valeur x (Super pour les scripts d'apps webs): 
print(model.predict([[2000]]))

# 5. On veut prédire nos valeurs y, en lui fournissant plusieurs valeurs x : 
X_new = np.array([1, 2000, 3, 4, 5, 26, 7]).reshape(-1, 1)
print(model.predict(X_new))

# 5. On veut tracer notre régression linéaire sur un graphique:

y_pred = model.predict(x)

# 6. On observe ici les valeurs obtenues par l'algoritme, (avec le taux d'erreur quadratique de base)
print('je prévois les réponses suivantes concernant les valeurs de X que vous me donnez:', y_pred, sep='\n')

# 7. On dessine une grille pour une meilleur lisibilité du graphe
axes = plt.axes()
axes.grid() 

# 8. On dessine chaque point de nos vecteurs x et y du début du script

plt.scatter(x,y) 

# 9. On dessine La ligne de la régression linéaire qui a été calculée par skLearn .
plt.plot(x,y_pred, color='blue', linewidth=3)

# 10. On affiche le graphique.
plt.show()