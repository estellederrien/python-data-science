""" 

Python niveau Lycee :

Définir une liste en compréhension.

1.Donner tous les cubes d'entiers entre 1 et 10 

2.Donner tous les cubes d'entiers entre 1 et 100,  
Parmis ces nombres, donner uniquement ceux qui sont divisibles par 6

3. Donner les carrés d'une liste secondaire

Source : Yvan Monka
https://www.youtube.com/watch?v=aXgNfWjEyP8

"""

# 1. créer la liste de x au cube de 1 à 10
l = [x**3 for x in range(1,11)]
print(l)

# 2. créer la liste de x au cube de 1 à 100 et la condition est qu'il soit divisible par 6 ( Soit un modulo = à 0 )
l = [x**3 for x in range(1,101) if x**3%6 == 0]
print(l)

# 3. Donner les carrés d'une liste secondaire
m = [2,5,9,10]
n = [x**2 for x in m] 
print(n)

