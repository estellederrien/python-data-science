""" Equation différentielle 

Info: 
Dans une equa diff, l'inconnue est une fonction.
Généralement, il y en a plusieurs résultats.
Il peut y avoir des conditions initiales, en ce cas, la solutions est unique .
Quand c'est égal à 0 , c'est "homogène".
Ca sert en stats, physique , mécanique, finances ..

Sources :

Solutions de calcul à la main :
http://dominique.frin.free.fr/terminales/coursTS_equadiff.pdf

Cas d'utilisations réels avec exemples: 
http://faccanoni.univ-tln.fr/user/enseignements/20152016/R33-R43_L2.pdf
Cas traités en PYTHON (Physique, Mécanique): 
https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/resolution-numerique-dequations-differentielles


Vidéos : 
MONKA : https://www.youtube.com/watch?v=YJNHTq85tJA

Tutos: 
https://dridk.me/equation-differentielle.html
https://dridk.me/category/informatique.html
https://interstices.info/modeliser-la-propagation-dune-epidemie/
https://web.stanford.edu/class/archive/math/math21/math21.1156/files/21/notes5.pdf
https://www6.versailles-grignon.inrae.fr/ecosys/content/download/5545/68104/version/1/file/Equations_Differentielles.pdf
https://fr.wikipedia.org/wiki/%C3%89quations_de_pr%C3%A9dation_de_Lotka-Volterra
https://www.methodemaths.fr/equadiff/#generalite
https://www.math.univ-toulouse.fr/~jbhu/Equa-diff-couverture.pdf
http://www.iecl.univ-lorraine.fr/~Damien.Megy/enseignement/1112calculsEtMaths/CM2011cours_EDO.pdf


exemple Eq diff classique : 
différentielle = nombre * f(x) - un nombre
ou 
f'(x) = 3*f(x)-5

Il s’agit donc d’une équation où l’inconnue n’est pas la variable x mais la fonction y. Résoudre une équation différentielle revient à trouver la ou les fonctions y solutions de cette équation.
"""

# Exemple 1 : Monka : https://www.youtube.com/watch?v=YJNHTq85tJA

# Pour un eq diff donnée y' = ay
# La solution générale est yc(x) = Ce^ax , C Appartient à R
# C est une constante qui peut prendre n'importe quelle valeur.

""" 
Si on nous donne 3y' + 5y = 0

1. Passer sous la forme y'= ay

y' = -5/3y

2. Donc la solution générale est 
yx(x) = Ce ^-5/3x , C appartient à R. 

3. Si on nous donne la condition initiale que y(1) = 2 , on nous demande l'unique solution

On substitue les valeurs 
Ce ^5/3*1 = 2
et ainsi de suite.
Puis on substitue C dans la première eq."""

# Exemple 2 : Monka : https://www.youtube.com/watch?v=QeGvVncvyLc

""" 
Si on nous donne y' - 2y  = x2

1. Passer sous la forme y'= ay + f



"""


# Exemple 3 : équation différentielle d'ordre 1 avec python
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# On précise notre constante
a=-0.1
# On crée la liste des temps : 1000 points entre t=0 et t=50. 
# Plus on met de points plus la résolution sera précise
temps = np.linspace(0, 50,1000)

# L'équation différentielle sous forme de fonction :
def equation(Y,temps):
    return a*Y

#On résout notre équation différentielle et on récupère la liste des résultats
Y=odeint(equation, [10], temps)

#On affiche le résultat des Y en fonction du temps
plt.plot(temps,Y)
# On montre le résultat
plt.show()
