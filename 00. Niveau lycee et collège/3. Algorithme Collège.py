""" Python niveau collège 3eme :
Roger dispoe d'un budget de 40 euros et va dans un magasin ou chaque clef usb coute 10.90 E 
et chaque dvd 0.80 euros .
Prévenir quand Roger a dépassé son budget . """


# 1. initialisation des variables
PrixDvd = 0.80 # A floating point
PrixUsb = 10.90 
budget = 30
facture = 0

# 2. initialisation des variables

nbUsb = float(input("ENtrez Nombre de clefs usb achetées : "))
nbDvd = float(input("Entrez Nombre de dvds achetés : "))

facture =  PrixUsb * nbUsb + PrixDvd * nbDvd  

if (facture > budget):
    print("Ton budget de 30 euros est dépassé")

print(facture, " euros")

