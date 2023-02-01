# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

# Prédire la qualité d'un vin en fonction des champs fixed acidity, 
# volatile acidity, citric acid, residual sugar, chlorides, 
# free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, 
# alcohol

# pour cela, un fait une régression multi-linéaire.

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# CHARGER UN DATASET CSV DE PLUSIEURS COLONNES
dataset = pd.read_csv('datasets/winequality.csv')

# INFOS SUR LE FICHIERS 19040 rows and 31 columns.
print(dataset.shape) 

# STATS SUR LE FICHIER
print(dataset.describe())

# LES COLONNES EN NAN 
dataset.isnull().any()

# SUPPRIMER LES VALEURS NULLES
dataset = dataset.fillna(method='ffill')

# DIVISER LES DATA EN ATTRIBUTS ET LABELS , X contient les attributs/features, et y contients les labels.
X = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol']].values
y = dataset['quality'].values


# ON VISIONNE LES VALEURS MOYENNES DE QUALITE, ON VOIT QUE CEST ENTRE 5 et 6
plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['quality'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


regressor = LinearRegression()  
regressor.fit(X_train, y_train)


y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))