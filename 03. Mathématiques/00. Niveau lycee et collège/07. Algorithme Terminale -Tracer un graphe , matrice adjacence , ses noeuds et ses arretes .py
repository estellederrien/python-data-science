""" 

Python niveau Lycee Term / Fac:

Utiliser le module networkX pour créer des Graphs

Installer le module : #pip install networkx 

"""

# 0. import de la lib
import networkx as nx


# 1. On paramêtre le graphe 
G = nx.cycle_graph(10) 
A = nx.adjacency_matrix(G)

# 2. On Imprime la matrice d'adjacence
print(A.todense())


# 3. import de la lib
import matplotlib.pyplot as plt 

# 4. On dessine le graphe 
nx.draw_networkx(G) 
plt.show()

#5 Ajouter une arrète entre le noeud 1 et 5 
G.add_edge(1,5) 
nx.draw_networkx(G) 
plt.show()
