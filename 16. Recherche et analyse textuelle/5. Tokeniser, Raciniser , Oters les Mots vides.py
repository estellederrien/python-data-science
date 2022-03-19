""" 
** Introduction 

On a 1 document ,

Avant de faire des statistiques sur notre document, il faut le NETTOYER :

0. Importer le fichier .txt qui contient notre document
1. Normaliser ( Oter les majuscules, Oter la ponctuation ...)
2. Oter les mots inutiles (articles: et , le, ce , etc ... verbes du style être avoir faire, les conjonctions: et, ou etc ...)
3. Raciniser (Confondre toutes les formes d'un même mot en un seul)
4. Scinder le document en mots uniques

En anglais cela se dit :
0. Importing the .txt file
1. Normalise
2. Removing Stop Words 
3. Stemming
4. Tokeniser 

** Sources 


http://docs.cltk.org/en/latest/french.html

https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/

 """

# 1. On importe les librairies .

# Cette lib sert pour le stemming, elle ne fonctionne pas en python 32 bits !! :
import spacy
nlp = spacy.load("fr_core_news_sm")
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')


""" --------------------------------------------------------------------------------------------------
0. On importe un document TXT, avec cette méthode, on obtient 1 variable string contenant le document
-------------------------------------------------------------------------------------------------- """

"""  
    C: Un loup a mangé un mouton, les autres loups sont restés dans la bergerie.

"""

with open('datasets/A.txt', 'r', encoding="utf-8") as file:
    docA = file.read().replace('\n', '')




""" --------------------------------------------------------------------------------------------------
1. Normaliser ( Oter les majuscules, Oter la ponctuation ...)
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


""" --------------------------------------------------------------------------------------------------
2. Oter les mots inutiles (articles: et , le, ce , etc ... verbes du style être avoir faire, les conjonctions: et, ou etc ...), c'est la façon 'naïve'
  Removing the stop words - https://stackoverflow.com/questions/36808940/how-to-remove-stop-words-using-string-replace
-------------------------------------------------------------------------------------------------- """

liste_noire = ["le", "la", "ce", "et", "ou"]  # La Liste noire des mots à suprimer, les stop words
for mot in liste_noire:
    docA = docA.replace(" " + mot + " ", " ")


""" --------------------------------------------------------------------------------------------------
3. Raciniser (Confondre toutes les formes d'un même mot en un seul), 
   utiliser https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/
   Stemming
-------------------------------------------------------------------------------------------------- """

# Spacy ne fonctionne pas avec python 3.8 32 bits, il faut le 64

def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]

return_stem(docA) 




"""  --------------------------------------------------------------------------------------------------
4. Scinder le document en mots uniques - Tokeniser ( Il faudrait plutôt le faire avec nltk), c'est la façon 'naïve'
--------------------------------------------------------------------------------------------------  """
docA = docA.split() 
print(docA)



