""" 
Source : https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial 

Les chaînes de Markov ont une utilisation prolifique en mathématiques. Ils sont largement employés en économie, en théorie des jeux, 
en théorie de la communication, en génétique et en finance. 

Ils se posent largement dans les statistiques statistiques spécialement bayésiennes et les contextes théoriques de l'information. 
Lorsqu'il s'agit de problèmes du monde réel, ils sont utilisés pour postuler des solutions pour étudier les systèmes de régulateur de vitesse 
dans les véhicules à moteur, les files d'attente ou les files de clients arrivant à un aéroport, les taux de change des devises, etc. 

L'algorithme connu sous le nom de PageRank, qui a été initialement proposé pour le moteur de recherche Internet Google, est basé sur un processus 
de Markov. Le Subreddit Simulator de Reddit est un subreddit entièrement automatisé qui génère des soumissions et des commentaires aléatoires 
à l'aide de chaînes de Markov, tellement cool!

il vous suffit de connaître l'état actuel pour déterminer l'état suivant

"""



""" 
Phase 1 :

On récupère des statistiques suivantes :

Quand Cj est triste, ce qui n'est pas très courant: elle va courir, goûte la glace ou fait une sieste.

D'après les données historiques, si elle a passé une triste journée à dormir. Le lendemain, il est probable à 60% qu'elle ira courir, à 20% elle restera au lit le lendemain et à 20% de chances qu'elle se raccroche à la crème glacée.

Quand elle est triste et va courir, il y a 60% de chances qu'elle aille courir le lendemain, 30% qu'elle se gorge de glace et seulement 10% de chances qu'elle passe son sommeil le lendemain.

Enfin, quand elle s'adonne à la crème glacée un jour triste, il y a à peine 10% de chances qu'elle continue d'avoir de la crème glacée le lendemain également, 70% elle est susceptible d'aller courir et 20% de chance qu'elle passe à dormir le lendemain journée.

 
On peut alors créer un diagramme de 3 états :

dormir, courir et crême glacée .
                état suivant
dormir          0.2     0.6     0.2
courir          0.1     0.6     0.3
creme glacée    0.2     0.7     0.1

comment et où pouvez-vous utiliser ces théories dans la vraie vie?

Avec l'exemple que vous avez vu, vous pouvez maintenant répondre à des questions telles que: 
"A partir de l'état: dormir, quelle est la probabilité que Cj s'exécute (état: courir) à la fin d'une triste durée de 2 jours?"

Travaillons celui-ci: Pour passer de l'état: sommeil à état: exécuter, Cj doit soit rester à l'état: 
dormir le premier mouvement (ou jour), puis passer à l'état: exécuter le prochain (deuxième) mouvement (0,2 ⋅
0,6); ou passer à l'état: courir le premier jour puis y rester le deuxième (0,6 ⋅ 0,6) 
ou elle pourrait passer à l'état: glace au premier mouvement puis à l'état: courir le second (0,2 ⋅ 0,7). 
Donc la probabilité: ((0,2 ⋅ 0,6) + (0,6 ⋅ 0,6) + (0,2 ⋅ 0,7)) = 0,62. 
Donc, nous pouvons maintenant dire qu'il y a 62% de chances que Cj passe à l'état: 
courir après deux jours de tristesse, si elle a commencé dans l'état: dormir.
"""


""" 
Phase 2 : 
Import des librairies
"""

import numpy as np
import random as rm



""" 
Phase 3 :
Créer l'espace des états : il y en a 3 .
"""

# espace des états
states = ["Sleep","Icecream","Run"]

# Séquences d'évents
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# Matrice de transition de probabilités
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

# Controle que chaque ligne des transitions de probabilités soient égales à 3 (1+1+1)
if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Erreur dans la matrice de transition")
else: print("Tout est bon, on peut aller plus loin ;)")



""" 
Phase 4 :

On génére une transition d'état aléatoire ( random )
Et on affiche la probabilité qu'une telle transition ait lieu 
NOTE : Je n'aime pas ce code.

"""
# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sleep"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
        i += 1  
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)

# Exemple de résultat : 

""" 
Start state: Sleep
Possible states: ['Sleep', 'Sleep', 'Run']
End state after 2 days: Run
Probability of the possible sequence of states: 0.12 
"""