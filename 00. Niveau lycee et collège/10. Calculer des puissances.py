""" 

Python niveau Lycee Term / Fac:

Calculer des puissances 

"""
# NOTATION  1
Puissance = 3**4 
  
print ("la valeur de 3**4 est : ", Puissance ) 

# NOTATION  2
# positive x, positive y (x**y)
print(pow(2, 2))    # 4

# negative x, positive y
print(pow(-2, 2))    # 4  

# positive x, negative y
print(pow(2, -2))    # 0.25

# negative x, negative y
print(pow(-2, -2))    # 0.25


""" Avec MODULO en argument 3 """

x = 7
y = 2
z = 5 

print(pow(x, y, z))    # 4

# Ici, 7 puissance 2 est égal à 49. Ensuite, 49 modulo 5 est égal à 4.


# Calculer modulo :
# Méthode 2: Effectuer la division entière et calculer la valeur de la différence.

# Exemple : Calcul de A=49modN=5 , faire la division : 49/5=9.8 Récupèrer la partie entière : 9, 
# la multiple par N=5 : 9×5=45. La différence entre 49 et 45 vaut 4, donc 49%5=4.

