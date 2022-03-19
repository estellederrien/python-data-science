""" 
Classification de fromages

Cours :
Institut de Mathématiques de Bordeaux - Université de Bordeaux
http://www.math.u-bordeaux.fr/~mchave100p/teaching/
TP3 [sujet][fromage.txt][correction algos à la main]


SOURCE : 

Classification automatique sous python de Ricco Rakotomalala :

"Ce document retranscrit une démarche de classification automatique d’un ensemble de fromages  
(29 observations) décrits par leurs propriétés  nutritives (ex. protéines, lipides, etc. ; 9 variables).  
L’objectif est d’identifier des groupes de fromages homogènes, partageant des caractéristiques similaires.
Nous utiliserons essentiellement deux approches  en nous appuyant sur deux procédures des packages spécialisés 
pour Python: la classification ascendante hiérarchique (CAH – Package SciPy) ;  
la méthode des centres mobiles (k-Means – Package Scikit-Learn)."


http://eric.univ-lyon2.fr/~ricco/cours/

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# PARTIE 1 : VISUALISATION DES DATAS
#importation des données 
import pandas as pd
fromage = pd.read_table("datasets/fromage.txt",sep="\t",header=0,index_col=0)

#dimension des données 
print(fromage.shape)

#statistiques descriptives 
print(fromage.describe())

# graphique - croisement deux à deux des variables 
# Ca nous permet de connaitre le taux de correlation linéaire entre deux colonnes 
from pandas.plotting import scatter_matrix 
scatter_matrix(fromage,figsize=(9,9))
plt.show()


# PARTIE 2 : Classification ascendante hiérarchique
# A Le dendrogramme permet de suggérer la future classification.
#librairies pour la CAH from matplotlib 
from scipy.cluster import hierarchy

#générer la matrice des liens 
Z = hierarchy.linkage(fromage,method='ward',metric='euclidean')

#affichage du dendrogramme sans couleurs
plt.title("CAH") 
hierarchy.dendrogram(Z,labels=fromage.index,orientation='left',color_threshold=0) 
plt.show()







# B Découpage en classes – Matérialisation des groupes 
# **************NOTE NICO fcluster LES GROUPES NE CORRESPONDENT PAS A CEUX VUS SUR LE PDF***************** 

#matérialisation des 4 classes (hauteur t = 7) 
plt.title('CAH avec matérialisation des 4 classes') 
hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
hierarchy.dendrogram(Z,labels=fromage.index,orientation='right') 
plt.show()

#découpage à la hauteur t = 7 ==> identifiants de 4 groupes obtenus 
from scipy.cluster.hierarchy import fcluster
groupes_cah = fcluster(Z,t=7,criterion='distance') 
print('groupes')
print(groupes_cah)

#index triés des groupes 
idg = np.argsort(groupes_cah)
print(idg)

#affichage des observations et leurs groupes 
print('observations')
print(pd.DataFrame(fromage.index[idg],groupes_cah[idg]))
pd.DataFrame(fromage.index[idg],groupes_cah[idg])
plt.show()


# C Méthode des centres mobiles KMEANS
# k-means sur les données centrées et réduites 
# **************NOTE NICO les groupes crées ne correspondent pas à ceux du document PDF**************** 
from sklearn import cluster

fromage = pd.read_table("datasets/fromage.txt",sep="\t",header=0,index_col=0)
kmeans = cluster.KMeans(n_clusters=4) 
kmeans.fit(fromage)

#index triés des groupes 
idk = np.argsort(kmeans.labels_)

#affichage des observations et leurs groupes 
print(pd.DataFrame(fromage.index[idk],kmeans.labels_[idk]))

#distances aux centres de classes des observations 
print(kmeans.transform(fromage))

#correspondance avec les groupes de la CAH 
pd.crosstab(groupes_cah,kmeans.labels_)





