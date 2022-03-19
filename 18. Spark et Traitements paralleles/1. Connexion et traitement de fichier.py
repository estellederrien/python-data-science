""" 
Utiliser Spark avec le connecteur PYTHON

Sources: 
https://realpython.com/pyspark-intro/ 

"""

# 1. on importe les libs
# facultatif
import findspark
findspark.init()

from pyspark import SparkContext,SparkConf

# 2. on spécifie le contexte, en fait, on créé un RDD ( résilient data set) en mémoire ram, là c'est du local, mais normalement c'est sur un cluster/

conf = SparkConf().setAppName('testing').setMaster('local')
sc=SparkContext(conf=conf)

# 3. on importe un fichier
txt = sc.textFile('datasets/copyright.txt')

# Syntaxe Sur linux ....
# txt = sc.textFile('file:////usr/share/doc/python/copyright')

# 3. bis Si on avait voulu se connecter à un cluster, voici le code : 

""" 
conf = pyspark.SparkConf()
conf.setMaster('spark://head_node:56887')
conf.set('spark.authenticate', True)
conf.set('spark.authenticate.secret', 'secret-key')
sc = SparkContext(conf=conf) 
"""

# 4. on affiche son nombre de lignes du fichier
print("le nombre de lignes de mon ficher est de :" ,txt.count())

# 5. On filtre sur les lignes contenant le terme 'python'
python_lines = txt.filter(lambda line: 'python' in line.lower())

# 6. on affiche son nombre de lignes du résultat filtré
print("le nombre de lignes de mon ficher comprenent le terme python est de :" ,python_lines.count())

""" Vous apprendrez bientôt tous les détails de ce programme, mais regardez bien. Le programme compte le nombre total de lignes et le nombre de lignes contenant le mot python dans un fichier nommé copyright.

N'oubliez pas qu'un programme PySpark n'est pas très différent d'un programme Python standard, mais le modèle d'exécution peut être très différent d'un programme Python standard, surtout si vous exécutez sur un cluster.

Il peut y avoir beaucoup de choses qui se passent dans les coulisses qui répartissent le traitement sur plusieurs nœuds si vous êtes sur un cluster. Cependant, pour l'instant, considérez le programme comme un programme Python qui utilise la bibliothèque PySpark.

Maintenant que vous avez vu certains concepts fonctionnels communs qui existent en Python ainsi qu'un simple programme PySpark, il est temps de plonger plus profondément dans Spark et PySpark.

 """
