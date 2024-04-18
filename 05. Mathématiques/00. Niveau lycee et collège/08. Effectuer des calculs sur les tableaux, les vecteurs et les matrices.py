""" 

Python niveau Lycee Term / Fac:

Utiliser les matrices

"""

# 0. import de la lib
import numpy as np


# 1. On crée un tableau et on se sert de np.max et np.min pour directement effectuer des calculs .
dataset = np.array([[2, 5, 6, 8, 3, 2, 5],
                     [7, 5, 3, 1, 6, 8, 0],                     
                     [1, 3, 3, 1, 0, 0, 8]]) 
max =  np.max(dataset, axis=1)
min =  np.min(dataset, axis=1) 
result = max - min
print('La valeur max - la valeur min de chacune de mes lignes est :',result)

# 2. On Multiplie un vecteur par une matrice 
a = np.array([2, 4, 6, 8]) 
b = np.array([[1, 2, 3, 4],              
[2, 3, 4, 5],             
[3, 10, 5, 6],              
[4, 5, 6, 7]]) 
c = np.dot(a, b) 
print('La multiplication de mon vecteur par ma matrice 4*4 est  :',c)
# [60 116 100 120]
# L 1 ère ligne est égale à  2 * 1 + 4 * 2 + 6 * 3 + 8 * 4, qui veut dire  60.


# 3. ON mutliplie une matrice par une matrice
a = np.array([[2, 10, 6, 8],[1, 3, 5, 7]]) 
b = np.array ([[1, 2],[2, 3],[3, 4],[4, 5]]) 
c = np.dot(a, b) 
print('La multiplication de ma matrice 2*4  par ma matrice 4*2 est  :',c)
# [[60 80] [50 66]]
#  1 * 1 + 3 * 2 + 5 * 3 + 7 * 4. = 50 pour trouver le résultat 50


