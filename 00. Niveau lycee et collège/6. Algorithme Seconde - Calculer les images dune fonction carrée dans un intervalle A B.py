""" 

Python niveau Lycee seconde:

Calculer les images d'une fonction carrée sur un intervalle A B

f(x) -> x^2

"""

# 0. import de la lib


# 1. initialisation des variables
a       = float(input("valeur du début de l'intervalle appelé a ?"))
b       = float(input("valeur de la fin de l'intervalle appellée b ?"))
pas     = float(input("valeur du pas ? "))

# 2. Calculs des images de x par la fonction, carrée

x = a 

# Une image est égale à x au carré .
y = x ** 2

# On calcule l'image pour chaque pas de la fonction, jusqu'à la fin de l'intervalle.
while x <= b :
    
    # On exécute la fonction carrée sur la nouvelle valeur de x 
    y = x**2
    
    print(x,"a pour image ",y)

    # On incrémente x d'un pas lors de chaque itération
    x = x + pas
  