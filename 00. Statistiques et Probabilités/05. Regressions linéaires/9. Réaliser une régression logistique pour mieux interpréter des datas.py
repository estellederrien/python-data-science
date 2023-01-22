# Source : 
# https://people.duke.edu/~ccc14/sta-663/BlackBoxOptimization.html

""" Courbe d'ajustement

Parfois, nous voulons simplement utiliser les moindres carrés non linéaires pour ajuster une fonction aux données, 
peut-être pour estimer des paramètres pour un modèle mécaniste ou phénoménologique.
 La fonction curve_fit utilise l'algorithme de quasi-Newton Levenberg-Marquadt pour effectuer de tels ajustements. 
 Derrière les scènes, curve_fit est juste un wrapper autour de la fonction leastsq que 
 nous avons déjà vue dans un format plus pratique. """

from scipy.optimize import curve_fit

 # Pour Tracer les courbes
import matplotlib.pyplot as plt
import numpy as np

def logistic4(x, a, b, c, d):
    """La fonction logistique à quatre paramètres est souvent utilisée pour ajuster les relations dose-réponse."""
    return ((a-d)/(1.0+((x/c)**b))) + d

nobs = 24
xdata = np.linspace(0.5, 3.5, nobs)
ptrue = [10, 3, 1.5, 12]
ydata = logistic4(xdata, *ptrue) + 0.5*np.random.random(nobs)

popt, pcov = curve_fit(logistic4, xdata, ydata)

perr = yerr=np.sqrt(np.diag(pcov))
print ('Param\tTrue\tEstim (+/- 1 SD)')
for p, pt, po, pe  in zip('abcd', ptrue, popt, perr):
    print ('%s\t%5.2f\t%5.2f (+/-%5.2f)' % (p, pt, po, pe))

x = np.linspace(0, 4, 100)
y = logistic4(x, *popt)
plt.plot(xdata, ydata, 'o')
plt.plot(x, y)
plt.show()