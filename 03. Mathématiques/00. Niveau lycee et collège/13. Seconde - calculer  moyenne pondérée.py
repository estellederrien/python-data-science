""" 

Python niveau 2nde :

Moyenne pondérée

"""


# 1. Moyenne pondérée

print(" Nous allons calculer la moyenne pondérée d'une série que vous allez entrer ")

# Initialisation
valeurs = []
effectifs = []
val_eff = []
n = 0

while n != "fin":
    n = input(("Entrer valeur de la série  ou écrire Fin si il n'y a plus de valeur à entrer: \n"))
    if n != "fin":
        n = float(n)
        valeurs.append(n)

for i in range (len(valeurs)):
    print("Entrer l\'effectif correspondant à la valeur: ",valeurs[i])
    n  = int(input())
    effectifs.append(n)

for i in range (len(valeurs)):
    val_eff.append(valeurs[i]*effectifs[i])

m = sum(val_eff) / sum(effectifs)

print("La moyenne pondérée de votre série est  ", m)

