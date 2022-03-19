# https://mrmint.fr/regression-lineaire-python-pratique

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("dataset/univariate_linear_regression_dataset.csv")

#selection de la première colonne de notre dataset (la taille de la population)
X = df.iloc[0:len(df),0]
#selection de deuxième colonnes de notre dataset (le profit effectué)
Y = df.iloc[0:len(df),1] 


# On dessine les points x y des datas de nos 2 colonnes dans le graphique
axes = plt.axes()
axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
plt.scatter(X,Y) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent

# Maintenant, on fait une régression :
#linregress() renvoie plusieurs variables de retour. On s'interessera 
# particulierement au slope et intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

def predict(x):
	return slope * x + intercept
   
#la variable fitLine sera un tableau de valeurs prédites depuis la tableau de variables X
fitLine = predict(X)
plt.plot(X, fitLine, c='r') 

# Afficher les variables du fichier EXCEL ET la fitline qui est la regression linéaire des 2 colonnes qu'on a choisi'.
plt.show()

