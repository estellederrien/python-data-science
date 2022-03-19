""" 

Python niveau 2nde :

Moyenne, Médiane, Quartile

"""

# 1. Moyenne
print(" Nous allons calculer la moyenne des notes que vous allez entrer ")

liste = []
n = 0
while n != "fin":
    n = input(("Entrer une note ou écrire Fin si il n'y a plus de note à entrer: \n"))
    if n != "fin":
        n = float(n)
        liste.append(n)
print("Vous avez entré ",len(liste)," notes")
m = sum(liste)/len(liste)
print("La moyenne de votre série est ",m)



# 2. Médiane
print(" Nous allons calculer la médiane des notes que vous allez entrer ")

liste = []
n = 0
while n != "fin":
    n = input(("Entrer valeur de la série  ou écrire Fin si il n'y a plus de note à entrer: \n"))
    if n != "fin":
        n = float(n)
        liste.append(n)

liste.sort()
# SI LE TOTAL DE NOMBRES RENTRE EST PAIR
if len(liste) %2 == 0 :
    print(liste)
    k = liste[(len(liste) -1 ) // 2] 
    g = liste[len(liste) // 2]

    m = (k + g ) / 2
# SI LE TOTAL DE NOMBRES RENTRE EST IMPAIR
else :
    m=liste[len(liste)//2]

print("Vous avez entré ",len(liste)," valeurs")

print("La médiane de votre série est ",m)


# 3. Quartile

print(" Nous allons calculer les  1er et 3 ème quartiles de la série que vous allez entrer ")

liste = []
n = 0
while n != "fin":
    n = input(("Entrer valeur de la série  ou écrire Fin si il n'y a plus de valeur à entrer: \n"))
    if n != "fin":
        n = float(n)
        liste.append(n)

liste.sort()

if len(liste) %4 == 0 :

   Q1 = liste[len(liste)//4-1]
   Q3 = liste[3*len(liste)//4-1]


else :
   Q1 = liste[len(liste)//4]
   Q3 = liste[3*len(liste)//4]

print("Le premier quartile de la série est  ",Q1)
print("Le troisieme quartile de la série est  ",Q3)
