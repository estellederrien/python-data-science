""" 

Python niveau Lycée  :

Dénombrement : Arrangement ou Permutation .

Source : Monka https://www.youtube.com/watch?v=hWkIwXXEECc
""" 


""" 
EXO 1
Combien de mots composés de 3 lettres de l'alphabet peut on former ?

1. Est ce  que l'ordre compte ? FFO != OFF, donc oui le résultat est ordonné, donc c'est une liste de type (x,y,z).

2. Est ce qu'il y a des répétitions ? Oui car il y a FFO ou OFF .

3. Donc on parle d'un calcul de P-Uplets et dans le cadre de l'exo c'est un 3 uplets .

4. SI n , est l'ensemble et p la longuer de la liste, alors, le nombre de listes possibles est n¨p 

 """

#  Modélisation en fonction : 

def calcule_nb_liste(n,p):
    return n**p

print(calcule_nb_liste(26,3))

# 17576 listes possibles

""" 
EXO 2
On dispose de 26 jetons marqués des 26 lettres de l'alphabet , on tire successivement et sans remise 3 jetons . 
Combien de mots de 3 lettres peut on former?

1. Est ce  que l'ordre compte ? Oui, car c'est successif .

2. Est ce qu'il y a des répétitions ? Non, car c'est sans remise .

3. Du coup c'est un arrangement , une liste de 3 éléments, sans répétition : 26 possibilités * 25 possibilités * 24 possibilités

4. Du coup on utilise plutot la formule n! / (n-p)! qui est 26! / (26 - 3)!

 """

 #  Modélisation en fonction : 
import math
def calcule_nb_liste_sans_remise(n,p):
    return math.factorial(n) / math.factorial(n - p)

print(calcule_nb_liste_sans_remise(26,3))

""" 
EXO 3
Quel est le nb d'anagrammes du mot 'MDR'

1. Est ce  que l'ordre compte ? Oui.

2. Est ce qu'il y a des répétitions ? Non parce que on utilise une fois M, une fois R, une fois D

3. Du coup c'est un arrangement , mais c'est le cas particulier, la permutation .

4. Du coup on utilise plutot la formule n!

 """
 #  Modélisation de la permutation en fonction : 
import math
def calcule_nb_permutations(n):
    return math.factorial(n)

print(calcule_nb_permutations(3))