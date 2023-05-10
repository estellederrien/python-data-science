""" 

Python niveau Lycee Term / Fac:

Au premier janvier 2020, Philippe vient de se faire embaucher pour un salaire net mensuel de 1 500 €
 dans une entreprise qui a mis en place la règle d'évolution des salaires suivante : 
 chaque mois, les salaires mensuels sont augmentés de 0,2 % puis de 2 €. 
 Donc le salaire net mensuel de Philippe au mois de février 2020 sera de 1,002 x 1 500 + 2 = 1505 €,puis de 1,002 x 1505 + 2 = 1510,01 €
 au mois de mars, etc. Déterminer le mois et l'année à partir desquels le salaire net mensuel de Philippe
 dépassera 2 000 €.

Calculer modulo :
Méthode 2: Effectuer la division entière et calculer la valeur de la différence.

Exemple : Calcul de A=123modN=4 , faire la division : 123/4=30.75. Récupèrer la partie entière : 30, 
la multiple par N=4 : 30×4=120. La différence entre 123 et 120 vaut 3, donc 123%4=3.

#  NOTE : JE N'AIME PAS


"""

# 0. import de la lib
import numpy as np


#########################Fonctions############################# 

def s(n) : 
    if n == 1 : 
        return(1500) 
    else : 
        return ( s (n-1) * 1.002 + 2 ) 

# Affiche le mois 
def mois(n) : 
    L = ['janvier ','février',' mars', 'avril' , 'mai' , 'juin' , 'juillet' , 'aout' , 'septembre' , 'octobre' , 'novembre' , 'decembre' ] 
    n = ( n - 1 ) % 12 
    return(L[n])

def annee(n): 
    a = 2020 + (n - 1) // 12 
    return (a) 

#################### Partie principale ######################### 
N = 1
while s(N) <= 2000 :
     N = N + 1 
print("Le salaire de Philippe dépasse 2000 euros au mois de : ", mois(N), annee(N), " . " ) 
# Le salaire de Philippe dépasse 2000 euros au mois de :  septembre 2027  .

