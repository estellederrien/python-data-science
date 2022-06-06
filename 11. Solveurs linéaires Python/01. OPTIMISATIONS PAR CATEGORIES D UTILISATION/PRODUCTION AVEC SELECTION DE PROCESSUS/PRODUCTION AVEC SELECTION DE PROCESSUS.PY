""" Source : https://www.lindo.com/downloads/LINGO_text/Chapter6.pdf

6.3 Processus de sélection des problèmes de mélange de produits

Une caractéristique courante des modèles de mix de produits est la présence de deux variables distinctes 
ou plus dans la formulation LP peuvent en fait correspondre à des méthodes alternatives pour produire le même produit. 

Dans ce cas, le PL est être utilisé non seulement pour découvrir combien doit être produit d'un produit, mais aussi pour sélectionner le meilleur
processus de production de chaque produit.

Une deuxième caractéristique qui apparaît généralement avec les problèmes de gamme de produits est l'exigence d'une certaine
quantité d'un produit à produire. Cette condition sort le problème du domaine du produit simple
mélanger. 

Néanmoins, considérons un problème avec les deux caractéristiques ci-dessus.

L'American Metal Fabricating Company (AMFC) fabrique divers produits à partir de barres d'acier. 
Une des étapes initiales est une opération de mise en forme effectuée par des laminoirs. Il y a trois appareils
disponibles à cet effet, les B3, B4 et B5. 

Le tableau suivant donne leurs caractéristiques :
        Vitesse     épaisseur de matériel admissible en pieds         Disponible           Coût
B3      150         3/16 à 3/8                                         35 h                 10 $
B4      100         5/16 à 1/2                                          35 h                 15 $
B5      75          3/8 à 3/4                                           35 h                 17 $

Ce type de combinaison de capacités n'est pas rare. 
Autrement dit, les machines qui traitent de plus gros le matériau fonctionne à une vitesse plus lente.

Cette semaine, trois produits doivent être fabriqués. AMFC doit produire au moins 218 000 pieds de 1 / 4 " en
matériel, 114 000 pieds de matériel de 3 / 8 " et 111 000 pieds de matériel de 1 / 2 ". 

Les contributions aux bénéfices par pieds hors main-d'œuvre pour ces trois produits sont de 0,017, 0,019 et 0,02. 
Ces prix s'appliquent à tous 

production (par exemple, tout dépassement de la production requise). Le service d'expédition a une limite de capacité
de 600 000 pieds par semaine, peu importe l'épaisseur

Quelles sont les variables de décision et les contraintes pour ce problème ? 
Les variables de décision nécessitent une certaine pensée. 
Il n'y a qu'une seule façon de produire du matériel d'épaisseur 1 /  4 " 
( 3/16 dans le tableau est égal à 1/4 , pour l'auteur et c la machine b3 qui peut le traiter), 
trois façons de produire du 3 / 8 " et deux façons de produire du 1 / 2 ". 
Ainsi, vous voudrez avoir au moins les variables de décision suivantes. 
Pour commodité numérique, nous mesurons la longueur en milliers de pieds :


"""
