""" Source : Linear Programming: Introduction
de Frédéric Giroire

Note de Nicolas Estel HULEUX:
J'essaye de tirer au clair la capacité des solveurs de prendre en compte des contraintes mixant des pourcentages et 
des unités quelconques et de savoir si cela fonctionne réellement en faisant des tas de comparaisons de résultats 
sur tous les solveurs gurobi, excel, pulp et pleins d'autres ainsi que la théorie.

Exemple 1 : un problème d'allocation de ressources

Une entreprise produit des câbles en cuivre de 5 et 10 mm de diamètre sur une
ligne de production unique avec les contraintes suivantes :

• Le cuivre disponible permet de produire 21000 mètres de câble de
5 mm de diamètre par semaine.

• Un mètre de cuivre de 10 mm de diamètre consomme 4 fois plus de
cuivre qu'un mètre de cuivre de 5 mm de diamètre.

En raison de la demande, la production hebdomadaire de câble de 5 mm est limitée à
15000 mètres et la production de câble de 10 mm ne doit pas dépasser
40% de la production totale.

Les câbles sont respectivement vendus 50 et 200 euros le mètre.

Que doit produire l'entreprise pour maximiser ses revenu? 






"""