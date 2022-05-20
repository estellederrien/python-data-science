# https://medium.com/@sushan531/integer-programming-with-python-and-gekko-51ac235de408

# Je vais choisir le problème de charge fixe pour cette démo. 

# Voyons une sorte de problème de charge fixe et essayons de formuler ce problème.

# PROBLÈME : Une entreprise de confection souhaite fabriquer trois types de vêtements : 

# des chemises, des shorts et des jeans. 

# La machine nécessaire à la fabrication sera louée en fonction du résultat du calcul que nous obtenons,

#  c'est-à-dire que nous ne louerons la machine que si nous produisons ce type de vêtement spécifique. 
 
#  Le tableau ci-dessous contient les données dont dispose l'entreprise de confection avant de choisir
 
#   le nombre de chaque type de vêtement à fabriquer.

# Some problem’s are :

#     Project Selection Problem
#     Fixed Charge Problem
#     Cutting Stock Problem
#     Set Covering Problem
#     Assignment Problem
#     Traveling Salesman Problem

# Certains problèmes sont :

#     Problème de sélection de projet
#     Problème de charge fixe
#     Problème de stock de coupe
#     Définir le problème de couverture
#     Problème d'affectation
#     Problème de voyageur de commerce


# Le plan est de maximiser le profit des vêtements après avoir déduit le coût par vêtement et le loyer de la machinerie qui est fixe. Disons que nous allons fabriquer x1 unités de chemises, x2 unités de shorts et x3 unités de jeans.

# Commençons à formuler le problème avant d'entrer dans la partie codage.

#     En réalité, nous ne pouvons produire aucun vêtement, mais nous ne pouvons jamais produire de vêtements négatifs,
#     c'est-à-dire que les valeurs de x1, x2, x3 ne peuvent pas être inférieures à 0. (x1,x2,x3 ≥0)
#     L'heure de travail de la somme de chaque type de vêtement est limitée à seulement 150 heures par semaine. 
#      (3*x1+2*x2*6*x3 ≤ 150)
#     Les vêtements que nous avons ne font que 160 m². (4*x1+3*x2+4*x3 ≤160)
#     Comme indiqué ci-dessus, nous louerons une machine si et seulement si nous produisons le type de vêtement spécifique. 
#     Disons que y1 est la location de machines pour une chemise, y2 pour un short, y3 pour un jean. 
#     Si nous fabriquons des chemises, nous louerons des machines, c'est-à-dire que y1 sera (Vrai ou 1) sinon (Faux ou 0). 
#     Respectivement pour les autres vêtements un puits. Ainsi (x1≤M*y1 , x2≤M*y2 , x3≤M*y3) 
#     Si nous ne produisons pas de vêtements, disons chemise, alors x1 est 0, et si pour satisfaire l'équation, 
#      la valeur de y1 doit également être 0. Ici M est une grande valeur constante.
#     Quelle est donc la valeur de M. Nous prendrons M comme la valeur maximale que xi peut avoir, où i = {1,2,3}. 
#     La valeur maximale (tissu total / tissu par unité) que max_x1 peut avoir est de 160/4, de même, max_x2 = 160/3, 
#      max_x3 = 160/4.
#     L'objectif est de maximiser le profit (bénéfice des ventes - coût unitaire - coût des machines)

from gekko import GEKKO
m = GEKKO(remote=False) 
CLOTH_LIMIT = 160
WORK_LIMIT = 150
max_x1 = CLOTH_LIMIT / 4
max_x2 = CLOTH_LIMIT / 3
max_x3 = CLOTH_LIMIT / 4

# initializing variables
x1 = m.Var(lb=0, ub=max_x1, integer=True)
x2 = m.Var(lb=0, ub=max_x2, integer=True)
x3 = m.Var(lb=0, ub=max_x3, integer=True)
y1 = m.Var(lb=0, ub=1, integer=True)
y2 = m.Var(lb=0, ub=1, integer=True)
y3 = m.Var(lb=0, ub=1, integer=True)

# equations/constraint
m.Equation(3 * x1 + 2 * x2 + 6 * x3 <= WORK_LIMIT)
m.Equation(4 * x1 + 3 * x2 + 4 * x3 <= CLOTH_LIMIT)
m.Equation(x1 <= x1.UPPER * y1)
m.Equation(x2 <= x2.UPPER * y2)
m.Equation(x3 <= x3.UPPER * y3)

# sales profit = 12 * x1 + 8 * x2 + 15 * x3
# production cost = 6 * x1 + 4 * x2 + 8 * x3
# machinery cost = 200 * y1 + 150 * y2 + 100 * y3
# (sales profit — unit cost — machinery cost)
m.Maximize((12 * x1 + 8 * x2 + 15 * x3) - (6 * x1 + 4 * x2 + 8 * x3) - (200 * y1 + 150 * y2 + 100 * y3))

m.solve(disp=False) 

print(f"x1: {x1.VALUE}")
print(f"x2: {x2.VALUE}")
print(f"x3: {x3.VALUE}")
print(f"y1: {y1.VALUE}")
print(f"y2: {y2.VALUE}")
print(f"y3: {y3.VALUE}")