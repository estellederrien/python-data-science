""" 
Le mélange SP 95 doit respecter les contraintes suivantes:

    Ethanol -  SP95 : = 7,5 % d’éthanol
	Alcane  -  SP95 : > 20 % d’alcane

Mon tableau pour 1 litre
fournisseur      alcane     Ethanol            Cout unitaire
                (litre/litre) (litre/litre)   (centime/litre) 
fournisseur 1      0.25        0.075               21.7 	
fournisseur 2      0.26        0.03                20.5
fournisseur 3      0.27        0.15                21.5


Minimiser Z = 21.7L + 20.5C + 21.5S

A vérifier ...

Source originelle (EXCEL)

https://www.me.utexas.edu/~jensen/ORMM/models/unit/linear/subunits/blending/index.html


"""

import pulp
from pulp import *

# Liste des fournisseurs
Fournisseurs = ['FOURNISSEUR1','FOURNISSEUR2','FOURNISSEUR3']

# Cout unitaire PAR FOURNISSEUR  (centimes/litre) 
couts = {
            'FOURNISSEUR1': 21.7, 
            'FOURNISSEUR2': 20.5,
            'FOURNISSEUR3': 21.5
        }



# alcane (l,l)
alcane = {
            'FOURNISSEUR1': 0.25, 
            'FOURNISSEUR2': 0.26,
            'FOURNISSEUR3': 0.27
        }

# ethanol (l,l)
ethanol = {
            'FOURNISSEUR1': 0.075, 
            'FOURNISSEUR2': 0.03,
            'FOURNISSEUR3': 0.15
        }


# On veut minimiser nos couts
prob = LpProblem("Probleme essence", LpMinimize)

# On se sert du dictionnaire Fournisseurs pour créer nos variables
fournisseurs_vars = LpVariable.dicts("Fournisseurs",Fournisseurs,0)

# Notre function objectif s'exprime en euros ou en dollars
prob += lpSum([couts[i]*fournisseurs_vars[i] for i in Fournisseurs]), "Cout total des ingrédients par litre essence SP95"

# La production totale est de 1 litre
prob += lpSum([fournisseurs_vars[i] for i in Fournisseurs]) == 1 ,"conservation"

# On spécifie au solveur PULP Notre contrainte

# On veut au minimum 25% d'alcane sur 1 litre, ce qui nous donne 0.25 litre. 
prob += lpSum([alcane[i]    * fournisseurs_vars[i] for i in Fournisseurs]) >= 0.25,"alcaneRequirementMin"

# On veut au minimum 7.5% d'ethanol  sur 1 litre, ce qui nous donne 0.075 litre. 
prob += lpSum([ethanol[i]    * fournisseurs_vars[i] for i in Fournisseurs]) == 0.075,"ethanolRequirementMin"



prob.writeLP("problemEssence.lp")
prob.solve()
# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chauqe variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
    print (v.name, "=", v.varValue)

# Le résultat de la fonction objectif :
print ("Cout total des ingrédients par litre essence SP95 = ", value(prob.objective), "Centimes")

# Le résultat de la fonction objectif pour 1000 litres, en euros:
print ("Cout total des ingrédients par 1000 litres essence SP95 = ", value(prob.objective) * 10, "Euros")

""" 
Status: Optimal
Fournisseurs_FOURNISSEUR1 = 0.0
Fournisseurs_FOURNISSEUR2 = 0.625
Fournisseurs_FOURNISSEUR3 = 0.375
Cout total des ingrédients par litre essence SP95 =  20.875 Centimes
Cout total des ingrédients par 1000 litres essence SP95 =  208.75 Euros

 """


