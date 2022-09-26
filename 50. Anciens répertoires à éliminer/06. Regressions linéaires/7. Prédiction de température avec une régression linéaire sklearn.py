# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# CHARGER UN DATASET CSV DE PLUSIEURS COLONNES
dataset = pd.read_csv('dataset/Weather.csv')

# INFOS SUR LE FICHIERS 19040 rows and 31 columns.
print(dataset.shape) 

# STATS SUR LE FICHIER
print(dataset.describe())

# CREER UN NUAGE DE POINTS AVEC MIN TEMPERATURE EN ABSCISSE ET MAX TEMPERATURE EN ORDONNEE
dataset.plot(x='MinTemp', y='MaxTemp', style='o')  
plt.title('MinTemp vs MaxTemp')  
plt.xlabel('MinTemp')  
plt.ylabel('MaxTemp')  
plt.show()


# TEMPERATURE MAX MOYENNE
plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['MaxTemp'])
plt.show()


# On veut prédire la maxtemp en fonction de la mintemp
X = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

# Next, we split 80% of the data to the training set while 20% of the data to test set using below code.
# The test_size variable is where we actually specify the proportion of the test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

# Comme nous l'avons vu, le modèle de régression linéaire trouve essentiellement la meilleure valeur pour l'ordonnée à l'origine et la pente, ce qui donne une ligne qui correspond le mieux aux données. Pour voir la valeur de l'interception et de la pente calculées par l'algorithme de régression linéaire pour notre jeu de données, exécutez le code suivant.
print(regressor.intercept_)#For retrieving the slope:
print(regressor.coef_)


# On prédit les températures max en fonction des températures min présentes dans le tableau, 
# puis on compare nos prédictions par rapport aux données réelles qui ont été relevées .
y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

# Nous pouvons également visualiser le résultat de la comparaison sous forme de graphique à barres en utilisant le script ci-dessous:

# Remarque: Comme le nombre d'enregistrements est énorme, à des fins de représentation, je ne prends que 25 enregistrements.
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
