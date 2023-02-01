""" 
Quelles est la probabilité qu'un chien paresseux se lève pour manger (état2) alors qu'il est couché (état 1)  ?

Source : http://www.blackarbs.com/blog/introduction-hidden-markov-models-python-networkx-sklearn/2/9/2017

Les chaines de markov n'ont pas de mémoire des états antérieurs (Memory less). 

"""



""" 
Phase 1 : 
Import des librairies
pip install pydot
pip install graphviz
python -m pip install --upgrade pip

"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

""" 
Phase 2 :

Créer l'espace des états : il y en a 3 .
Créer la probabilité initiale de chaque état . 
35 %, 35 % et 30 %

"""

etats = ['dormir', 'manger', 'defequer']
pi = [0.35, 0.35, 0.3]

espace_etats = pd.Series(pi, index=etats, name='etats')

print(espace_etats)

# La somme des probabilités est égale à 1 .
print(espace_etats.sum()) 

""" 
Phase 3 :

On définit les probabilités de transition .

Ce sont les probabilités de rester dans le même état ou d'obtenir un nouvel état, quand on connait l'état actuel .

La matrice est de taille (M * M) ou M est le nombre d'états .

"""

q_df = pd.DataFrame(columns=etats, index=etats)
q_df.loc[etats[0]] = [0.4, 0.2, 0.4]
q_df.loc[etats[1]] = [0.45, 0.45, 0.1]
q_df.loc[etats[2]] = [0.45, 0.25, .3]

# On imprime notre tableau avec les 3 états .
print(q_df)

q = q_df.values
print('\n', q, q.shape, '\n')

# La somme des probabilités par ligne est de 1
print(q_df.sum(axis=1))


""" 
Phase 4 :

On crée le diagramme de markov avec la lib networkX

NetworkX crée des graphiques avec des noeuds et des arrêtes.

Dans l'exemple, les états possibles du chien sont des noeuds, et les arrêtes, les connexions .

Les probabilités des transitions sont les poids des arrêtes .

Elles représentent la probabilit éde transitionner de l'état actuel à un état donné.


"""


from pprint import pprint 

# Créer une fonction qui mappe les valeurs de probabilités aux poids des arrêtes du graphe .


def _get_markov_arretes(Q):
    arretes = {}
    for col in Q.columns:
        for idx in Q.index:
            arretes[(idx,col)] = Q.loc[idx,col]
    return arretes

arretes_wts = _get_markov_arretes(q_df)

# On affiche toutes les valeurs des poids des arrêtes ( Ce sont les probabilités de transitions d'un état à l'autre)
pprint(arretes_wts)


""" 
Phase 5 :

Maintenant, on peut créer le graphe .

Pour visualiser le modè-le de Markov, on utilise la function  use nx.MultiDiGraph()

Un multidigraph est simlement un graphe orienté, qui peut avoir des multiples arrêtes (arcs) et des boucles.

Dans le code suivant, nous créons l'objet graphique, ajoutons nos nœuds, bords et étiquettes, 

puis dessinons un mauvais tracé networkx lors de la sortie de notre graphique vers un fichier de points.


"""
# Crer l'objet graph
G = nx.MultiDiGraph()

# les noeuds correspondent aux états du chien qu'on a défini au début du programme
G.add_nodes_from(etats)
print(f'Nodes:\n{G.nodes()}\n')

# Les arrêtes représentent les probabilités de transitionner d'un état à l'autre 
# Edges represent transition probabilities
for k, v in arretes_wts.items():
    tmp_origin, tmp_destination = k[0], k[1]
    G.add_edge(tmp_origin, tmp_destination, weight=v, label=v)
print(f'Edges:')

""" On affiche les arrêtes et leurs poids (probabilités de passer d'un état à l'autre) """
pprint(G.edges(data=True))    
# Edges (Arrêtes):
# OutMultiEdgeDataView([('dormir', 'dormir', {'weight': 0.4, 'label': 0.4}), ('dormir', 'manger', {'weight': 0.2, 'label': 0.2}), ('dormir', 'defequer', {'weight': 0.4, 'label': 0.4}), ('manger', 'dormir', {'weight': 0.45, 'label': 0.45}), ('manger', 'manger', {'weight': 0.45, 'label': 0.45}), ('manger', 'defequer', {'weight': 0.1, 'label': 0.1}), ('defequer', 'dormir', {'weight': 0.45, 'label': 0.45}), ('defequer', 'manger', {'weight': 0.25, 'label': 0.25}), ('defequer', 'defequer', {'weight': 0.3, 'label': 0.3})])

# Maintenant, on se sert de la lib graphiviz pour générer le graphique   ( le graphe ne s'affiche pas sous mon win 10)
pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')
nx.draw_networkx(G, pos)
plt.show()


# On crée les titres des états pour Jupiter mais ce n'est pas nécessaire
edge_labels = {(n1,n2):d['label'] for n1,n2,d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G , pos, edge_labels=edge_labels)

# On mets ça dans un fichier word ( le graphe ne s'affiche pas sous mon win 10)
nx.drawing.nx_pydot.write_dot(G, 'pet_dog_markov.dot')
plt.show()

