""" 
** Introduction 

On a 2 documents textes classiques, on cherche à calculer la similarité cosinus, avec Python , par curiosité.

mon interprétation : 
La similarité cosinus  nous donne un résultat 0>x>1, plus il est élevé, plus les deux documents sont similaires.
Le premier document est généralement le vecteur requête auquel on compare des dizaines d'autres documents.


** Sources 

https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50

https://machinelearningmastery.com/develop-word-embeddings-python-gensim/

https://stackoverflow.com/questions/47728069/sklearn-cosine-similarity-for-strings-python

"""

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


Phrase1 = "AI est mon ami est a toujours été sympa"
Phrase2 = "AI et les humains ont toujours été amis"

# Voici notre fonction de vectorisation de nos variables strings
def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()

k = get_vectors(Phrase1,Phrase2)
print(k)

# Ca nous affiche l'occurence des termes dans les 2 documents
""" [[1 0 1 1 1 1 1 0 0 1 1 1]
 [1 1 1 1 0 1 0 1 1 0 0 0]]
 """

# Maintenant, on veut calculer notre similarité cosinus entre les 2 documents.

def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)
    

j = get_cosine_sim(Phrase1,Phrase2)
print(j)

""" Ca nous affiche une similarité de  0.335
[[1.        0.3354102]
 [0.3354102 1.       ]] """

""" Pour être sur que cela fonctionne, on modifie nos deux documents pour 
qu'ils se ressemblent plus, et on vérifie que la similarité cosinus change ' """

Phrase1 = "AI est mon ami est a toujours été sympa"
Phrase2 = "AI est mon ami est a toujours été sympa oui"

j = get_cosine_sim(Phrase1,Phrase2)
print(j)

""" Ca nous affiche une similarité de  0.953 , cela valide la validité de notre function
[[1.         0.95346259]
 [0.95346259 1.        ]]"""
