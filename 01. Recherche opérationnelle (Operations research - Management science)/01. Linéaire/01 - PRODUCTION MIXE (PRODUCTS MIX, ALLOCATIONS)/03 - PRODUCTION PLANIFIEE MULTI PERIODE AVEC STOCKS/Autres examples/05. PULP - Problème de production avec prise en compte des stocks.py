""" 
Source : 
Multi-period planning problem
There is a factory that processes two types of raw materials A and B to produce two types of products I and II. 
The problem of making a production plan for the next three months. 
The amount of raw materials used to produce one unit of each product, the production / inventory cost of each product, 
the monthly shipment amount of each product, and the monthly available amount of each raw material are given.

Il y a une usine qui transforme deux types de matières premières A et B pour produire deux types de produits I et II.
Le problème de faire un plan de production pour les trois prochains mois.
La quantité de matières premières utilisées pour produire une unité de chaque produit, le coût de production/inventaire de chaque produit,
le montant de l'expédition mensuelle de chaque produit et la quantité mensuelle disponible de chaque matière première sont indiqués.
 """



#Set for the purpose of minimizing the function
problem3 = pulp.LpProblem("Problem-3", pulp.LpMinimize)

#Variable setting(Variable name, minimum value, maximum value, type)
#production(Prodution)I
Pi1 = pulp.LpVariable('Prodution I_1', 0, 170, 'Integer')
Pi2 = pulp.LpVariable('Prodution I_2', 0, 170, 'Integer')
Pi3 = pulp.LpVariable('Prodution I_3', 0, 170, 'Integer')
#production(Prodution)II
Pii1 = pulp.LpVariable('Prodution II_1', 0, 160, 'Integer')
Pii2 = pulp.LpVariable('Prodution II_2', 0, 160, 'Integer')
Pii3 = pulp.LpVariable('Prodution II_3', 0, 160, 'Integer')

#stock(Stock)I
Si1 = pulp.LpVariable('Stock I_1', 0, 170, 'Integer')
Si2 = pulp.LpVariable('Stock I_2', 0, 170, 'Integer')
#stock(Stock)II
Sii1 = pulp.LpVariable('Stock II_1', 0, 160, 'Integer')
Sii2 = pulp.LpVariable('Stock II_2', 0, 160, 'Integer')

#Objective function(Define the cost you want to minimize)
problem3 += (75*Pi1 + 50*Pii1 + 8*Si1 + 7*Sii1) + (75*Pi2 + 50*Pii2 + 8*Si2 + 7*Sii2) + (75*Pi2 + 50*Pii2)

#Constraint setting
#Restriction on the number of production by material
problem3 += 2*Pi1 + 7*Pii1 <= 920
problem3 += 5*Pi1 + 3*Pii1 <= 790
problem3 += 2*Pi2 + 7*Pii2 <= 750
problem3 += 5*Pi2 + 3*Pii2 <= 600
problem3 += 2*Pi3 + 7*Pii3 <= 500
problem3 += 5*Pi3 + 3*Pii3 <= 480
#Shipment and inventory constraints
problem3 += Pi1 - Si1 == 30
problem3 += Pii1 - Sii1 == 20
problem3 += Pi2 + Si1 - Si2 == 60
problem3 += Pii2 + Sii1 - Sii2 == 50
problem3 += Pi3 + Si2 == 80
problem3 += Pii3 + Sii2 == 90

#Confirmation of problem definition
print(problem3)

#Run
result = problem3.solve()

#Check the result
print("---1st month---")
print("Prodution I_1:" ,pulp.value(Pi1))
print("Prodution II_1:" ,pulp.value(Pii1))
print("Stock I_1:" ,pulp.value(Si1))
print("Stock II_1:" ,pulp.value(Sii1))

print("---2nd month---")
print("Prodution I_2:" ,pulp.value(Pi2))
print("Prodution II_2:" ,pulp.value(Pii2))
print("Stock I_2:" ,pulp.value(Si2))
print("Stock II_2:" ,pulp.value(Sii2))

print("---3rd month---")
print("Prodution I_3:" ,pulp.value(Pi3))
print("Prodution II_3:" ,pulp.value(Pii3))
print("Cost:" ,pulp.value(problem3.objective))



#Check the result
""" ---1st month---
Prodution I_1: 98.0
Prodution II_1: 100.0
Stock I_1: 68.0
Stock II_1: 80.0
---2nd month---
Prodution I_2: 8.0
Prodution II_2: 7.0
Stock I_2: 16.0
Stock II_2: 37.0
---3rd month---
Prodution I_3: 64.0
Prodution II_3: 53.0
Cost: 15741.0

The result was output that such a production plan should be made. 
The cost is lower than the answer to the example. You may have gotten better results than the example tool. """