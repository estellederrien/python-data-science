""" 
Introduction 


On a 4 documents 

On veut calculer

1. La fréquence des termes dans chaque document tf(t,d)=nt,d avec t = terme et d = document et créer la matrice d'incidence .
La fréquence d’un terme t dans un document d est le nombre d’occurrences de t dans d . 
    1.1 Avec la lib skLearn

2. L'idf

3. la similarité cosinus.



Sources 

https://scikit-learn.org/stable/modules/feature_extraction.html

https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76

https://medium.com/@imamun/creating-a-tf-idf-in-python-e43f05e4d424



 """



# 1. On importe les librairies .

import pandas as pd
import sklearn as sk
#(seulement pour l'idf)
import math 


""" --------------------------------------------------------------------------------------------------
1. La fréquence des termes pour chaque document : tf(t,d)=nt,d avec t = terme et d = document .
1.1 Avec skLearn
-------------------------------------------------------------------------------------------------- """

# on importe la librairie

from sklearn.feature_extraction.text import CountVectorizer

# D'abord, un Premier exemple avec un tableau contnant des docs ( C'est l'exemple du site sk learn))
vectorizer = CountVectorizer()
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
X = vectorizer.fit_transform(corpus)

# Créer la matrice d'incidence , on voit qu'il y 2 fois le mot second dans le 2 ème doc
count = X.toarray()
print(count)

""" 
[[0 1 1 1 0 0 1 0 1]
 [0 1 0 1 0 2 1 0 1]
 [1 0 0 0 1 0 1 1 0]
 [0 1 1 1 0 0 1 0 1]] """

# Voir le dictionnaire créé pour comprendre la matrice d'incidence.
X = vectorizer.get_feature_names()
print(X)
# ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this'] 

# On calcule le TF
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(count)

print(tfidf.toarray())
""" 
[
 [0.         0.43306685 0.56943086 0.43306685 0.         0. 0.33631504 0.         0.43306685]
 [0.         0.24014568 0.         0.24014568 0.         0.89006176    0.18649454 0. 0.24014568]
 [0.56115953 0.         0.         0.         0.56115953 0. 0.23515939 0.56115953 0.        ]
 [0.         0.43306685 0.56943086 0.43306685 0.         0. 0.33631504 0.         0.43306685]
] 
"""


# Deuxième exemple , en prenant 4 documents .txt pour source et en les important
# Voici leur contenu :

"""  
    A: Le loup est dans la bergerie.
    B: Les moutons sont dans la bergerie.
    C: Un loup a mangé un mouton, les autres loups sont restés dans la bergerie.
    D: Il y a trois moutons dans le pré, et un mouton dans la gueule du loup. 
"""

with open('datasets/A.txt', 'r', encoding="utf-8") as file:
    docA = file.read().replace('\n', '')
with open('datasets/B.txt', 'r', encoding="utf-8") as file:
    docB = file.read().replace('\n', '')
with open('datasets/C.txt', 'r', encoding="utf-8") as file:
    docC = file.read().replace('\n', '')
with open('datasets/D.txt', 'r', encoding="utf-8") as file:
    docD = file.read().replace('\n', '')

corpus = [docA,docB,docC,docD]
print(corpus)

X = vectorizer.fit_transform(corpus)

# Créer la matrice d'incidence , on voit qu dans le doc 4 il y a 2 fois le mot 'dans' dans le 4ème doc
count = X.toarray()
print(count)
""" 
[[0 1 1 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0]
 [0 1 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0]
 [1 1 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 1 0 2]
 [0 0 2 1 0 1 1 1 1 1 0 1 0 0 1 1 1 0 0 1 1]]
 """

# Voir le dictionnaire créé pour comprendre la matrice d'incidence.
X = vectorizer.get_feature_names()
print ("Les mots présents dans mes 4 fichiers, sans doublons,  sont: ")
print(X)
# ['autres', 'bergerie', 'dans', 'du', 'est', 'et', 'gueule', 'il', 'la', 'le', 'les', 'loup', 'loups', 'mangé', 'mouton', 'moutons', 'pré', 'restés', 'sont', 'trois', 'un']


# On calcule le TF
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(count)

print(tfidf.toarray())
""" 
[[0.         0.34566437 0.26843922 0.         0.640575   0.
  0.         0.         0.26843922 0.45450711 0.         0.34566437
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.36778358 0.28561676 0.         0.         0.
  0.         0.         0.28561676 0.         0.48359121 0.
  0.         0.         0.         0.48359121 0.         0.
  0.48359121 0.         0.        ]
 [0.34385543 0.18554981 0.14409598 0.         0.         0.
  0.         0.         0.14409598 0.         0.2439757  0.18554981
  0.34385543 0.34385543 0.2439757  0.         0.         0.34385543
  0.2439757  0.         0.48795141]
 [0.         0.         0.27657592 0.32999578 0.         0.32999578
  0.32999578 0.32999578 0.13828796 0.23414187 0.         0.17807093
  0.         0.         0.23414187 0.23414187 0.32999578 0.
  0.         0.32999578 0.23414187]] """





""" --------------------------------------------------------------------------------------------------
 L'IDF
-------------------------------------------------------------------------------------------------- """


