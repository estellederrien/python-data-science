""" Python niveau collège 3eme :
Tirer de façon aléatoire une pièce 1000 fois et compter combien de fois elle tombe pile ou face

Univers omega (0,1) - Cardinal = 2 - P(o)  = 2 ^ cardinal = 4 
 . """

# 0. import de la lib
import random

# 1. initialisation des variables
nbExperiences   = 1000
nbPile          = 0
nbFace          = 0
i               = 1

# 2. On lance 1000 fois la pièce
while i < nbExperiences :
    # On incremente le compteur
    i = i + 1 
    
    # On lance la pièce
    x = random.uniform(0, 1)
    
    if x < 0.5 :
        nbPile  += 1
    
    if x > 0.5:
        nbFace  += 1


print("Nombre de tirages piles :", nbPile);
print("Nombre de tirages face : ", nbFace);
  