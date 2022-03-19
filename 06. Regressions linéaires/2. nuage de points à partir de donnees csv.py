# https://www.stat4decision.com/fr/faire-regression-lineaire-r-python/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importer les données Advertising.csv
donnees = pd.read_csv('dataset\Advertising.csv', index_col=0)
donnees.head()

from sklearn.linear_model import LinearRegression

#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X
list_var=donnees.columns.drop("Sales")
y=donnees.Sales
X=donnees[list_var]

modeleReg.fit(X,y)

print(modeleReg.intercept_)
print(modeleReg.coef_)

#calcul du R²
modeleReg.score(X,y)

RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

plt.plot(y, modeleReg.predict(X),'.')
plt.show()

plt.plot(y, y-modeleReg.predict(X),'.')
plt.show()
