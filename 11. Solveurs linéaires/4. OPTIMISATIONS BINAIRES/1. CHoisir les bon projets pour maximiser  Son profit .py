""" 

CHoisir les bon projets pour maximiser son profit .
Une optimisation binaire utilise des variables de décision boléennes c'est soit 0, soit 1.


ETAPE1 : Savoir Décrire les contraintes booléenes dans un programme linéaire  :

    Les rêgles pour bien écrire les contraintes binaires ( Booléens) sont ici:
    https://www.youtube.com/watch?v=B3biWsBLeCw 

    Example : 
    Une entreprise a 5 projets parmis elle doit choisir un ou des projets parmis ces projets 

    Les variables de décisions sont donc : 

    xi =  { 1. Selectionné
            2. Non selectionné 

    Ensuite, pour exprimer différentes contraintes, on jour avec les contraintes binaires : ( Booléens)

    Si le projet 3 est sélectionné, alors le projet 5 ne peut pas être séolectionné  :
    On exprime ça comme ça 
    x3 + x5 <= 1 

    Seulement un des projets 2 et 3 doivent être sélectionné s'exprime comme ça : 
    x2 + x3 = 1

ETAPE 2 : CREER UN PROGRAMME LINEAIRE EN VARIABLES BOOLEENNES
    On a un bon example de problème là : 
    https://www.youtube.com/watch?v=-3my1TkyFiM&t=56s

    On a 4 projets, lesquels faut il choisir our maximiser notre profit

    Projet          1       2       3       4       Fonds investis
    Janvier         58      44      26      33      120 
    Février         25      29      13      17      80
    Mars            43      25      23      29      95
    Profit          217     125     88      109      

    On veut maximiser notre profit, donc, voici la fonction objectif : 
    Maximize 217X1 + 125X2 + 88X3 + 109X4 
    
    Et nos contraintes : 
    58X1 + 44X2 + 26X3 + 23X4 <= 120 ( Janvier)
    25X1 + 29X2 + 13X3 + 17X4 <= 80 ( Février)
    43X1 + 25X2 + 23X3 + 29X4 <= 95 ( Mars)
    Xi = 0-1 ( Binaire)

    
Sources et auteurs : 
    Integer Linear Programming | 0-1 Binary Constraints | Examples - Part 1
    https://www.youtube.com/watch?v=B3biWsBLeCw 
    https://www.youtube.com/watch?v=MO8uQnIch6I
    https://www.paypal.com/paypalme/joshemman

"""

# Importer la librairie Pulp 
import pulp 
   