""" 

    Calculer une fréquence des termes (tf / idf)

    TF (Term Frequency) mesure la fréquence d'un mot dans un document.

    TF = (nombre de fois où le mot apparaît dans le texte) / (nombre total de mots dans le texte)

    IDF (Inverse Document Frequency) mesure le rang du mot spécifique pour sa pertinence dans le texte. Les mots vides qui contiennent des informations inutiles telles que «a», «dans» et «et» ont moins d'importance malgré leur occurrence.

    IDF = (Nombre total de documents / Nombre de documents contenant le mot t)

    Ainsi, le TF-IDF est le produit du TF et de l'IDF:

    TF-IDF = TF * IDF

    SOURCE : https://iyzico.engineering/how-to-calculate-tf-idf-term-frequency-inverse-document-frequency-from-the-beatles-biography-in-c4c3cd968296


"""


# 1. import des libs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
import re

# 2. import du dataset
file = open("datasets/beatles_biographie.txt","r") 

# 3. Séparation en phrases
sentences = list()
for line in file:
    for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
        if l:
            sentences.append(l) 
print(sentences)

# 4. Véctorisation en tenant compte des stop words
cvec = CountVectorizer(stop_words='english', min_df=3, max_df=0.5, ngram_range=(1,2))
sf = cvec.fit_transform(sentences)

# 5. Phase de calcul
transformer = TfidfTransformer()
transformed_weights = transformer.fit_transform(sf)
weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': cvec.get_feature_names(), 'weight': weights})
weights_df.sort_values(by='weight', ascending=False).head(10) 

# 6. Affichage du poid de  mots .
print(weights_df)