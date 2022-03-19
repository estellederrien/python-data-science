""" 
Calculer une dérivée
Sources :
https://towardsdatascience.com/taking-derivatives-in-python-d6229ba72c64
https://www.dcode.fr/derivee
https://moonbooks.org/Articles/Calculer-et-tracer-la-d%C3%A9riv%C3%A9e-dune-fonction-avec-python/
http://how.okpedia.org/fr/python/comment-calculer-la-derivee-d-une-fonction-en-python

La fonction diff() a au moins deux paramètres 
Le premier argument y est la fonction à dériver. 
Le deuxième argument x est la variable de dérivation. 
La fonction diff() génère la dérivée première.
"""

import sympy as sym
from sympy import init_printing
init_printing() 

# EXAMPLE 1
# Declarer une  variable
x = sym.Symbol('x')

# ON calcule la dérivée premiere de x^5
print(sym.diff(x**5))
## 5x^4


# EXAMPLE 2
# calculer la dérivée de la fonction f(x)=x2 quand x=2.
from scipy import misc 
def fonction(x): 
    return x*x
print(misc.derivative(fonction, 2.0))
#4

# EXAMPLE 3
#  calculer la derivée de la fonction f(x)=3x2+2x+1 sur l'intervalle [-2,2] et de tracer celle-ci avec la bibliothèque python matplotlib
from pylab import *
from scipy import misc

ax = subplot(111)

def fonction(x):
    return 3*x*x+2*x+1

# Dessiner la function
x = arange(-2.0, 2.0, 0.01)
y = fonction(x)
plot(x, y,'r-')

# Dessiner la dérivée
yp = misc.derivative(fonction, x)
plot(x, yp,'b-')

grid(True)

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

text(-0.75, 6.0,
     r'$f(x)=3x^2+2x+1$', horizontalalignment='center',
     fontsize=18,color='red')

text(-1.0, -8.0,
     r"$f'(x)=6x+2$", horizontalalignment='center',
     fontsize=18,color='blue')

show()