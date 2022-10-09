
# Source : https://towardsdatascience.com/4-steps-to-easily-allocate-resources-with-python-bin-packing-5933fb8e53a9

# Librarie : https://pypi.org/project/binpacking/

''' 0. Une brève introduction au problème

Supposons que vous ayez m articles de poids (ou de valeur) différents que vous devez placer dans 

n bacs équilibrés égaux (Fig.1).

C'est ce qu'on appelle généralement le problème d'emballage du bac.

Le BPP est classé par la théorie de la complexité computationnelle comme un problème 

NP-difficile qui, pour faire court, est aussi difficile que le problème le plus difficile à résoudre en temps 

polynomial non déterministe (problème NP).

Très simple, n'est-ce pas ? … 

Bien que ces mots puissent sembler à la limite de la compréhension 

(je peux vous jurer qu'il n'y a pas de fautes de frappe dans les phrases précédentes), 

le problème de Bin Packing se produit souvent dans la vie quotidienne.

Voici quelques exemples:

    Vous êtes au supermarché. Vous venez de payer et vous devez mettre tous les m produits dans le plus 
    petit nombre de n sacs en essayant de les remplir au maximum et de manière équilibrée.

    👔 Vous êtes un chef de projet qui a besoin de doter m ressources pour n projets. 
    En supposant des projets tout aussi complexes, votre objectif sera - probablement - 
    d'atteindre des groupes équilibrés en connaissant une valeur de contribution estimée de vos ressources.

    🚣‍♂️ Vous prévoyez une sortie en bateau avec des amis. Malheureusement, les bateaux ont une charge maximale. 
    Vous devrez forcément répartir vos m amis à parts égales sur les n bateaux à votre disposition.

Oui. Comme son nom l'indique, le problème de l'emballage des bacs survient chaque fois que nous devons « remplir » 
quelque chose avec autre chose.

Comme vous pouvez l'imaginer, il existe des variantes à n dimensions qui prennent en compte 
d'autres informations utiles telles que le volume ou le coût (problème du sac à dos).

'''

''' 1. Il est temps de mettre la table : le pack binpacking

Commençons à chauffer les moteurs. Nous allons utiliser uniquement ces deux packages :

    matplotlib : le package de visualisation ultra populaire ;
    binpacking : un package de résolution de problèmes de binpacking gourmand ;

Pour les installer, tapez simplement ceci dans l'invite de commande 💻 :

pip installer binpacking matplotlib

Et voilà. Fait! '''

import binpacking
import matplotlib.pyplot as plt

 

''' les paramètres

Voici une de mes étapes préférées : la définition des paramètres.

🗑️ Définissons d'abord le nombre de bacs que nous voulons, puis le dictionnaire contenant 

la valeur estimée/mesurée des ressources à notre disposition.

Nous aurons 21 ressources à doter de 6 projets. 👨👩👧👦 '''



# Number of desidered equal balanced bins
numberOfBins = 6

# Your dictionary of Resources:
#   - Key: Resource name
#   - Value: Resource contribution value
resources = {
    "A" : 5, "B" : 5, "C" : 3, "D" : 4, 
    "E" : 4, "F" : 1, "G" : 4, "H" : 5, 
    "I" : 4, "L" : 3, "M" : 3, "N" : 4,
    "O" : 3, "P" : 2, "Q" : 3, "R" : 1,
    "S" : 5, "T" : 2, "U" : 5, "V" : 3,
    "Z" : 1,
}
# A chaque clé du dictionnaire correspondra l'estimation de la valeur de contribution de cette ressource. 

# Oui, une sorte de score.


''' 
4. Déballez le problème d'emballage du bac

Compte tenu de l'extrême complexité de la recherche de la solution optimale dans les problèmes NP-difficiles, 

nous ne pourrions pas réussir sans une approche gloutonne. 

Ici entre en jeu le paquet binpacking.

   Les algorithmes gloutonnes permettent d'arriver à des solutions de problèmes difficiles 
   
   de manière approximative mais acceptable. Bref, avec des approches gourmandes, 
   
   on paie la solution du problème au détriment de sa précision.

D'accord, j'aime ça. C'est pour nous. ✌️

L'utilisation du pack est extrêmement simple. '''



groups = binpacking.to_constant_bin_number(resources, numberOfBins)
print("##########Groups")
print(groups)

# prints:
# [
#   {'A': 5, 'E': 4, 'Q': 3},
#   {'U': 5, 'G': 4, 'P': 2, 'F': 1},
#   {'B': 5, 'N': 4, 'T': 2, 'R': 1},
#   {'S': 5, 'C': 3, 'L': 3, 'Z': 1},
#   {'H': 5, 'M': 3, 'V': 3},
#   {'I': 4, 'D': 4, 'O': 3}
# ]

# chaque ligne est un conteneur et on voit ce qu'il contient ainsi que la valeur de ce qu'il contient

''' Fait! Incroyablement indolore. Essayons de visualiser le résultat d'une manière différente

 en nettoyant les valeurs à l'aide d'une compréhension de liste.

 '''

resourcesPerGroups = [list(group.keys()) for group in groups]
print("##################resourcesPerGroups")
print(resourcesPerGroups)
# prints
# [
#  ['A', 'E', 'Q'], 
#  ['U', 'G', 'P', 'F'],
#  ['B', 'N', 'T', 'R'],
#  ['S', 'C', 'L', 'Z'],
#  ['H', 'M', 'V'],
#  ['I', 'D', 'O']
#]
''' Nous avons doté toutes les ressources et créé 6 groupes (probablement) équilibrés.

D'accord, mais il est maintenant temps de voir comment l'algorithme a fonctionné. 

Voyons si les groupes sont vraiment équilibrés entre eux.

5. Explorons les résultats

Ce que nous attendons, ce sont 6 groupes chacun avec une valeur totale très proche 

de la somme des valeurs totales divisée par le nombre de groupes.

Il est donc facile de calculer la valeur idéale par groupe et les valeurs des groupes trouvés.'''
print("##################ressources values")
np =  list(resources.values())
print(np)

# Ideal average desired value , La valeur moyenne que l'on voudrait placer dans caque container
idealValue = (sum(np) / numberOfBins)    #    11.666
print("##################idealValue")
print(idealValue)


# Value of the groups obtained - On regarde la valeur totale des objets dans chaque container 
realValues = [sum(list(group.values())) for group in groups]
print("##################irealValues")
print(realValues)

''' Voici le graphique : 

la ligne horizontale rouge représente la valeur moyenne 

idéale souhaitée pour chaque groupe (Fig.2). '''

fig, ax = plt.subplots(1, 1, figsize = (16,6))


# Plots
ax.bar(x = range(numberOfBins), height = realValues, color="#408090")
ax.hlines(idealValue, -1, numberOfBins, colors="#995050", linewidths=5)

# Style
ax.set_xlim(-1,numberOfBins); ax.set_ylim(0,max(realValues)+2)
ax.set_xticklabels(" 123456 ")
ax.set_xlabel("Groups")
ax.set_ylabel("Weight/Value")

plt.show()

''' Ta daa ! Comme nous l'avions prévu, nous avons constitué 6 groupes équilibrés. 

Chaque groupe a en effet un score très proche de l'idealValue (11,666). 

Je pense que l'objectif est (approximativement) atteint.   

Rappelons, en effet, que ce que nous avons obtenu est une solution compatible avec 

notre problème mais pas optimale, puisque nous avons utilisé un algorithme glouton. '''


''' -1. Conclusion

Bref, le problème du Bin Packing est vraiment très courant dans la vie de tous les jours.
Les approches gourmandes comme celle que nous venons de voir

 (l'emballage en bacs peut être résolu en utilisant différentes approches gourmandes) peuvent 
 
 s'avérer utiles dans de nombreuses occasions, surtout si elles sont extrêmement faciles à mettre en œuvre.

Quelques pistes de réflexion ? Et si on voulait essayer de prendre en compte le coût des articles ? 

Et si on voulait aussi intégrer une 2e ou 3e dimension ?

Probablement le simple 1D Bin Packing conviendrait un peu à l'étroit.

Je pense qu'on devrait en parler dans les prochains articles… Alors, restez connectés ! 😉 '''

