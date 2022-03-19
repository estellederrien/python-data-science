""" 
    Loi géométrique ou de pascal - Python géométric law with numpy

    
    Attention ce code n'est pas sur à 100% car basé sur la function RANDOM, voir le cas numéro 8 pour un meilleur code  sur les pourcentages
    En effet, faire des calculs sur les datas randoms est étrange ...


    https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.geometric.html

    AUTRES EXEMPLES :

    Un ingénieur en sécurité estime que 35% de tous les accidents industriels dans son usine sont causés par le non-respect des instructions par les employés. 
    Elle décide d'examiner les rapports d'accident (sélectionnés au hasard et replacés dans la pile après lecture) jusqu'à ce qu'elle en trouve un qui montre un 
    accident causé par le non-respect des instructions par les employés. En moyenne, combien de rapports l'ingénieur de sécurité s'attendrait-il à examiner 
    jusqu'à ce qu'elle trouve un rapport montrant un accident causé par le non-respect des instructions par un employé? 
    Quelle est la probabilité que l'ingénieur de sécurité devra examiner au moins trois rapports jusqu'à ce qu'elle trouve un rapport montrant un accident causé 
    par le non-respect des instructions par un employé?

    Soit X =
    le nombre d'accidents que l'ingénieur de sécurité doit examiner jusqu'à ce qu'elle trouve un rapport 
    indiquant un accident causé par le non-respect des instructions par l'employé. X prend les valeurs 1, 2, 3,…. 
    La première question vous demande de trouver la valeur attendue ou la moyenne. 
    La deuxième question vous demande de trouver P (x≥3)
    . («Au moins» se traduit par un symbole «supérieur ou égal à»).
  

    Un instructeur estime que 15% des étudiants obtiennent un C inférieur à leur examen final. 
    Elle décide de regarder les examens finaux (sélectionnés au hasard et replacés dans la pile après lecture) jusqu'à ce qu'elle en trouve un qui affiche une note inférieure à un C. 
    Nous voulons savoir la probabilité que l'instructeur devra examiner au moins dix examens jusqu'à ce qu'elle trouve une avec une note inférieure à C. 
    Quelle est la question de probabilité énoncée mathématiquement?

    P (x ≥ 10)
 """

 # Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problème : 
"""  
Je lance un dès à 6 côtés

Je le lance jusqu'à obtenir un 1.

La probabilité géométrique est de p = 1/6. 

Nombre de lancers = 100

"""

resultat = np.random.geometric(p=0.16, size=100)
print(resultat);

#   Dans ce tableau, on a obtenu un 1 au deuxième lancer, puis au 19 ème lancer, puis au 3ème lancer etc ...

""" [ 2 19  3  2  2  1  2  1 22  3  1  6  3  1  2 11  8 28  4  7  9  3  3  5
 18  8  2 15  6  4  4 25  3  2  2  3  4  3  3  4  7  9  2 10  1  1  6  7
  5  3  1 10  3  6  1  7  7  1 13  3  2  5  2  7  3  6 10  1  6  5  1 10
  1  1  2  3  4 10  2  4  7  6  6  2  1  3  6  7  2  3 15  7  4 10  4  5
  2 10  5 23] """

# Essayons désormais de voir le pourcentage de chances d'obtenir un 1 dès le premier lancer, pb calculée sur 100 tentatives :
succesImmediat =  (resultat == 1).sum() / 100.
print(succesImmediat * 100,"%");
# Environ 17.0 %, ça ocrrespond bien à notre pb initiale

# Essayons désormais de voir le pourcentage de chances d'obtenir un 1 au bout de 3 lancers , pb calculée sur 100 tentatives :
succesImmediat =  (resultat <= 3).sum() / 100.
print(succesImmediat * 100,"%");
# Environ 41.0 %