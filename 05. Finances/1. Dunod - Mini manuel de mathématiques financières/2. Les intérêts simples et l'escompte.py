""" 
Les intérêts simples et l'escompte :

Sources : 

1. Dunod - Mini manuel de mathématiques financières
2. Wikibooks : https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Suites_en_Python
3. https://fr.wikihow.com/calculer-un-int%C3%A9r%C3%AAt-simple

"""

# -------------------------------------
# 1. La formule des intérêts simples .
# -------------------------------------

""" INTERETS PAR ANNEES """
#Les intérêts simples se calculent à partir du capital initial.
#Initialisation des variables :
n = 2     #duree_placement
t = 0.03  #taux_interet annuel de 3 % écrit au format décimal
C0 = 1000 #capital placé

# La somme totale gagnée à l'année n
Cn = C0 * ( 1 + n * t)
print(Cn) # 1060

# On transforme ça en function :
def placement_annuel(nb_annees,taux_decimal,capital_place):
    return capital_place * (1 + nb_annees * taux_decimal)

print(placement_annuel(2,0.03,1000)) # 1060

# La somme des intérêts sur n années est :
In = n * C0 * t
print(In)
# 60

""" INTERETS PAR MOIS """
# Initialisation des variables :
n = 120     # duree_placement avec un taux mensuel = 10 ans * 12 mois
t = 0.03    # taux_interet MENSUEL de 3 % écrit au format décimal
C0 = 55000  #capital placé

#La somme totale perçue au mois n
Cn = C0 * ( 1 + n * t)
print(Cn)
# 252999

#La somme des intérêts sur n mois est :
In = n * C0 * t
print(In)
# 198 000 euros c'est énorme car c'est un taux mensuel.

""" INTERETS PAR JOURS """
#EXEMPLE 3 : Durée comptée en jours , sur une année comptable de 360 jours.

#Initialisation des variables :
j = 50     #duree_placement en jours
t = 0.02  #taux_interet annuel de 2 % écrit au format décimal
C0 = 1000 #capital placé

# Les intérêts gagnés au bout de 50 jours sont  de (Formule du livre Dunod)
# Ij = C0 * t * (j/360)

somme = C0 * t * (j / 360)
print(somme) # Idem livre Dunod 2.777

# Exemple 4 : Durée comptée en jours(Formule du livre Dunod)

""" ON réalise un placement de 1000 euros à 8% du 1ere mars au 2 septembre .
Le nombre de jours entre ces 2 dates est de 31-1 + 30 +31 +30 + 30 +31 + 31 + 2 = 185 jours """

j = 185     #duree_placement en jours
t = 0.08  #taux_interet annuel de 2 % écrit au format décimal
C0 = 1000 #capital placé

# Le capital au terme du placement est :
# capital = C0 * (1 + t * (j/360))
capital = C0 * (1 + t * (j/360))
print(capital) # Idem livre Dunod 1041.11

# On transforme ça en function :
def placement_journalier(nb_jours,taux_decimal,capital_place):
    return capital_place * (1 + taux_decimal * (nb_jours/360))

print(placement_journalier(185,0.08,1000)) # Idem livre Dunod 1041.11

# -------------------------------------
# 2. La formule des versements constants .
# -------------------------------------

""" Une personne place une somme S tous les mois sur un compte au taux T pendant M mois .
Quelle est la valeur du capital après le dernier versement ? """

""" Exemple : Une personne place une somme S de 1000 tous les mois sur un compte au taux T de 5 % pendant 15 mois .
Quelle est la valeur du capital après le dernier versement ? """

somme = 1000
nb_mois = 15
taux = 0.05

#Formule du livre Dunod : 
capital = somme * nb_mois * ( 1 + taux * ((nb_mois - 1 )/ 24 ))
print(capital) # Idem livre Dunod  :  15 437,50E

# On transforme ça en function :
def versement_constant(somme,nb_mois,taux):
    return somme * nb_mois * ( 1 + taux * ((nb_mois - 1 )/ 24 ))

print(versement_constant(50,10,0.10)) # La personne qui investit 50 euros par mois sur 10 mois à 10% aura un capital de 518.75 euros à la fin des 10 mois, soit 18.75 d'intérêts

# -------------------------------------
# 3. Calculer un taux moyen .
# -------------------------------------

""" On investit à des taux différents, et on veut calculer le taux moyen de nos investissements. """

# On place 1000 E pendant 50 jours à 6 % et l'on place 2000E pendant 30 jours à 2%, quel est le taux moyen de l'ensemble de ces 2 placements?

"""
Cn sont les capitaux placés respectifs en euros
Dn sont les durées respectifs en jours
Tn sont les taux respectifs en décimal
"""

taux_moyen = (1000 * 50 * 0.06 + 2000 * 30 * 0.02) / (1000 * 50  + 2000 * 30 )
print(taux_moyen * 100) # Idem Livre Dunod : 3.82%

# On transforme ça en function ( Version naïve, pour tester , en fait, il faut un loop dedans assez compliqué):
def taux_moyen(Cn,Dn,Tn):
    return  (Cn[0] * Dn[0] * Tn[0] + Cn[1] * Dn[1] * Tn[1]) / (Cn[0] * Dn[0]  + Cn[1] * Dn[1] ) * 100

Cn = [1000,2000]
Dn = [50,30]
Tn = [0.06,0.02]

print(taux_moyen(Cn,Dn,Tn))  # Idem Livre Dunod : 3.82%

# Tentative de faire le loop , pour rendre la function générique et vraiment effective : 

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

# -------------------------------------
# 4. Calcul de l'escompte .
# -------------------------------------