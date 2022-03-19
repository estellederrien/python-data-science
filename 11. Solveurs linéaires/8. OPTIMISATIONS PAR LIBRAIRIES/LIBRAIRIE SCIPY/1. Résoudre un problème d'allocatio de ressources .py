""" 

Source : 
https://realpython.com/linear-programming-python/#resource-allocation-problem
https://realpython.com/linear-programming-python/

Problème d'allocation des ressources



Dans les sections précédentes, vous avez examiné un problème de programmation linéaire abstrait qui n’était lié à 

aucune application réelle. 

Dans cette sous-section, vous trouverez un problème d’optimisation plus concret et pratique lié à l’allocation 

des ressources dans la fabrication.

Disons qu'une usine fabrique quatre produits différents et que la quantité produite quotidiennement du premier produit 

est x is, la quantité produite du deuxième produit est x₂, et ainsi de suite. 

L'objectif est de déterminer la quantité de production quotidienne qui maximise le profit pour chaque produit, 

en tenant compte des conditions suivantes:

--------------------------------------------------------------------------------------------------------------------------

    1. Le bénéfice par unité de produit est de 20 $, 12 $, 40 $ et 25 $ pour le premier, deuxième, troisième et 
    
    quatrième produit, respectivement.

    2. En raison des contraintes de main-d’œuvre, le nombre total d’unités produites par jour ne peut pas dépasser cinquante.

    3. Pour chaque unité du premier produit, trois unités de la matière première A sont consommées. 
    
    Chaque unité du deuxième produit nécessite deux unités de la matière première A et une unité de la matière première B.
    
    Chaque unité du troisième produit nécessite une unité de A et deux unités de B.Enfin, chaque unité du quatrième 
    
    produit en nécessite trois unités de B.
    
    4.En raison des contraintes de transport et de stockage, l'usine peut consommer jusqu'à cent unités de 
    
    matière première A et quatre-vingt dix unités de B par jour.
--------------------------------------------------------------------------------------------------------------------------

Le modèle mathématique peut être défini comme ceci:

max 20x1 + 12x2 +40x3 + 25x4 
s.t : 
x1 + x2 + x3 + x4 <= 50 ( Manpower temps de travail)
3x1 + 2x2 + x3 <= 100 ( materiel A)
x2 + 2x3 + 3x4 <= 90 ( materiel B)
x1 + x2 + x3 + x4 >= 0 

- La fonction objectif (profit) est définie dans la condition 1. 

- La contrainte de main-d'œuvre découle de la condition 2. 

- Les contraintes sur les matières premières A et B peuvent être dérivées des conditions 3 et 4 en additionnant 

les besoins en matière première de chaque produit.

- Enfin, les montants des produits ne peuvent pas être négatifs, toutes les variables de décision 

doivent donc être supérieures ou égales à zéro.

Contrairement à l'exemple précédent, vous ne pouvez pas visualiser celui-ci de manière pratique en mode graphique

car il comporte quatre variables de décision. Cependant, les principes restent les mêmes quelle que soit 

la dimensionnalité du problème.


-------------------------------------------------------------------------------------------------------------------------------
Dans ce didacticiel, vous allez utiliser deux packages Python pour résoudre le problème de programmation linéaire 

décrit ci-dessus:

    * SciPy est un package à usage général pour le calcul scientifique avec Python.
    * PuLP est une API de programmation linéaire Python permettant de définir des problèmes et d'appeler des solveurs externes.

SciPy est simple à installer. Une fois que vous l'avez installé, vous aurez tout ce dont vous avez besoin pour démarrer. 

Son sous-paquet scipy.optimize peut être utilisé à la fois pour l'optimisation linéaire et non linéaire.

PuLP vous permet de choisir des solveurs et de formuler des problèmes de manière plus naturelle. 

Le solveur par défaut utilisé par PuLP est COIN-OR Branch and Cut Solver (CBC). 

Il est connecté au solveur de programmation linéaire COIN-OR (CLP) pour les relaxations linéaires et à la bibliothèque 

de générateurs de coupes COIN-OR (CGL) pour la génération de coupes.

Un autre excellent solveur open source est le GNU Linear Programming Kit (GLPK). 

Certaines solutions commerciales et propriétaires bien connues et très puissantes sont Gurobi, CPLEX et XPRESS.

En plus d'offrir une flexibilité lors de la définition des problèmes et la possibilité d'exécuter divers solveurs, 

PuLP est moins compliqué à utiliser que des alternatives comme Pyomo ou CVXOPT, qui nécessitent plus de temps et d'efforts 

pour maîtriser.

 """

from scipy.optimize import linprog

obj = [-20, -12, -40, -25]

lhs_ineq = [[1, 1, 1, 1],  # Manpower
            [3, 2, 1, 0],  # Material A
            [0, 1, 2, 3]]  # Material B

rhs_ineq = [ 50,  # Manpower
            100,  # Material A
             90]  # Material B

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")
print(opt)


"""     con: array([], dtype=float64)
     fun: -1900.0
 message: 'Optimization terminated successfully.'
     nit: 2
   slack: array([ 0., 40.,  0.])
  status: 0
 success: True
       x: array([ 5.,  0., 45.,  0.]) """