# Source : https://www.programiz.com/python-programming/examples/quadratic-roots
# Solve the quadratic equation ax**2 + bx + c = 0

# Une balle est lancée tout droit, à 3 m au-dessus du sol, avec une vitesse de 14 m/s.
# Quand touche-t-elle le sol?
#Source : https://www.mathsisfun.com/algebra/quadratic-equation-real-world.html

""" Ignorant la résistance de l’air, nous pouvons calculer sa hauteur en additionnant ces trois choses:
(Remarque: t est le temps en secondes)
La hauteur commence à 3 m: 3
Il se déplace vers le haut à 14 mètres par seconde (14 m/s): 14t
La gravité le tire vers le bas, changeant sa position d’environ 5 m par seconde au carré : −5t²
(Note pour les enthousiastes : le -5t² est simplifié de -(1/2)² avec a=9,8 m/s²) """

# importer le module complex math 
import cmath

a = -5
b = 14
c = 3

# calculer le discriminant
d = (b**2) - (4*a*c)

# trouver 2 solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))#

# The "t = −0.2" is a negative time, impossible in our case. /  La 1 ère solution trouvée est impossible
# The "t = 3" is the answer we want: / L solution 3 est ok , donc elle mets 3 secondes