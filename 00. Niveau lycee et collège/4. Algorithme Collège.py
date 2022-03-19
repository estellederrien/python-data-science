""" Python niveau collège 3eme :
Tirer de façon aléatoire une pièce
omega (0,1)
 . """

# 0. import de la lib
import random

# 1. initialisation des variables
x = random.uniform(0, 1)

# 2. On regarde de quel côté la pièce est tombée ( En python  le switch n'existe pas !)
if x < 0.5 :
    print("PILE :", x)


if x > 0.5:
    print("FACE :", x)   
  


