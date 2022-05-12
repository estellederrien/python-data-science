# Source : https://people.duke.edu/~ccc14/sta-663/BlackBoxOptimization.html
# Pour tracer avec matplotlib.pyplot : http://math.mad.free.fr/depot/numpy/courbe.html
"""
De nombreux problèmes d'optimisation du monde réel ont des contraintes - 

par exemple, un ensemble de paramètres peut devoir totaliser 1,0 (contrainte d'égalité), 

ou certains paramètres doivent être non négatifs (contrainte d'inégalité). 

Parfois, les contraintes peuvent être incorporées dans la fonction à minimiser, par exemple, 

la contrainte de non-négativité p > 0 peut être supprimée en substituant p = eq et en optimisant pour q. 

En utilisant de telles solutions de contournement, il peut être possible de convertir un problème d'optimisation 

contraint en un problème sans contrainte et d'utiliser les méthodes décrites ci-dessus pour résoudre le problème.

Alternativement, nous pouvons utiliser des méthodes d'optimisation qui permettent 

la spécification des contraintes directement dans l'énoncé du problème, comme indiqué dans cette section. 

En interne, les pénalités de violation de contraintes, les barrières et les multiplieurs de Lagrange 

font partie des méthodes utilisées pour gérer ces contraintes. Nous utilisons l'exemple fourni dans le didacticiel 

Scipy pour illustrer comment définir des contraintes.

Voici un problème : 

f (x) = - (2xy + 2x − x2−2y2)

Soumis aux contraintes
x3 − y = 0
y− (x − 1) 4−2≥0

Et aux limites
0.5≤x≤1.5
1.5≤y≤2.5 

"""

# On charge La lib qui va optimiser grâce à son module optimize
import scipy.optimize as opt

# Pour Tracer les courbes
import matplotlib.pyplot as plt
import numpy as np

# On écrit la fonction f (x) = - (2xy + 2x − x2−2y2)
def f(x):
    return -(2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*x[1]**2)

# On dessine la fonction 
x = np.linspace(0, 3, 100)
y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(np.vstack([X.ravel(), Y.ravel()])).reshape((100,100))

plt.contour(X, Y, Z, np.arange(-1.99,10, 1))
plt.plot(x, x**3, 'k:', linewidth=1)
plt.plot(x, (x-1)**4+2, 'k:', linewidth=1)
plt.fill([0.5,0.5,1.5,1.5], [2.5,1.5,1.5,2.5], alpha=0.3)
plt.axis([0,3,0,3])
plt.show()

""" Pour définir les contraintes, nous passons dans un dictionnaire avec les touches type, fun et jac. 
Notez que l'inégalité contrainte prend une forme Cjx≥0. 
Comme d'habitude, le jac est facultatif et sera estimé numériquement s'il n'est pas fourni. """

""" En fait, on réecrit les fonctions mathématiques suivantes : 

Soumis aux contraintes
x3 − y = 0
y− (x − 1) 4−2≥0

Et aux limites
0.5≤x≤1.5
1.5≤y≤2.5 
 """
cons = ({'type': 'eq',
         'fun' : lambda x: np.array([x[0]**3 - x[1]]),
         'jac' : lambda x: np.array([3.0*(x[0]**2.0), -1.0])},
        {'type': 'ineq',
         'fun' : lambda x: np.array([x[1] - (x[0]-1)**4 - 2])})

bnds = ((0.5, 1.5), (1.5, 2.5))
x0 = [0, 2.5]

# Optimisation sans contrainte
ux = opt.minimize(f, x0, constraints=None)
print(ux)

# Optimisation en tenant compte de la contrainte
cx = opt.minimize(f, x0, bounds=bnds, constraints=cons)
print(cx)

# On dessine la solution optimale avec une croix en 2D
x = np.linspace(0, 3, 100)
y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(np.vstack([X.ravel(), Y.ravel()])).reshape((100,100))
plt.contour(X, Y, Z, np.arange(-1.99,10, 1))
plt.plot(x, x**3, 'k:', linewidth=1)
plt.plot(x, (x-1)**4+2, 'k:', linewidth=1)
plt.text(ux['x'][0], ux['x'][1], 'x', va='center', ha='center', size=20, color='blue')
plt.text(cx['x'][0], cx['x'][1], 'x', va='center', ha='center', size=20, color='red')
plt.fill([0.5,0.5,1.5,1.5], [2.5,1.5,1.5,2.5], alpha=0.3)
plt.axis([0,3,0,3])
plt.show()