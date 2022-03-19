""" 
On a un dataset comprenant un vecteur x avec des valeurs numériques
et un vecteur y avec des valeurs numériques.

L'algo KMean ou Kmoyenne permet de "regrouper" les valeurs similaires en groupes (clusters). 
Cahque cluster dispose alors d'un 'centroid' qui est la moyenne des valeurs X,Y présentes dans chaque clusters.

Source :
https://datatofish.com/k-means-clustering-python/
"""

# 1. on importerla lib 
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 2. On crée notre dataset
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       }
  
df = DataFrame(Data,columns=['x','y'])
print (df)

# 3. On utilise l'algoritme KMEANS pour créer nos 3 clusters et repérer nos centroids.
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()