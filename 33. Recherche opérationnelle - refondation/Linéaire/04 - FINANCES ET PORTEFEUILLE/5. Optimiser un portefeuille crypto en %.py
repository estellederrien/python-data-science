""" 
Etudes : 

Maximiser le profit d' un portefeuille crypto dont les paramêtres sont exprimés en %

note : 
- Les contraintes sont exprimées en % lors de l'initialisation des datas
- Par contre, dans les functions, on transforme tout en décimal, et on indique la loi de conservation == 100

Expérimental by Nicolas Estel HULEUX

"""

from pulp import *

# --------------------------------------------------------
# PARTIE 1 : ON INITIALISE LES DATAS DE NOTRE PORTEFEUILLE
# --------------------------------------------------------

# Liste des cryptos 
coinsList = ['bitcoin','litecoin','euthereum','ripple']

# Renseigner la marge prévisionnelle de la monnaie en %
margins = {"bitcoin": 18,"litecoin": 35,"euthereum":18,"ripple":16}

# Renseigner   la fiabilité de la monnaie en  %
fiability = {"bitcoin": 9,"litecoin": 8,"euthereum":5,"ripple":13}

# Limites minimales d'achat de chaque coins en %
lowbounds = {"bitcoin": 10,"litecoin": 10,"euthereum":8,"ripple":5}

# --------------------------------------------------------
# PARTIE 2 : ON CREE NOTRE PROGRAMME LINEAIRE
# --------------------------------------------------------

# Création du problème : 
prob = LpProblem("Portfolio_Opt",LpMaximize)

# Création des variables de décision
decision_variables = LpVariable.dicts("Maximisation de profit",coinsList,cat='Continuous')

# On ajoute les limites inférieures de chaque variable de décision
for i in decision_variables.keys():
    decision_variables[i].lowBound = lowbounds[i]

# La function à maximiser
prob += lpSum([margins[i] / 100 * decision_variables[i] for i in coinsList])

# Cette Fonction est nécessaire lorsque les contraintes sont exprimées en %
prob += lpSum([1 * decision_variables[f] for f in coinsList]) == 100, "budget"

# Les contraintes exprimées en % , On veut un minimum de 9%  de fiabilité global 
prob += lpSum([fiability[f] / 100 * decision_variables[f] for f in coinsList]) >= 9, "fiability"

# --------------------------------------------------------
# PARTIE 3 : ON RESOUDS ET IMPRIME LE RESULTAT DE  NOTRE PROGRAMME LINEAIRE
# --------------------------------------------------------

# Imprimer le look du problème
print(prob)
print(LpStatus[prob.status])

# Ecriture du programme linéaire dans un fichier
prob.writeLP("Portfolio_Opt.lp")

# Résoudre le programme linéaire.
prob.solve()

# Le meilleur portefeuille est exprimé en %
print("Le portefeuille de qualité optimum est \n")
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Le meilleur pourcentage global trouvé pour le portefeuille, exprimé en %
print(prob.objective.value())
