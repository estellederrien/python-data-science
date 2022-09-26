""" 

Calculer une fréquence des termes (tf / idf)

TF (Term Frequency) mesure la fréquence d'un mot dans un document.

TF = (nombre de fois où le mot apparaît dans le texte) / (nombre total de mots dans le texte)

IDF (Inverse Document Frequency) mesure le rang du mot spécifique pour sa pertinence dans le texte. Les mots vides qui contiennent des informations inutiles telles que «a», «dans» et «et» ont moins d'importance malgré leur occurrence.

IDF = (Nombre total de documents / Nombre de documents contenant le mot t)

Ainsi, le TF-IDF est le produit du TF et de l'IDF:

TF-IDF = TF * IDF


La transformation Term Frequency times Inverse Document Frequency (TF ‐ IDF) est une technique utilisée pour compenser 
la longueur des différents documents. Un document court et un document long peuvent discuter des mêmes sujets, 
mais le document long aura un nombre de mots plus élevé car il contient plus de mots. 
Lorsque vous effectuez une comparaison entre le document court et long, 
le document long recevra une pondération injuste sans cette transformation. 
Les moteurs de recherche doivent souvent pondérer les documents de manière égale, 
vous voyez donc cette transformation utilisée assez souvent dans les applications des moteurs de recherche.

"""

# 0. import du dataset
from sklearn.datasets import fetch_20newsgroups 

# 1. import de la lib
import sklearn.feature_extraction.text as ext

""" Cet exemple commence un peu comme les autres exemples de cette section, en récupérant le jeu de données 20 Newsgroups. 
Il crée ensuite un sac de mots, un peu comme l'exemple de la section «Comprendre le modèle de sac de mots», 
plus haut dans ce chapitre. Cependant, vous voyez maintenant quelque chose que vous pouvez faire avec le sac de mots.
Dans ce cas, le code fait appel à TfidfTransformer () pour convertir les documents bruts de newsgroup en une matrice de fonctionnalités TF-IDF. 
Use_idf contrôle l'utilisation de la repondération de fréquence de document inverse, qu'il a désactivée dans ce cas. 
Les données vectorisées sont ajustées à l'algorithme de transformation. 
L'étape suivante, appelant tf_transformer.transform (), effectue le processus de transformation proprement dit. 
Voici le résultat que vous obtenez de cet exemple:
(593, 13564)
TF ‐ IDF vous aide à localiser le mot ou les n ‐ grammes les plus importants et à exclure les moins importants. 
Il est également très utile en tant qu'entrée pour les modèles linéaires, car ils fonctionnent mieux avec les scores TF ‐ IDF qu'avec 
le nombre de mots. À ce stade, vous formez normalement un classificateur et effectuez différentes sortes d'analyses. 
Ne vous inquiétez pas encore pour cette prochaine partie du processus. À partir des chapitres 12 et 15, vous découvrez les classificateurs. 
Au chapitre 17, vous commencez à travailler sérieusement avec les classificateurs.
 """
# 2. On filtre
categories = ['sci.space']
twenty_train = fetch_20newsgroups(subset='train',categories=categories,remove=('headers', 'footers', 'quotes'),shuffle=True,random_state=42)

# 3. On Vectorise
count_vect = ext.CountVectorizer() 
X_train_counts = count_vect.fit_transform(twenty_train.data)

# 4. On Compte
tfidf = ext.TfidfTransformer().fit(X_train_counts) 
X_train_tfidf = tfidf.transform(X_train_counts)

print (X_train_tfidf.shape)

