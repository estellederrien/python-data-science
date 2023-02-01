"""

Chaines de markov à 3 états qui prédit le temps ! :
Soleil, Pluvieux, Neigeux

La matrice stochastique contient les probabilités de passer d'un état à un autre .
Important : Elle se lit de ligne en ligne, et pas de colonne en colonne, sinon, on ne comprends pas.

TEST D UNE CLASSE TROUVEE SUR INTERNET

Source : https://www.upgrad.com/blog/markov-chain-in-python-tutorial/

"""

# 1. On charge la librairie
import numpy as np

# 2. On créee une classe python qui comprends 3 functions, qui au final vont nous faire une prédiction en fonction du nb d'états.
class MarkovChain(object):
    def __init__(self, transition_matrix, states):
        """
       Initialisez l'instance MarkovChain.
 
        Paramètres
        ----------
        transition_matrix: tableau 2D
            Un tableau 2D représentant les probabilités de changement de
            dans la chaîne de Markov.
 
        états: tableau 1-D
            Un tableau représentant les états de la chaîne de Markov. Il
            doit être dans le même ordre que transition_matrix.
        "" "


        """
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {self.states[index]: index for index in 
                           range(len(self.states))}
        self.state_dict = {index: self.states[index] for index in
                           range(len(self.states))}
 
    def next_state(self, current_state):
        """
        Renvoie l'état de la variable aléatoire la prochaine fois
        exemple.
 
        Paramètres
        ----------
        current_state: str
            L'état actuel du système.
        """
        return np.random.choice(
         self.states, 
         p=self.transition_matrix[self.index_dict[current_state], :]
        )
 
    def generate_states(self, current_state, no=10):
        """
       Génère les prochains états du système.
 
        Paramètres
        ----------
        current_state: str
            L'état de la variable aléatoire actuelle.
 
        non: int
            Le nombre d'états futurs à générer.
        """
        future_states = []
        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states

""" 
En dessous, on voit la ligne 1 de la matrice de probabilités de transition qui concerne l'état SUNNY : 
La prob qu'il reste sunny a l'état n+1 est de 0.8
La prob qu'il devienne Rainy a l'état n+1 est de 0.19
La prob qu'il devienne Snowy a l'état n+1  est de 0.01
On lit les probabilités ligne par ligne et on peut recréer le diagramme saggital comme cela . 
La ligne 2 concerne les probabilités de l'état Rainy, on voit que la pb que l'état rainy perdure 1 état est de 0.2
"""


transition_matrix = [[0.8, 0.19, 0.01], """ SUNNY """
[0.2,  0.7,  0.1], """ RAINY """
[0.1,  0.2,  0.7]]  """ SNOWY """

weather_chain = MarkovChain(transition_matrix=transition_matrix,states=['Sunny', 'Rainy', 'Snowy'])

# On lance la chaine de markov sur un état pour avoir l'état suivant, qui sera calculé en fonction de la probabilité , vu qu'elle est de 0.8, on obtient la plupart du temps SUNNY.
print(weather_chain.next_state(current_state='Sunny'))


# On lance la chaine de markov sur un état  pour avoir l'état suivant, qui sera calculé en fonction de la probabilité , la probabilité est que ca reste snowy à 70%.
print(weather_chain.next_state(current_state='Snowy'))

# 10 est le nombre d'états qu'on veut prédire, vu qu'on commence par Rainy, on a 0.7 de chances de de rester sur l'état RAINY  (On lit la matrice de LIGNES EN LIGNES).
print(weather_chain.generate_states(current_state='Rainy', no=10)) 
