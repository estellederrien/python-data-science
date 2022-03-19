""" 
Chaine de Markov à temps discrets

On veut prévoir le trajet d'une souris amnésique .
Celle ci se déplace dans un graphe dont les arrêtes sont valuées par des probabilités.

Source : 
EICNAM
RCP 103 - Kamel Barkaoui

 """

# 0. On charge la librairie
import numpy as np


# 1. En introduction, On Définit notre fonction qui va calculer une puissance d'une matrice de transition
def matrixMul(a, n):
    if(n <= 1):
        return a
    else:
        return np.matmul(matrixMul(a, n-1), a)

# 2. On crée la ** matrice de transition ** de notre graphe markov discret, celle ci comprends la probabilité de passer d'un état à un autre.
""" 
La probabilité  de rester à Lausanne est de  : 0.8 
La probabilité  de déménagement  de Lausanne à Genève est de  : 0.2 
La probabilité  de déménagement  de Genève à Lausanne: 0.1 
La probabilité  de rester  à Genève  est de : 0.9  
"""
transition_matrix = [[0.8,0.2], [0.1,0.9]]

# 3. On précise le nombre d'états qui va nous donner notre probabilité.
nombre_etats = 3

# 4. On calcule notre matrice à la puissance nombre_etats
transition_matrix_power = matrixMul(transition_matrix,nombre_etats)

print(transition_matrix_power )

# 5. On crée le ** vecteur de probabilités de l'état initial **
# 20% de la popuplation est sur Lausanne et 80% sur Genève, on peut aussi le mettre n personnes
probabilite_0 = np.array([2000,8000]) 

# 4. On calcule les probabilités de l'état du système en fonction du nombre de temps.

""" 
Etat du système après une période de temps  = P1 = probabilité_0 . transition_matrix
Etat du système après 2 période de temps  = P2 = probabilité_0 . transition_matrix ** 2
Etat du système après 3 période de temps  = P3 = probabilité_0 . transition_matrix ** 3 -> c'est celle qu'on a choisi de calculer.
Etat du système après n période de temps  = Pn = probabilité_0 . transition_matrix ** n
"""

c = np.dot(probabilite_0,transition_matrix_power) 

print(c)
# [2876. 7124.]


""" 

CE CODE NE FONCTIONNE PAS, LE NP POWER NE DONNE PAS LA BONNE MATRICE DE TRANSITION ELEVEE AU CUBE CEST PAS CORRECT, je ne sais pas pourquoi  !
transition_matrix = np.array([[0.8,0.2], 
[0.1,0.9]])
transition_matrix_cube = np.power(transition_matrix, 3)
print(transition_matrix_cube) 

"""