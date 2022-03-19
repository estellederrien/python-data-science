# Chapitre 1 : Les suites .
# Source : 1. Dunod - Mini manuel de mathématiques financières
# Functions Python élaborées à partir des fonctions mathématiques du livre, par Nicolas HULEUX
""" 
====================================================================================
Calculer la valeur d'un terme d'une suite arithmétique, à l'aide d'une function secondaire.
====================================================================================
"""

def calculerTermeRecurrence(premierTerme,f,dernierTerme):
    u = premierTerme
    for index in range(dernierTerme):
        u = f(u)
    return u

def ajoute_deux(x):
    return 2 + x


print(calculerTermeRecurrence(1,ajoute_deux,5))
#11



""" 
====================================================================================
Calculer la somme des termes d'une suite arithmétique de raison 2 du rang u0 au rang u(n).
====================================================================================
"""
raison = 2 

def somme(n):
    u=1
    s=0
    for i in range(0,n+1):
            s=s+u
            u=raison+u
           
    return(s)

print(somme(2)) # On itère jusqu'au terme u3 ( La boucle for commence à 0, donc ca compte 3 termes)
# La somme est de u0+ u1 +u2 = 1 + 3 + 5 = 9



""" 
====================================================================================
Calculer le n ieme terme d'une suite géométrique avec une fonction récurrente en paramêtre, de raison * 2 .
====================================================================================
"""
def calculerTermeRecurrence(premierTerme,f,n):
    u = premierTerme
    for index in range(n):
        u = f(u)
    return u

def double(x):
    return 2 * x 

print(calculerTermeRecurrence(1,double,5))

""" 
====================================================================================
# Calculer la Somme des termes d'une suite géométrique
# Somme = (q ^ (Nombre de termes+1) - 1 / q - 1 ) * 1er terme 
# avec q qui est la raison   avec q ≠ 1 et q ≠ 0,
====================================================================================
""" 

u0 = 1       # on initialise u au premier terme de la suite
n = 5        # on veut calculer jusqu'au rang 5
q = 2        # on multiplie par 2 à chaque fois.

# Somme = (q ^ (Nombre de termes+1) - 1 / q - 1 ) * 1er terme ->c'est la formule du livre Dunod Finances
c = q ** (n + 1)
Somme =  (  (c - 1) / (q - 1)) * u0 
print(Somme) # u5 32 -> somme u0 + u1 + u 2 = 63 = OK


# Chapitre 2 : Les intérêts simples et l'escompte .



# -------------------------------------
# 1. La formule des intérêts simples .
# -------------------------------------

def placement_annuel(nb_annees,taux_decimal,capital_place):
    return capital_place * (1 + nb_annees * taux_decimal)

print(placement_annuel(2,0.03,1000)) # 1060


def placement_journalier(nb_jours,taux_decimal,capital_place):
    return capital_place * (1 + taux_decimal * (nb_jours/360))

print(placement_journalier(185,0.08,1000)) # Idem livre Dunod 1041.11

# -------------------------------------
# 2. La formule des versements constants .
# -------------------------------------

def versement_constant(somme,nb_mois,taux):
    return somme * nb_mois * ( 1 + taux * ((nb_mois - 1 )/ 24 ))

print(versement_constant(50,10,0.10)) # La personne qui investit 50 euros par mois sur 10 mois à 10% aura un capital de 518.75 euros à la fin des 10 mois, soit 18.75 d'intérêts


# -------------------------------------
# 3. Calculer un taux moyen .
# -------------------------------------

"""
Cn sont les capitaux placés respectifs en euros
Dn sont les durées respectifs en jours
Tn sont les taux respectifs en décimal
"""

Cn = [1000,2000]
Dn = [50,30]
Tn = [0.06,0.02]

def taux_moyen(Cn,Dn,Tn):
    
    var1 = []
    var2 = []
    
    for  idx, val in enumerate(Cn ):
        var1.append(Cn[idx] * Dn[idx] * Tn[idx]) 
    for idx, val in enumerate(Cn):
        var2.append(Cn[idx] * Dn[idx] ) 

    total1 = 0
    total2 = 0

    for x in var1:
        total1 += x
    for x in var2:
        total2 += x

    return (total1 / total2) * 100
    
  

print(taux_moyen(Cn,Dn,Tn))  # Idem Livre Dunod : 3.82%   = OK la function est bonne !