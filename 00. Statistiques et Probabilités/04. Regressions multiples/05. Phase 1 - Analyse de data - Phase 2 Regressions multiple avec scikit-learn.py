""" 
# TITRE

Régression multiple linéaire avec scikit-learn
Prédire les ventes en fonction de la  pub radio et tv 

# LE PROBLEME 

PHASE 1  : ANALYSE DES VENTES
PHASE 2	 : PREDICTION DES VENTES 

TRADUCTION EN FRANCAIS

    Auteur :
	Lannie520
   https://github.com/Columbia-Intro-Data-Science/python-introduction-Lannie520/blob/master/Homework%201%20-%20Github%20and%20Pandas.ipynb


"""

# Librairies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.linear_model import LinearRegression
import numpy.random as nprnd
import random
import json
import numpy as np
pd.set_option('display.max_columns', 500)

# Commençons par importer ce fichier csv en tant que trame de données pandas à l'aide de read_csv ():
df = pd.read_csv("datasets/Advertising.csv")

# afficher les cinq premières lignes de l'ensemble de données publicitaires
print(df.head())


# Quelles sont les fonctionnalités? (FEATURES)

    # TV: dollars publicitaires dépensés à la télévision pour un seul produit sur un marché donné (en milliers de dollars)
    # Radio: l'argent publicitaire dépensé à la radio
    # Journal: les dépenses publicitaires consacrées au journal
	# Objectif: prédire le nombre de ventes sur un marché donné en fonction de la publicité à la télévision, à la radio et dans les journaux.


# Problème 2, partie 0: tracer des tracés de boîtes de coefficients

df.boxplot()

plt.show()


# Problème 2, partie 1: créer des nuages ​​de points en utilisant plt.scatter () 
# qui compare l'investissement au retour sur investissement

plt.scatter(df["TV"],df["Sales"],label="TV")
plt.scatter(df["Radio"],df["Sales"],label="radio")
plt.scatter(df["Newspaper"],df["Sales"],label="newspaper")
plt.title('Investissement vs ventes ') 
plt.legend(bbox_to_anchor=(1,1),loc=1,borderaxespad=0.)
plt.xlabel('Investissement en dollars')
plt.ylabel('Ventes en unités')
plt.show()

# Problème 2 partie 1b: créer la matrice de correlation entre l'investissement publicitaire et les ventes !

from pandas.plotting import scatter_matrix 
scatter_matrix(df,figsize=(5,5))
plt.show()

print(df.corr());

# Lesquelles des variables semblent corrélées entre elles? Lequel pas? Expliquez votre réponse:

# De la matrice de corrélation, nous pouvons voir que les variables TV et Sales ont la corrélation 0,782, 
# qui est la plus grande parmi les 3 chaînes. 
# Le deuxième est la corrélation entre la radio et les ventes, qui est de 0,576. 
# Alors que sa corrélation avec le journal est d'environ 0,228, ce qui n'est pas élevé. 
# Ce résultat correspond aux diagrammes de dispersion que nous avons observés.




# Probleme 2, partie 2: prédire les ventes à l'aide de sklearn

    # Divisez les données en sous-ensembles de formation et de test.
    # Former le modèle à l'aide de LinearRegression () de sklearn.linear_model sur les données d'entraînement.
    # Évaluer à l'aide de RMSE et R ^ 2 sur l'ensemble de test

# Si vous avez besoin d'aide, veuillez vous référer à cet exemple:

# https://github.com/Columbia-Intro-Data-Science/APMAE4990-/blob/master/notebooks/Lecture%202%20-%20Regression%20Bookingdotcom%20Case%20Study.ipynb


# Voyez où je divise les données en tests / formation et performances d'évaluation.


# Librairies
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split


# Tout d'abord, nous initialisons notre modèle de régression linéaire, 
# puis ajustons le modèle à nos prédicteurs et variables de sortie:

# a) Définissez y pour être les ventes en df
y = df['Sales']

# b) Définissez X pour être juste les fonctionnalités décrites ci-dessus dans df
X = df.drop(['Sales'],1) # ON PRENDS TOUTES LES COLONNES SAUF LA COLONNE DES VENTES QUON DROPPE 'supprime'

# c) Diviser au hasard les données en formation et tests - 80% de formation, 20% de test.
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)
	
#  d) Former le modèle sur les données de formation et faire des prédictions sur les données de test

regress = LinearRegression()
regress.fit(X_train,y_train)
print('La prédiction est : \n',regress.predict(X_test))

# e) Évaluez le R ^ 2 sur les données de test. Est-ce que c'est bon? Mal? Pourquoi?
print('R^2 est: \n',regress.score(X_test,y_test))

# R ^ 2 est:
 # 0,899438024101

# Le score R ^ 2 est d'environ 0,9. Un score R ^ 2 de 0,9 signifie 
# qu'environ 90% de la variance est 
# expliquée par le modèle. Ainsi, le modèle fonctionne relativement bien.

# f) Faites un diagramme de dispersion de vos prévisions par rapport aux valeurs réelles sur les données de test. 
# Cela ressemble-t-il à un bon modèle?

plt.scatter(y_test,regress.predict(X_test))
plt.plot(y_test,y_test,color='r')
plt.title("Diagrammes de dispersion de la prévision par rapport à la valeur réelle")

# g) Pouvez-vous mesurer l'importance des fonctionnalités de ce modèle? Que devez-vous vérifier avant de tirer des conclusions?

# Essayez de regarder LinearRegression (). Coef_


print('Coefficients:\n',regress.coef_)
print("Somme résiduelle des carrés Erreur:: %.2f"
% np.mean((regress.predict(X_test) - y_test) ** 2))



# Coefficients:
 # [ 0.04472952  0.18919505  0.00276111]
# Somme résiduelle des carrés Erreur:: 3.17


# Explication:

# Les coefficients représentent les caractéristiques importantes du modèle. Chacun représente le nombre d'unités qui augmentera lorsqu'une unité de la variable augmentera. La somme résiduelle de l'erreur carrée mesure la moyenne de tous les résidus. Nous devons le vérifier avant de conclure car s'il est trop grand, cela signifie que le modèle ne fonctionne pas vraiment bien.

# En outre, nous pouvons envisager de normaliser l'ensemble de données avant d'exécuter la régression, car il semble que même si la radio a le coefficient le plus élevé tandis que la télévision en a un très petit, qui n'est pas le même que celui de la matrice de corrélation. C'est peut-être que les varibales elles-mêmes ne sont pas à la même échelle.

# h) Que pouvez-vous conclure de g) - pouvez-vous penser à une façon d'interpréter le résultat? Qu'aurions-nous dû faire pour mesurer l'importance des fonctionnalités impliquées?

# D'après g), nous savons que le coefficient de la télévision est d'environ 0,0447, ce qui signifie qu'avec une augmentation de 1 unité de la télévision, la vente augmentera d'environ 0,0447. De même, le coefficient de radio est d'environ 0,1889, ce qui signifie qu'avec une augmentation de 1 unité de radio, la vente augmentera d'environ 0,1889. Le coefficient du journal est d'environ 0,0028, ce qui signifie qu'avec une augmentation de 1 unité de journal, la vente augmentera d'environ 0,0028.
# Afin de mesurer l'importance des caractéristiques impliquées, nous pouvons voir quels sont les coefficients les plus significatifs. Afin de mesurer le significatif, nous devons standardiser le coefficient et supprimer les facteurs colinéaires.


