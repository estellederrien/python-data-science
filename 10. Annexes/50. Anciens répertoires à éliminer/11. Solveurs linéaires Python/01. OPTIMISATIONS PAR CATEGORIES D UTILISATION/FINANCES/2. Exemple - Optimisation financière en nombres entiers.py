
""" 

Exemple simple d'optimization financière en nombres entiers:



Supposons que nous devions passer 150 contrats dans un titre exotique en vente libre particulier auprès de trois concessionnaires.


- Le concessionnaire(dealer) X a cité 500 $ par contrat plus des frais de traitement de 4 000 $, quel que soit le nombre de contrats vendus. 

- Le concessionnaire Y facture 450 $ par contrat plus des frais de transaction de 2 000 $. 

- Le concessionnaire Z facture 450 $ par contrat plus des frais de 6 000 $. 

- Le concessionnaire X vendra au plus 100 contrats, le concessionnaire Y au plus 90 et le concessionnaire Z au plus 70. 

- Le volume de transaction minimum de tout courtier est de 30 contrats s'il y en a avec ce courtier. 


Comment minimiser le coût d'achat de 150 contrats?

SOURCE : Mastering Python for Finance.pdf page 36
""" 


# An example of implementing an integer programming model with binary conditions  

import pulp

dealers = ["X", "Y", "Z"] 
variable_costs = {"X": 500,"Y": 350, "Z": 450} 
fixed_costs = {"X": 4000,"Y": 2000,"Z": 6000}

# Define PuLP variables to solve 

quantities = pulp.LpVariable.dicts("quantity",dealers,lowBound=0,cat=pulp.LpInteger) 
is_orders = pulp.LpVariable.dicts("orders",dealers,cat=pulp.LpBinary)

""" 
La variable dealers contient simplement les identificateurs de dictionnaire qui seront utilisés ultérieurement 
pour référencer les listes et les dictionnaires. 

Les variables variables_costs et fixed_costs sont des dictionnaires qui contiennent leur coût de contrat respectif 
et les frais facturés par chaque concessionnaire. 

Le solveur PuLP résout les valeurs des quantités et is_orders, qui sont définies par la fonction LpVariable. 

La fonction dicts indique à PuLP de traiter la variable affectée comme un objet de dictionnaire, 
en utilisant la variable dealers pour le référencement. Notez que la variable des quantités a une limite inférieure de 0 
qui nous empêche d'entrer une position courte sur des titres. 

Les valeurs is_orders sont traitées comme des objets binaires, 
indiquant si nous devons conclure une transaction avec l'un des revendeurs. 

"""


""" 
Voir l'équation dans le livre page 34
L'équation indique simplement que nous voulons minimiser les coûts totaux avec la variable binaire i IsOrder, 
en déterminant s'il faut tenir compte des coûts associés à l'achat d'un concessionnaire spécifique si nous le souhaitons. 
Implémentons ce modèle en Python:
 """


""" This is an example of implementing an integer programming model with binary  variables the wrong way. """ 
# Ceci est un exemple d'implémentation d'un modèle de programmation entier avec des variables binaires dans le mauvais sens.
# Initialize the model with constraints 
# model = pulp.LpProblem("A cost minimization problem",  pulp.LpMinimize) 

# model += sum([(variable_costs[i] * quantities[i] + fixed_costs[i])*is_orders[i] for i in dealers]),"Minimize portfolio cost" 

# model += sum([quantities[i] for i in dealers]) == 150,"Total contracts required"

# model += 30 <= quantities["X"] <= 100, "Boundary of total volume  of X" 
# model += 30 <= quantities["Y"] <= 90, "Boundary of total volume of  Y" 
# model += 30 <= quantities["Z"] <= 70, "Boundary of total volume of  Z"

# model.solve()

# Pulp dit : TypeError: Non-constant expressions cannot be multiplied

""" 
Une approche différente avec des conditions binaires ...

Une autre méthode de formulation de l'objectif de minimisation consiste à placer toutes les variables inconnues de manière linéaire de sorte 
qu'elles soient additives( Voir le livre): 

Minimize variable cost quantity fixed cost IsOrder

En comparant avec l'équation objective précédente, 
nous obtiendrions les mêmes valeurs de coût fixe. 
Cependant, la variable inconnue i quantité reste dans 
le premier terme de l'équation. 
Par conséquent, la variable i quantité 
doit être résolue en fonction de telle que les contraintes sont énoncées comme suit:
Voir le livre page 35


"""
#Let's apply these formulas in Python:
""" This is an example of implementing an IP model with binary variables the correct way.
""" 
# Initialize the model with constraints 
model = pulp.LpProblem("A cost minimization problem",pulp.LpMinimize) 

model += sum([variable_costs[i]*quantities[i] + fixed_costs[i]*is_orders[i] for i in dealers]),"Minimize portfolio cost" 
model += sum([quantities[i] for i in dealers]) == 150,"Total contracts required" 

model += is_orders["X"]*30 <= quantities["X"] <= is_orders["X"]*100, "Boundary of total volume of X" 
model += is_orders["Y"]*30 <= quantities["Y"] <= is_orders["Y"]*90, "Boundary of total volume of Y" 
model += is_orders["Z"]*30 <= quantities["Z"] <= is_orders["Z"]*70, "Boundary of total volume of Z" 

model.writeLP("finances2.lp")

model.solve()


for v in model.variables():
    print(v.name, "=", v.varValue)

"""     Result - Optimal solution found

Objective value:                66500.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.04
Time (Wallclock seconds):       0.04

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.06   (Wallclock seconds):       0.06

orders_X = 0.0
orders_Y = 1.0
orders_Z = 1.0
quantity_X = 0.0
quantity_Y = 90.0
quantity_Z = 60.0 """



