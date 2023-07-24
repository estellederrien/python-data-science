""" 

Python niveau Lycée / Fac  :

Dénombrement : Arrangement ou Permutation .


Exemple :
Soit 1 Course de 10 élèves , le podium est de 3 personnes .

1.  Calculer le nombre le nombre de permutations possibles , permutations, car c'est le nombre de " rangements " possible qui comprends tous les élèves (arrangement de 10 élèves ).
2.  Calculer le nombre d'arrangements possibles de 3 personnes sur le podium. Un arrangement est une partie du nb total n d'élèves .
3.  Enumérer le nombre d'arrangements possibles de podiums possibles avec itertools.


Sources :
itertools : https://callicode.fr/blog/post/enumerer.html
http://python.jpvweb.com/python/mesrecettespython/doku.php?id=arrangements
"""


# 1. Calculer le nombre d'arrangements possible des 10 élèves, aussi appelé le nombre de permutations possibles 
#  la formule est n! (factorielle)

eleves = 10
fact = 1
for i in range(1, eleves+1):
  fact = fact * i
print (eleves,'Le nombre de permutations possible est de 10! = ',fact)

# 2.  Calculer le nombre d'arrangements possibles de 3 personnes sur le podium.
#  la formule est n! (factorielle) / (n - k)! Ou n est le nb total d'élèves et k le nb d'élèves sur le podium


def arrang(n, k):
    """Nombre des arrangements de n objets pris k à k"""
    if k>n:
        return 0
    x = 1
    i = n-k+1
    while i <= n:
        x *= i
        i += 1
    return x

print(" Il y a ",arrang(eleves,3)," podiums de 3 élèves possibles")



# 3. Enumérer le nombre de permutations possibles avec itertools

import itertools
eleves = [1,2,3,4,5,6,7,8,9,10]
for p in itertools.combinations(eleves,3):
    print(p)




