"""
 NOTE : SEULEMENT TRADUIT 

SOURCE
https://itnext.io/introduction-to-linear-programming-with-python-1068778600ae

Essayons de formaliser un cas d'utilisation et de le faire progresser tout au long de l'article. 
Supposons que vous soyez un guérisseur magique et que votre objectif soit de guérir quiconque demande de l'aide. 
Plus vous êtes capable de guérir quelqu'un, mieux c'est. Votre secret derrière la guérison est 2 médicaments, 
chacun utilisant des herbes spéciales. 

Pour créer une unité de médicament 1,vous avez besoin de 3 unités d'herbe A et 2 unités d'herbe B. 

De même, pour créer une unité de médicament 2, vous avez besoin de 4 et 1 unités d'herbe A et B respectivement. 
 
 Désormais, le médicament 1 peut soigner une personne par 25 unités de santé (quel qu'il soit) 
 et le médicament 2 par 20 unités. 
 
 Pour compliquer encore les choses, vous n'avez que 25 et 10 unités d'herbes A et B à votre disposition. 
 Maintenant, la question est de savoir combien de chaque médicament allez-vous créer pour maximiser la santé 
 de la prochaine personne qui entre?

Modéliser le problème

Essayons d'abord d'identifier l'objectif (ce que nous voulons faire et comment) et la contrainte (les fonctions de délimitation)
du problème posé.

Comme le montre clairement le problème, nous voulons augmenter la santé du plus grand nombre possible d'unités. 
Et les médicaments sont la seule chose qui peut nous aider. 

Ce dont nous ne sommes pas sûrs, c'est la quantité de chaque médicament à créer. 
En suivant la logique d'un mathématicien, disons que nous créons x unités de médecine 1 et y unités de médecine 2. 
Ensuite, la santé totale restaurée peut être donnée par,

25 * x + 20 * y = Santée restaurée
C'est la fonction objectif que nous voulons maximiser. Maintenant, les deux médicaments dépendent des herbes que nous avons en quantité limitée. Comprenons les contraintes. Si nous créons des unités x et y des médicaments 1 et 2,

Nous utilisons 3 * x + 4 * y unités d'herbe A. Mais nous n'en avons que 25 unités, d'où la contrainte, notre utilisation totale d'herbe A ne doit pas dépasser 25, dénotée par,
2 * x + 4 * y <= 25

Nous utilisons 2 * x + 1 * y unités d'herbe B. Nous en avons 10 unités, d'où la contrainte, notre utilisation totale d'herbe B ne doit pas dépasser 10, dénotée par,
2*x + y <= 10

De plus, la quantité de médicaments créés ne peut pas être négative (cela n'a pas de sens), par conséquent, ils doivent être égaux ou supérieurs à zéro, dénotés par,
x >= 0 ; y >= 0



"""

# importer PuLP
from pulp import *

# ON crée le problème et on veut maximiser 
prob = LpProblem("Un patient restauré", LpMaximize)

# On crée les variables de décision
x=LpVariable("Medicine_1_units",0,None,LpInteger)
y=LpVariable("Medicine_2_units",0, None, LpInteger)

# La fonction objectif est ajoutée en premier , c'est celle qu'on veut maximiser
prob += 25*x + 20*y, "Santé restaurée, à maximiser"

# Les 2 contraintes
prob += 3*x + 4*y <= 25, "Herbe A contrainte"
prob += 2*x + y <= 10, "Herbe B contrainte"

# On écrit le problème dans un fichier
prob.writeLP("PatientRestaure.lp")

# Le problème est solvé avec le solveur de notre choix
prob.solve()

# On affiche le statut de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables elements
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonction objectif est ici :
print ("Santé totale qui peut être restaurée", value (prob.objective))


""" 
Medicine_1_units = 3.0 // Veut dire que cela 'sauve' 3 personnes
Medicine_2_units = 4.0 // Veut dire que cela 'sauve' 4 personnes
TotalDesLotsaAcheter 155.0 // Veut dire que le total des unités utilisées est de 155, cela ne rompt pas les contraintes  A et B

"""