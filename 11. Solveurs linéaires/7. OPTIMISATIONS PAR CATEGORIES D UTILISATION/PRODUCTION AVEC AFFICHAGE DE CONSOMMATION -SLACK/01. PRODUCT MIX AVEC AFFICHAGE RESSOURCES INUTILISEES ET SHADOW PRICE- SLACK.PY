

# https://campus.datacamp.com/courses/supply-chain-analytics-in-python/sensitivity-and-simulation-testing-of-model?ex=3
""" 
Prix ​​fictif et exercice mou pt1

Vous planifiez quels cupcakes une boulangerie devrait faire. La boulangerie peut faire soit :

    cupcake de taille normale : profit = 5 $
    un cupcake géant deux fois plus grand : bénéfice = 10 $

Il y a 2 contraintes sur les heures de four (30) et les heures de travail (65). 
Ce scénario a été modélisé dans PuLP pour vous et une solution a été trouvée. 
Le statut du modèle, les valeurs des variables de décision, la valeur objective 
(c'est-à-dire le profit), les prix fictifs et le relâchement des contraintes ont été imprimés dans le shell.

L'exemple de script est une copie de ce code. Vous ajusterez les contraintes pour voir comment la solution optimale change. 


SUPPLY CHAIN ANALYTICS IN PYTHON
Constraint slack
slack (RELACHEMENT):
The amount of a resource that is unused.
La quantité d'une ressource qui n'est pas utilisée.




"""







import pulp
# import panda as pd

# Define Constraints, Solve, Print Status, Variables, Objective
model = pulp.LpProblem("Maximize Bakery Profits", pulp.LpMaximize)

R = pulp.LpVariable('Regular_production', lowBound=0, cat='Continuous')
J = pulp.LpVariable('Jumbo_production', lowBound=0, cat='Continuous')

model += 5 * R + 10 * J, "Profit"

# Adjust the constraint
# heures de four
model += 0.5 * R + 1 * J <= 30 
# heures de travail
model += 1 * R + 2.5 * J <= 65

# Solve Model, Print Status, Variables, Objective, Shadow and Slack
model.solve()

print("Model Status: {}".format(pulp.LpStatus[model.status]))

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Objective = $", pulp.value(model.objective))

o = [{'name':name, 'shadow price':c.pi, 'slack': c.slack} for name, c in model.constraints.items()]
print(o)
# print(pd.DataFrame(o))