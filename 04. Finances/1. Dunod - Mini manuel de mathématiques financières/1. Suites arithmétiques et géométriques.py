""" 
Suites arithmétiques et géométriques en python pour la finance :

Sources : 

1. Dunod - Mini manuel de mathématiques financières
2. Dunod - Méthodes mathématiques pourl'informatique pour le BTS SIO
3. Yvan Monka - SUITES : Calculer la somme des termes d'une suite (ALGORITHME) - Tutoriel PYTHON 
4. Python au lycée - tome 2 -  http://exo7.emath.fr/cours/livre-python2.pdf 
5. https://emilypython.wordpress.com/2019/02/20/calculer-le-terme-de-rang-n-dune-suite-recurrente-avec-python/
6. https://www.jeuxmaths.fr/cours/suites-geometriques.php
"""






""" 
PARTIE 1 :
Suite arithmétique 
La raison d'une suite arithmétique est r.
U0 est le premier terme, U1 le second ,U2 le troisième et ainsi de suite : Un

Définition globale:
Un + 1 = Un + r 


Les suites arithmétiques se retrouvent lorsque il y a un ajout ou un retrait d'une même somme à la meme période .
Loyer + 400 par mois, Retirer 100E de son compte tous les ans, intérêts simples , production augemente de 100 par jours.

"""
# -------------------------------------------------------------------------------
# 1. Calculer la valeur d' un terme d'une suite arithmétique si on connait u0 ( Le premier terme):
# Un = U0 + n * r
# -------------------------------------------------------------------------------

# Observons un exemple. On veut calculer le terme de rang 5 de la suite arithmétique de premier terme 1 et de raison 2. 
# Autrement dit, on va additionner  2 à u0 , puis 2 à u1 , etc.

u0 = 1       # on initialise u au premier terme de la suite
n = 5        # on veut calculer le terme de rang 5
raison = 2   # on ajoute 2 à chaque fois.

# Un = U0 + n * r
u5 = u0 + n * raison
print(u5)
# ça nous donne la valeur de 11 pour le terme de rang 5

""" 
Seconde solution :
Il est possible de mettre tout ceci dans une fonction Python nommée calculerTermeRecurrence, qui va prendre trois paramètres : """
def calculerTermeRecurrence(premierTerme,f,n):
    u = premierTerme
    for index in range(n):
        u = f(u)
    return u

def double(x):
    return 2 + x


print(calculerTermeRecurrence(1,double,5))

# -------------------------------------------------------------------------------
# 2. Calculer la somme des termes d'une suite arithmétique :
# -------------------------------------------------------------------------------

def somme(n):
    u=1
    s=0
    for i in range(0,n+1):
            s=s+u
            u=2+u
           
    return(s)

print(somme(2)) # On itère jusqu'au terme u3 ( La boucle for commence à 0, donc ca compte 3 termes)
# La somme est de u0+ u1 +u2 = 1 + 3 + 5 = 9

""" 
Seconde solution : 
Avec cette formule  Dunod - Mini manuel de mathématiques financières:

Ma_somme = ((1er terme + dernier terme) * Nb de termes) / 2 
"""

Ma_somme = ((1 + 5) * 3) / 2
print(Ma_somme) #  La somme est 9

""" 
PARTIE 2 :
Suite géométriques 
La raison d'une suite géométrique est q.
U0 est le premier terme, U1 le second ,U2 le troisième et ainsi de suite : Un

Définition globale:
Un + 1 = q * Un

ON les retrouve quand on multiplie par un facteur constant 
Une production baisse de 2% par mois, salaire augmente de 10% par ans, l'netreprise double tous les 3 ans, les intérêts composés.


Une augmentation de 10% est une multiplication par 1.1
Une baisse de 2% signifie une multiplication par 0.98

Si z est une valeur
Une augmentation  de +t% = z * 1 + t%
Une baisse de -t% = z * 1 - t%
"""
# -------------------------------------------------------------------------------
# 1. Calculer la valeur d'un terme d'une suite géométrique si on connait u0 ( Le premier terme):
# Un = q^n * U0
# -------------------------------------------------------------------------------

u0 = 1       # on initialise u au premier terme de la suite
n = 5        # on veut calculer le terme de rang 5
q = 2   # on multiplie par 2 à chaque fois.

# Un = q^n * U0 ->c'est la formule du livre Dunod Finances
u5 = q ** n * u0
print(u5)



""" 
Seconde solution :
Il est possible de mettre tout ceci dans une fonction Python nommée calculerTermeRecurrence, qui va prendre trois paramètres : """
def calculerTermeRecurrence(premierTerme,f,n):
    u = premierTerme
    for index in range(n):
        u = f(u)
    return u

def double(x):
    return 2 * x

print(calculerTermeRecurrence(1,double,5))


# -------------------------------------------------------------------------------
# 2. Calculer la valeur d'un terme d'une suite géométrique si on ne dispose pas du premier terme:
# Un = q^n-k * Uk
# -------------------------------------------------------------------------------

# Exemple : Si on a une suite  de raison 5 avec u3 = 625 , alors k = 3 dans la formule précédente.
# On peux ensuite calculer Un


# -------------------------------------------------------------------------------
# 3. Somme des termes d'une suite géométrique
# Somme = (q ^ (Nombre de termes+1) - 1 / q - 1 ) * 1er terme 
# avec q qui est la raison   avec q ≠ 1 et q ≠ 0,
# -------------------------------------------------------------------------------

u0 = 1       # on initialise u au premier terme de la suite
n = 5        # on veut calculer le terme de rang 5
q = 2        # on multiplie par 2 à chaque fois.

# Somme = (q ^ (Nombre de termes+1) - 1 / q - 1 ) * 1er terme ->c'est la formule du livre Dunod Finances
c = q ** (n + 1)
Somme =  (  (c - 1) / (q - 1)) * u0 
print(Somme) # u5 32 -> somme u0 + u1 + u 2 = 63 = OK

# u0 1
# u1 2
# u2 4 -> somme u0 + u1 + u 2 = 7
# u3 8 -> somme u0 + u1 + u 2 + u3= 15
# u4 16 -> somme u0 + u1 + u 2 + u3 + u4 = 31
# u5 32 -> somme u0 + u1 + u 2 + u3 + u4 + u5 = 63
# u6 64

# -------------------------------------------------------------------------------
# 3. Somme des termes d'une suite géométrique sans commencer par u0
# Somme = (q ^ (Nombre de termes+1) - 1 / q - 1 ) * 1er terme 
# avec q qui est la raison   avec q ≠ 1 et q ≠ 0,
# -------------------------------------------------------------------------------
u3 = 15
n = 5
# Somme = (q ^ Nombre de termes - 1 / q - 1 ) * 1er terme
c = q ** n 
Somme =  (  (c - 1) / (q - 1)) * u3 
print(Somme) # u5 32 -> somme u0 + u1 + u 2 = 63 = OK