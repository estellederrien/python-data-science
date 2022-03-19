# Source : https://hernandis.me/2020/04/05/three-examples-of-nonlinear-least-squares-fitting-in-python-with-scipy.html
""" 
Premier exemple: une fonction scalaire

Le premier exemple que nous allons considérer est une simple fonction logistique
y(t)  = K / 1 + e^-r(t-t0)

Les trois paramètres de la fonction sont:

    K, le supremum de yyy (pensez à cela comme un maximum qui est atteint lorsque t = ∞,
    r, le taux de croissance logistique ou la netteté de la courbe, et
    t la valeur à laquelle le point médian K / 2 est atteint.

L'optimisation des paramètres θ = (K, r, t0)  est simple dans ce cas, 

car les moindres carrés  nous permet de saisir le modèle sans aucune modification particulière . 

Pour ce faire, nous définissons d'abord le modèle comme la fonction Python y(theta, t) 

puis générons des données en ys en évaluant le modèle sur un échantillon ts de la variable indépendante ttt . 

Lors de la génération des données de test, nous transmettons un tableau de nombres ts directement au modèle.

 Nous sommes capables de le faire car nous avons défini le modèle y en utilisant l’objet tableau de NumPy 
 
 qui implémente des opérations élémentaires standard entre les tableaux. 
 
 Nous ajoutons du bruit uniformément réparti, faisons une première estimation des paramètres theta0 et définissons 
 
 le vecteur de résidus fun. Le vecteur des résidus doit être fonction des variables d'optimisation θθ afin 
 
 que les moindres carrés puissent évaluer l'adéquation de ses suppositions. ??

 """



# Charger les libs
import numpy as np
from scipy.optimize import least_squares

def y(theta, t):
    return theta[0] / (1 + np.exp(- theta[1] * (t - theta[2])))

ts = np.linspace(0, 1)
K = 1; r = 10; t0 = 0.5; noise = 0.1
ys = y([K, r, t0], ts) + noise * np.random.rand(ts.shape[0])

def fun(theta):
    return y(theta, ts) - ys

theta0 = [1,2,3]
res1 = least_squares(fun, theta0)

print(res1)