""" 
** Introduction 

On a 2 documents, on cherche à calculer la similarité cosinus, avec Python , par curiosité.

mon interprétation : 
La similarité cosinus calcule combien les angles des vecteurs de documents sont proches sans tenir compte de la longueur des vecteurs .
Pour effectuer le calcul, on a toujours un vecteur requête.
La similarité cosinus  nous donne un résultat 0>x>1, plus il est élevé, plus les deux documents sont similaires.
Le premier document est généralement le vecteur requête à qui l'on compre des dizaines d'autres documents.


** Sources 


https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

https://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists

"""

from scipy import spatial

dataSetI = [3, 45, 7, 2]
dataSetII = [2, 54, 13, 15]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
print(result)

# Le score de la distance entre les 2 tableaux est 
# 0.972284251712350
# C'est un score qui prouve que les deux documents sont relativement similaires.

dataSetI = [3, 45, 7, 2]
dataSetII = [120, 3, 153, 154]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
print(result)

# Le score de la distance entre les 2 tableaux est 
# 0.16536773896100232
# C'est un score qui prouve que les deux documents sont différents.