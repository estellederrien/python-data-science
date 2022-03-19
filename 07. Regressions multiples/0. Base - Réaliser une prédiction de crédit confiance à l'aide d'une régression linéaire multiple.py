
""" 

Réaliser une prédiction de crédit confiance à l'aide d'une régression linéaire multiple .

Code le plus simplifié possible, sans import EXCEL préalable.

# Sources
https://datatofish.com/multiple-linear-regression-python/
https://heartbeat.fritz.ai/implementing-multiple-linear-regression-using-sklearn-43b3d3f2fe8b


"""

# 1. On charge les librairies
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. On crée nos données au format JSON

data = {
'salaire':[16880, 14220, 24500, 25984, 28660,35600],
'age':[19,18,28,33,32,40],
'credit_confiance':[27,28,33,34,37,40],
'enfant':[0,1,3,0,0,1]
}

# On fait comme si on chargeait un tableau EXCEL ...
df = pd.DataFrame(data,columns=['salaire','age','credit_confiance','enfant'])

# On vérifie si il existe une relation linéaire entre le salaire et l'age
plt.scatter(df['age'], df['salaire'], color='red')
plt.title('age vs Salaire', fontsize=14)
plt.xlabel('salaires', fontsize=14)
plt.ylabel('age', fontsize=14)
plt.grid(True)
plt.show()


# On vérifie si il existe une relation linéaire entre le salaire et le crédit confiance
plt.scatter(df['credit_confiance'], df['salaire'], color='red')
plt.title('credit_confiance vs Salaire', fontsize=14)
plt.xlabel('salaires', fontsize=14)
plt.ylabel('credit_confiance', fontsize=14)
plt.grid(True)
plt.show()


#  On place dans X le vecteur salaire et age, et dans le vecteur Y le vecteur des crédits confiances. 
X = df[['salaire','age']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['credit_confiance']
 
# On crée la régression linéaire multiple :
regr = LinearRegression()
regr.fit(X, Y)

# on visionne les caractéristiques de la régression linéaire multiple :
print('Intercept: \n', regr.intercept_)

print('Coefficients: \n', regr.coef_)

# On prédit une nouvelle valeur de Y ( credit confiance), en donnant à sklearn les valeurs de X.
nouveau_salaire = 28000
nouvel_age = 30
print ('je vous prédit que ce nouveau client aura un crédit confiance de : \n', regr.predict([[nouveau_salaire ,nouvel_age ]]))
