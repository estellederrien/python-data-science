""" 
Module D108 : Programmation mathématique et optimisation 
Programmation Linéaire 
Programmation linéaire
Exemple
Forme canonique
Cas spéciaux
Exercices
Auteur(s) :
Nasser Saheb (IUP Miage, Bordeaux)
Mike Robson (IUP Miage, Bordeaux)
Contact :
saheb@labri.fr
mike.robson@labri.fr
Date de dernière modification : 30 Janvier 2006 



Exemple 2 :Composition d’Aliments pour le Bétail.
On désire déterminer la composition, à coût minimal, d’un aliment pour bétail qui est 
obtenu en mélangeant au plus trois produits bruts : orge, arachide, sésame. 

L’aliment ainsi conditionné devra comporter au moins 22% de protéines et 3,6% de graisses, 
pour se conformer aux exigences de la clientèle. 

On a indiqué ci-dessous les pourcentages de protéines et de graisses contenus, respectivement, dans l’orge, les 
arachides et le sésame, ainsi que le coût par tonne de chacun des produits bruts : 

Produit brut
                1       2           3       Pourcentage 
                ORGE    ARACHIDES   SESAME  requis
Pourcentage de 
protéines       12%     52%         42%     22%

Pourcentage de 
graisses        2%      2%          10%     3,6%

coût par tonne  25      41          39

1. On notera Xj (j = 1, 2, 3) la fraction de tonne de produit brut j contenu dans 
une tonne d’aliment. Formuler le problème algébriquement.

2. Montrer qu’il est possible de réduire la dimension du problème.



Solution de l'exercice 2

Puisqu’il s’agit d’obtenir une tonne d’aliment, en appelant respectivement, X1, X2 et X3 
les fractions d’orge, d’arachide et de sésame dans la dite tonne, on doit avoir
X1 +X2 + X3 = 1, qui sera une contrainte de notre problème.

Remarque : On peut parler soit en fraction de tonne, soit en pourcentage, c’est équivalent.

Par ailleurs, l’aliment doit contenir au moins 22% de protéines. D’où la contrainte :
12X1 + 52X2 + 42X3 >= 22

Et de même, pour les graisses, on doit avoir :
2X1 + 2X2 + 10 X3 >=  3,6

D’autre part, comme on désire fabriquer le produit à coût minimal, on devra minimiser la somme :
25X1 + 41X2 + 39X3

Soit, en récapitulant, le programme linéaire :


Note : Il n'y a pas la solution, impossible de comparer, abandon.

min 25x1 + 41x2 + 39x3

s.t 
12X1 + 52X2 + 42X3 >= 22
2X1 + 2X2 + 10 X3 >=  3,6



"""