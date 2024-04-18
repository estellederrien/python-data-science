""" 
** Introduction 

On a 1 document ,

Avant de faire des statistiques sur notre document, il faut le NETTOYER.

Cette fois ci, on utilise la librairie spécifique SPACY
Du coup, l'ordre de l'exécution n'est pas la même !
:

0. Importer le fichier .txt qui contient notre document
1. Normaliser ( Oter les majuscules, Oter la ponctuation ...)
2. Scinder le document en mots uniques - Inutile car la racinisation le fait automatiquement avec SPACY
3. Raciniser (Confondre toutes les formes d'un même mot en un seul)
4. Oter les mots inutiles / Enlever les mots les plus fréquents (articles: et , le, ce , etc ... verbes du style être avoir faire, les conjonctions: et, ou etc ...)

En anglais cela se dit :
0. Importing the .txt file
1. Normalise
2. Tokeniser  
3. Stemming
4. Removing Stop Words 

** Sources 

https://spacy.io/

https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/



 """

# 1. On importe les librairies .

# Cette lib ne fonctionne pas en python 32 bits !! :
import spacy
#  télécharger les modèles français.
nlp = spacy.load("fr_core_news_sm")


""" --------------------------------------------------------------------------------------------------
0. On importe un document TXT, avec cette méthode, on obtient 1 variable string appeleée 'docA' contenant le document
-------------------------------------------------------------------------------------------------- """

"""  
    C: Un loup a mangé un mouton, les autres loups sont restés dans la bergerie.

"""

with open('datasets/A.txt', 'r', encoding="utf-8") as file:
    docA = file.read().replace('\n', '')

""" --------------------------------------------------------------------------------------------------
1. Normaliser  ( Oter les majuscules, Oter la ponctuation ...)
-------------------------------------------------------------------------------------------------- """

# A/ oter les majuscules
docA = docA.lower()
print(docA)

# B/ oter la ponctuation ( fonction trouvée ici https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string)
import re
def remove_punctuation(pattern,phrase):
    for pat in pattern:
        return(re.findall(pat,phrase))
        return('\n')
        
# phrase='Welcome to Quora! We are happy to help you out. Need any help?'
pattern=['[^!.?]+']
phrase = docA    
docA = "".join(remove_punctuation(pattern,phrase))
print(docA)

# On obtient :
# le loup est dans la bergerie

"""
--------------------------------------------------------------------------------------------------
2.  Scinder le document en mots uniques - INUTILE CAR LA PHASE DE  STEMMING LE FAIT  !
    Tokeniser 
--------------------------------------------------------------------------------------------------  
"""

# def return_token(sentence):
#     # Tokeniser la phrase
#     doc = nlp(sentence)
#     # Retourner le texte de chaque token
#     return [X.text for X in doc]

# print(return_token(docA))
# docA = return_token(docA)


""" --------------------------------------------------------------------------------------------------
3. Raciniser (Confondre toutes les formes d'un même mot en un seul), 
   utiliser https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/
   Stemming
-------------------------------------------------------------------------------------------------- """

# Spacy ne fonctionne pas avec python 3.8 32 bits, il faut le 64
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')

def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]
print("mon stemming") 
print(return_stem(docA)) 
docA = return_stem(docA)

# on obtient :
# ['le', 'loup', 'est', 'dan', 'la', 'berger']


""" --------------------------------------------------------------------------------------------------
4. Oter les mots inutiles / Enlever les mots les plus fréquents 
    (articles: et , le, ce , etc ... verbes du style être avoir faire, les conjonctions: et, ou etc ...), c'est la façon 'naïve'
  Removing the stop words 
-------------------------------------------------------------------------------------------------- """

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopWords = set(stopwords.words('french'))

clean_words = []
for token in docA:
    if token not in stopWords:
        clean_words.append(token)

docA = clean_words
print(docA)

# on obtient :
# ['loup', 'dan', 'berger']
# on voit que le mot dans gène et est mal géré par le stemming






