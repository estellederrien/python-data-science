""" Lien : http://people.brunel.ac.uk/~mastjjb/jeb/or/morelp.html
Linear programming example 1994 UG exam

A company is involved in the production of two items (X and Y). The resources need to produce X and Y are twofold, namely machine time for automatic processing and craftsman time for hand finishing. The table below gives the number of minutes required for each item:

         Machine time Craftsman time
Item X   13           20
     Y   19           29

The company has 40 hours of machine time available in the next working week but only 35 hours of craftsman time. Machine time is costed at £10 per hour worked and craftsman time is costed at £2 per hour worked. Both machine and craftsman idle times incur no costs. The revenue received for each item produced (all production is sold) is £20 for X and £30 for Y. The company has a specific contract to produce 10 items of X per week for a particular customer.

    Formulate the problem of deciding how much to produce per week as a linear program.
    Solve this linear program graphically.

Solution

Let

    x be the number of items of X
    y be the number of items of Y

then the LP is:

maximise

    20x + 30y - 10(machine time worked) - 2(craftsman time worked)

subject to:

    13x + 19y <= 40(60) machine time
    20x + 29y <= 35(60) craftsman time
    x >= 10 contract
    x,y >= 0

so that the objective function becomes

maximise

    20x + 30y - 10(13x + 19y)/60 - 2(20x + 29y)/60

i.e. maximise

    17.1667x + 25.8667y

subject to:

    13x + 19y <= 2400
    20x + 29y <= 2100
    x >= 10
    x,y >= 0

It is plain from the diagram below that the maximum occurs at the intersection of x=10 and 20x + 29y <= 2100

Solving simultaneously, rather than by reading values off the graph, we have that x=10 and y=65.52 with the value of the objective function being £1866.5

 """



import pulp 

 
# Créer les variables du problème 
x = pulp.LpVariable("x", lowBound = 0, cat='Continuous')   
y = pulp.LpVariable("y", lowBound = 0, cat='Continuous')   
  
# Créer un programme linéaire de minimisation
prob = pulp.LpProblem("problem", pulp.LpMaximize)

# écrire la fonction objectif à maximiser

prob += 20 * x + 30 * y - 10 * (13 * x + 19 * y)/60 - 2 * (20 * x + 29 * y)/60, "Profit"
 
# Ensuite, On définit les contraintes.
prob +=  13 * x + 19 * y <= 40 * 60 
prob +=  20 * x + 29 * y <= 35 * 60 
prob +=  x >= 10 
prob +=  x >= 0
prob +=  y >= 0

# On résouds le problème linéaire
prob.solve()
 
# On imprime les résultats 

print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

pulp.LpStatus[prob.status]

# Print our objective function value
print (pulp.value(prob.objective))


