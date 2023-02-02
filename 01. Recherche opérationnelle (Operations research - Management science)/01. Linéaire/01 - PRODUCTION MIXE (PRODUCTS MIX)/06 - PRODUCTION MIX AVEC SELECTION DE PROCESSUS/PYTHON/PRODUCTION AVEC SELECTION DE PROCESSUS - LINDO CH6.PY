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

B34 = 1,000’s of feet of1 4 " produced on B3,
B38 = 1,000’s of feet of3 8 " produced on B3,
B48 = 1,000’s of feet of3 8 " produced on B4,
B58 = 1,000’s of feet of3 8 " produced on B5,
B42 = 1,000’s of feet of1 2 " produced on B4,
B52 = 1,000’s of feet of1 2 " produced on B5.

Pour la fonction objectif, nous devons avoir la contribution au profit,
y compris les coûts de main-d'œuvre. Quand c'est fait, on obtient :

                Profit Contribution
Variable        per Foot
B34             0.01589
B38             0.01789
B48             0.01650
B58             0.01522
B42             0.01750
B52             0.01622


En clair, il y aura quatre contraintes correspondant aux trois ressources machines rares d'AMFC et
sa capacité de service d'expédition. 
Il devrait y avoir trois autres contraintes dues aux exigences de la production pour les trois produits. 
Pour les contraintes de capacité machine, on veut le nombre d'heures requis pour 1 000 pieds traités. 
Pour la machine B3, ce chiffre est de 1 000/(60 min./hr.) * (150 ft./min.) = 0,111111 heures par 1 000 pieds. 
Des chiffres similaires pour B4 et B5 sont 0,16667 heures par 1 000 pieds et 0,22222
heures par 1 000 pieds.

La formulation peut maintenant s'écrire :
Maximiser=15.89B34+17.89B38+16.5B48+15.22B58+17.5B42+16.22B52
sujet à
0.11111B34 + 0.11111B38 <= 35   Machine
0.16667B48 + 0.16667B42 <= 35   capacités
0,22222B58 + 0,22222B52 <= 35   en heures
B34+B38+B48+B58+B42+B52 <= 600  Capacité d'expédition en milliers de pieds
B34 >= 218                      Fabrication
B38 + B48 + B58 >= 114          exigences
B42 + B52 >= 111                en milliers de pieds

"""

# Maintenant, on utilise le solveur PULP pour résoudre le p.l de la documentation LINDO Chapitre 6
import pulp


# Definir le type du pb
model = pulp.LpProblem("Maximize", pulp.LpMaximize)

# Définir les vars de décision, c'est ce que vont produire les 3 machines .
# B34 et B38 sont les mêmes machines, ca veut dire qu'elle peut produire du matériel de 1/4 OU 3/8 de largeur
# idem pour le reste (convention de nommmage)

B34 = pulp.LpVariable('B34', lowBound=0, cat='Continuous')
B38 = pulp.LpVariable('B38', lowBound=0, cat='Continuous')
B48 = pulp.LpVariable('B48', lowBound=0, cat='Continuous')
B58 = pulp.LpVariable('B58', lowBound=0, cat='Continuous')
B42 = pulp.LpVariable('B42', lowBound=0, cat='Continuous')
B52 = pulp.LpVariable('B52', lowBound=0, cat='Continuous')

# La fonction objectif , il a calculé dans le document en soustrayant les couts au profit avant d'écrire la fonction objectif

model += 15.89 * B34 + 17.89 * B38 + 16.5 * B48 + 15.22 * B58 + 17.5 * B42 + 16.22 * B52, "Profit"
 
# On a ici les contraintes habituelles de produits mix  . 
# Ca nous dit qu'on doit utiliser chaque machine moins de 35 heures.
# Dans la partie gauche, 0.11111 c'est une fraction horaire pour 1000 pieds qu'il a calculé grâce à son tableau initial
# il prends en compte la vitesse différente de chaque machine pour le calcul
model += 0.11111 * B34 + 0.11111 * B38 <= 35 , "1st machine temps de travail" # sa formule : 1,000/(60 min./hr.) * (150 ft./min.) = 0.111111 hours per 1,000 ft
model += 0.16667 * B48 + 0.16667 * B42 <= 35 , "2nd machine temps de travail"
model += 0.22222 * B58 + 0.22222 * B52 <= 35 , "3rd machine temps de travail"
model += B34 + B38 + B48 + B58 + B42 + B52 <= 600 , "Capacité de livraison max"

# Ces 3 prochaines contraintes sont spéciales, et ont été calculées au préalable par l'auteur LINDO dans sa doc
model += B34 >= 218  , "1/4 de largeur de materiel fait sur B34 seulement"   # normal car seul la machine B34 peut produire du 1/4 d'épaisseur , et il faut en produire 218 000 pieds comme dans sa doc                
model += B38 + B48 + B58 >= 114 , "3/8 de largeur materiel dispo sur 3 machines" # Là on dit au solveur qu'il faut produire 114 000 pieds de matériel de 3/8 de largeur, hors on ne peut les produire que sur les machines citées dans la contrainte
model += B42 + B52 >= 111 , "1/2 de largeur sur les 2 machines qui le peuvent"              

# Solve Model, Print Status, Variables, Objective, Shadow and Slack
model.solve()

print("Model Status: {}".format(pulp.LpStatus[model.status]))

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Objective = ", pulp.value(model.objective))

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack} for name, c in model.constraints.items()]
print(o)


""" 
Le résultat nous donne le nombre de pieds en 1000 d'unités à produire par machines, afin de maximiser le profit.
Ca fait penser à un flow shop machine multiples / Ordonnancement mais c'est est pas un.
Par exemple, B34 doit produire 218 000 pieds de matériel de 1/4 de largeur .
et B38, qui est la même machine doit produire 97.00315 de matériel de 3/8 de largeur
Le résultat est le même qu'avec le solveur LINDO - AMP

Model Status: Optimal
B34 = 218.0
B38 = 97.00315
B42 = 192.99895
B48 = 16.99685
B52 = 75.00105
B58 = 0.0
Objective =  10073.8530345
[{'name': '1st_machine_temps_de_travail', 'shadow price': 24.03024, 'slack': -0.0}, 
{'name': '2nd_machine_temps_de_travail', 'shadow price': 7.6798464, 'slack': -0.0}, 
{'name': '3rd_machine_temps_de_travail', 'shadow price': -0.0, 'slack': 18.333267}, 
{'name': 'Capacité_de_livraison_max', 'shadow price': 16.22, 'slack': -0.0}, 
{'name': '1/4_de_largeur_de_materiel_fait_sur_B34_seulement', 'shadow price': -3.0, 'slack': -0.0}, 
{'name': '3/8_de_largeur_materiel_dispo_sur_3_machines', 'shadow price': -1.0, 'slack': -0.0}, 
{'name': '1/2_de_largeur_sur_les_2_machines_qui_le_peuvent', 'shadow price': -0.0, 'slack': -157.0}]
"""
