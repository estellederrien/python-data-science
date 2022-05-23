""" Exemple d'image de mélange J'espérais obtenir de l'aide sur ce problème car je suis novice en python. 
Le problème: nous cherchons à mélanger une bière cible avec certains paramètres (couleur, alcool, etc.) et 
à utiliser un stock existant de bières "mères" pour y parvenir (50% de bière 1, 20% de bière 2, 30% de bière 3) . 
J'ai joint une image qui, je l'espère, explique mieux. J'avais du mal à trouver une solution au problème dans Excel et 
j'ai trouvé ce morceau de code sur le site Web de pulp qui semblait être exactement ce que je cherchais.

https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

Cependant, nous n'avons pas besoin de minimiser les coûts que j'espérais produire simplement si une solution 
est possible et quels sont les pourcentages nécessaires pour y parvenir. 
J'ai utilisé cette méthode pour construire mon idée. Je reste coincé cependant. 
Ma sortie semble être par défaut à 100% d'une bière à chaque fois et je ne peux pas faire fonctionner un mélange, 
même avec des combinaisons pour lesquelles je connais déjà la solution. Je suppose que je fais une simple erreur 
en raison du manque de connaissances sur la pâte, mais quelqu'un peut-il m'aider à me diriger dans la bonne direction? 
Je vois le __dummy ajouté à ma liste mais je ne sais pas pourquoi.

Source : 
https://stackoverflow.com/questions/59265365/pulp-python-function-for-blending-calculator

 """

from pulp import *

Ingredients = ['Beer 1', 'Beer 2', 'Beer 3', 'Beer 4']

RDF = {'Beer 1': 60, 
     'Beer 2': 60, 
     'Beer 3': 70, 
     'Beer 4': 70}

IBU = {'Beer 1': 15, 
     'Beer 2': 40, 
     'Beer 3': 25, 
     'Beer 4': 40}

Colour = {'Beer 1': 6, 
     'Beer 2': 40, 
     'Beer 3': 6, 
     'Beer 4': 15}

prob = LpProblem("BeerTest", LpMinimize)
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 100, "PercentagesSum"
prob += lpSum([RDF[i] * ingredient_vars[i] for i in Ingredients])/100 == 67, "RDF"
prob += lpSum([IBU[i] * ingredient_vars[i] for i in Ingredients])/100 == 22, "IBU"
prob.writeLP("BlendTest1")

prob.solve()


print ("Status:" + str(LpStatus[prob.status]))

for v in prob.variables():
    print (v.name + "=" + str(v.varValue))


""" Status:Optimal
Ingr_Beer_1=30.0
Ingr_Beer_2=0.0
Ingr_Beer_3=70.0
Ingr_Beer_4=0.0
__dummy=None """