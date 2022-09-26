""" 
Les intérêts composés:

Sources : 

1. Dunod - Mini manuel de mathématiques financières

Functions élaborées à partir des fonctions mathématiques, par NIcolas HULEUX

"""


""" CH 1. 
 A/ Les intérêts simples se calculent sur la somme placée initiale, 
mais les intérêts composés se calculent sur la somme l'année passée. """

# Somme initiale investie
S0 = 1000 
# Intérêts en décimal de 5%
i = 0.05
# Durée en années
n = 3 

# Formule : 
# Sn = S0(1+i)**n
# Sn est une suite géométrique de premier terme S0 et de raison (1 + i)

S3 = S0 * (1+i) ** n
print(S3)# La somme dispo au bout de 3 ans est de 1157 , 63 E soit 157,63 Eu d'intérêts

# Modélisation de la function 
def valeur_acquise(somme_initiale,duree_placement,taux):
    return somme_initiale * (1 + taux) ** duree_placement
print(valeur_acquise(1000,3,0.05)) # 1157.6250000000002 idem livre Dunod


"""  B/ ReTrouver le capital initial placé en connaissant la valeur acquise du placement ,
 la durée du placement (3) et le taux de placement (0.05) :  """

valeurPlacee = S3 *(1 + i) ** -n
print(valeurPlacee) # 1000

# Modélisation de la function 
def retrouver_valeur_placee(valeur_acquise,duree_placement,taux):
    return valeur_acquise *(1 + taux) ** -duree_placement

print(retrouver_valeur_placee(1157.63,3,0.05)) #1000.0043191879927 idem livre Dunod

""" C/ Calculer la durée de temps que va mettre un investissement S0 à atteindre 
une certaine valeur Sn à un taux de i % en décimal. """

# durée = logarithme( Sn / S0 ) / logarithme(1 + i) (Formule du livre Dunod)

# Exemple : En combien de temps un capital de 1000 euros peut il atteindre une valeur acquise de 1215.51 E au taux annuel de 5 % en décimal?

S0 = 1000
Sn = 1215.51
t = 0.05

import math
duree = math.log(S0 / Sn) / math.log(1 + t)
print(duree) # -4.000 , Dans le livre c'est 4 ans. (Pourquoi négatif ?)

# Modélisation de la function + a FAIRE 
# def duree_atteinte

""" 2.3 VERSEMENTS CONSTANTS """

""" On place 1000 Euros pendant 15 mois en intérêts simples à 5% .
Déterminer la valeur acquise des versements de ce compte :  """

""" capital = capital acquis en fin de durée.
m = Nombre de mois ou l'on place le versement constant.
t = taux en décimal
s = somme placée chaque mois.

capital = s * m * ( 1 + t * (m - 1 / 24)) """

# capital = 1000 * 15  * (1 +0.005 * (15-1/24) ) = 15 437,50 Euros // Resultat DUNOD

# Modélisation de la function des versements constants .

""" 
m = Nombre de mois ou l'on place le versement constant.
t = taux en décimal
s = somme placée chaque mois.
 """
def valeur_acquise_des_versements_constants(s,m,t):
    return s * m * ( 1 + t * ((m - 1) / 24))

print(valeur_acquise_des_versements_constants(1000,15,0.05)) #  idem livre Dunod


