""" Source : 
https://www.lindo.com/downloads/LINGO_text/Chapter6.pdf 

Version avec les contraintes simplifiées que l'on retrouve chez LINDO , 
Sauf qu'on comprends pas comment il a fait son calcul -> On tente de trouver comment il a fait ...

On voit qu'on a plus M1 M2 et M3 dans les résultats : 

106     Chapter 6  Product Mix Problems 
 
 This looks more like a standard product mix formulation. All the constraints are capacity constraints 
of some sort. Notice the solution to this formulation is really the same as the previous formulation: 
Optimal solution found at step:         6 
Objective value:                 1777.625 
Variable           Value        Reduced Cost 
       A       0.0000000            1.358333 
       B       0.0000000           0.1854170 
       C        942.5000           0.0000000 
       D       0.0000000           0.1291660 
      D2       0.0000000            1.129167 
       E        20.00000           0.0000000 
      E2       0.0000000           0.9187500 
"""


import pulp 

 
# Créer les variables du problème 
A = pulp.LpVariable("A", lowBound = 0, cat='')   
B = pulp.LpVariable("B", lowBound = 0, cat='Continuous')   
C = pulp.LpVariable("C", lowBound = 0, cat='Continuous')   
D = pulp.LpVariable("D", lowBound = 0, cat='Continuous')   
D2 = pulp.LpVariable("D2", lowBound = 0, cat='Continuous')   
E = pulp.LpVariable("E", lowBound = 0, cat='Continuous')   
E2 = pulp.LpVariable("E2", lowBound = 0, cat='Continuous')  
M1 = pulp.LpVariable("M1", lowBound = 0, cat='Continuous')   
M2 = pulp.LpVariable("M2", lowBound = 0, cat='Continuous')   
M3 = pulp.LpVariable("M3", lowBound = 0, cat='Continuous')    
 
# Créer un programme linéaire de minimisation
prob = pulp.LpProblem("problem", pulp.LpMaximize)

# écrire la fonction objectif à minimiser
#prob += 1.416667*A + 1.433333*B + 1.85*C + 2.183334*D + 1.183333*D2 + 1.7*E + .7*E2, "Profit"



prob += 3 * A + 3 * B + 3 * C + 3 * D + 2 * D2 + 3 * E + 2 * E2 - 4 * ((12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2)/60) - 4 * ((8*A + 9*B + 4*C + 11*E + 11*E2)/60) - 3 * ((5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2)/60), "Profit"
 

# Tentative de comprendre comment il a fait le calcul de cette nouvelle function objectif : 
# 3A + 3B + 3C + 3D + 2D2 + 3E + 2E2 - 4M1 - 4M2 - 3M3
# Il dit que M1 = (12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2)/60
# Il dit que M2 = ((12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2)/60
# Il dit que M3 = (5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2)/60
# Donc, si on substitue M1 M2 et M3 (qui sont le cout par machine) dans la function objectif: 
# 3A + 3B + 3C + 3D + 2D2 + 3E + 2E2 - 4 * ((12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2)/60) - 4 * ((8*A + 9*B + 4*C + 11*E + 11*E2)/60) - 3 * ((5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2)/60)

# ON REGARDE AVEC LA PREMIERE VAR DE DECISION SI ON TROUVE COMME LUI , si c'est bon pour ce calcul, c'est bon pour les autres vars de décision:
#  3A - 0.8A -  0.533A - 0.25A = 1.417 , donc oui, c'est à peu près comme lui, ce qu'il trouve dans sa fonction objectif  simplifiée .


# Ensuite, On définit les contraintes.
prob += 12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E + 7*E2 <= 7680; 
prob += 8*A + 9*B + 4*C + 11*E + 11*E2 <= 7680; 
prob += 5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2 <= 7680; 
prob += D <= 20 
prob += E <= 20 
prob += M1 <= 128 
prob += M2 <= 128 
prob += M3 <= 128 

# On résouds le problème linéaire
prob.solve()
 
# On imprime les résultats 

print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

pulp.LpStatus[prob.status]

# Print our objective function value
print (pulp.value(prob.objective))

""" 

Status: Optimal
A = 0.0
B = 0.0
C = 942.5
D = 0.0
D2 = 0.0
E = 20.0
E2 = 0.0
M1 = 0.0
M2 = 0.0
M3 = 0.0
1777.625
"""
