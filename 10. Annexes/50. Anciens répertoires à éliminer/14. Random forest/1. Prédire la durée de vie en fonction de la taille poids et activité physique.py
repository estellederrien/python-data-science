import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pour générer un DATASET :
# https://www.generatedata.com/


df = pd.read_csv("datasets/life_expectancy.csv")

# Montrer le fichier qui a été chargé 
print(df.head())

# On extrait les caractéristiques X (Features, par exemple, la taille , le poids , la cigarette ) , et l'espérance de vie (y) du tableau df

X = df.values[:, :-1]
y = df.values[:, -1]

# On importe la librairie de regression Random Forest 
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()

# Ajustement des données - On "entraine" l'algo avec nos datas .
model.fit(X, y)
print(model.fit(X, y))

# On prédit les valeurs de y (Espérance de vie ) en fonction de X (les features présents dans le tableau)
predicted = model.predict(X)

# On affiche les valeurs X de l'espérance de vie présentes dans le tableau .
print(y);

# On affiche les valeurs d'espérance de vie qui ont été prédites par l'algorithme random Forest, pour comparer .
print(predicted);

# Affiche le taux erreur quadratique moyen de l'algo, pour voir si l'algo est bien adapté à nos données.

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, predicted)
rmse = np.sqrt(mse)
print (rmse)


# ON affiche dans un graphe les données X actuelles et les prédictions pour voir si l'algo marche bien ...
plt.scatter(y,predicted, alpha = 0.5)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()


# C'est bien, mais maintenant, on veut donner à l'algorithme un autre fichier 
# qui ne comprends pas les espérances de vie, mais qui comprends les features (taille poids, cigarette...), 
# et qu'il calcule nos espérances de vie !

df = pd.read_csv("datasets/life_expectancy2.csv")

# On prends les valeurs des features ; toutes les colonnes sauf la dernière , qui est celle qu'on doit prédire.
X = df.values[:, :-1]
# On prédit les valeurs de y (Espérance de vie ) en fonction de X (les features présents dans le tableau)
predicted = model.predict(X)
# On affiche les valeurs d'espérance de vie qui ont été prédites par l'algorithme random Forest
# [56.9198189  34.87671429 76.9885     38.1844881  67.07279365]
# On voit que la personne qui père 210 kgs a 38 d'espérance de vie
print(predicted);
