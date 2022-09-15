""" Source : 
https://www.lindo.com/downloads/LINGO_text/Chapter6.pdf 



Product Mix Problems Chapter 6    103  
6.2 Example A certain plant can manufacture five different products in any combination. Each product requires time 
on each of three machines in the following manner (figures in minutes/unit): 

            Machine 
Product     1 2 3 
A           12 8 5 
B           7 9 10 
C           8 4 7 
D           10 0 3 
E           7 11 2 


Each machine is available 128 hours per week. 
 Products A, B, and C are purely competitive and any amounts made may be sold at respective prices 
of $5, $4, and $5. The first 20 units of D and E produced per week can be sold at $4 each, but all made 
in excess of 20 can only be sold at $3 each. Variable labor costs are $4 per hour for machines 1 and 2, 
while machine 3 labor costs $3 per hour. Material costs are $2 for products A and C, while products B, 
D, and E only cost $1. You wish to maximize profit to the firm. 
 The principal complication is that the profit contributions of products D and E are not linear. You 
may find the following device useful for eliminating this complication. Define two additional products 
D2 and E2, which sell for $3 per unit. What upper limits must then be placed on the sale of the original 
products D and E? The decision variables and their profit contributions are as follows:

Product Mix Problems Chapter 6    103  
6.2 Example A certain plant can manufacture five different products in any combination. Each product requires time 
on each of three machines in the following manner (figures in minutes/unit): 
 Machine 
Product 1 2 3 
A 12 8 5 
B 7 9 10 
C 8 4 7 
D 10 0 3 
E 7 11 2 
Each machine is available 128 hours per week. 
 Products A, B, and C are purely competitive and any amounts made may be sold at respective prices 
of $5, $4, and $5. The first 20 units of D and E produced per week can be sold at $4 each, but all made 
in excess of 20 can only be sold at $3 each. Variable labor costs are $4 per hour for machines 1 and 2, 
while machine 3 labor costs $3 per hour. Material costs are $2 for products A and C, while products B, 
D, and E only cost $1. You wish to maximize profit to the firm. 
 The principal complication is that the profit contributions of products D and E are not linear. You 
may find the following device useful for eliminating this complication. Define two additional products 
D2 and E2, which sell for $3 per unit. What upper limits must then be placed on the sale of the original 
products D and E? The decision variables and their profit contributions are as follows: 
 
Decision 
Variables 
 
A Number of units of A produced per week 5 − 2 = $3 
B Number of units of B produced per week 4 − 1 = $3 
C Number of units of C produced per week 5 − 2 = $3 
D Number  of  units  of D  not  in  excess  of  20 produced/week $3 
D2 Number of units of D produced in excess of 20 per week* $2 
E Number of units of E not  in excess of 20 produced/week $3 
E2 Number of units of E produced in excess of 20          $2 
M1 Hours of machine 1 used per week           −$4 
M2 Hours of machine 2 used per week           −$4 
M3 Hours of machine 3 used per week            −$3 
*Total production of product D is D + D2.

We  will  not  worry  about  issues  of  sequencing  the  various  products  on  each  machine.  This  is 
reasonable if the due-dates for the products are far enough in the future. Our problem in this case is to: 
Maximize     Revenues minus costs 
Subject to 
         Minutes used equals minutes run on each machine, 
         At most 20 units each can be produced of products D and E, 
         Each machine can be run at most 128 hours.

More precisely, the formulation in LINGO is: 

! Maximize revenue minus costs; 
MAX = 3 * A + 3 * B + 3 * C + 3 * D + 2 * D2 + 3 * E 
     + 2 * E2 - 4 * M1 - 4 * M2 - 3 * M3; 

! Machine time used = machine time made available; 
12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2 - 60*M1 = 0; 
8*A + 9*B + 4*C + 11*E + 11*E2 - 60*M2 = 0; 
5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2 - 60*M3=0; 
   D <= 20;  ! Max sellable at high price; 
   E <= 20; 

!Machine availability; 
   M1 <= 128; 
   M2 <= 128; 
   M3 <= 128; 
END 

 The first three constraints have the units of “minutes” and specify the hours of machine time as a 
function of the number of units produced. The next two constraints place upper limits on the number of 
high profit units of D and E that may be sold. The final three constraints put upper limits on the amount 
of machine time that may be used and have the units of “hours”. 
 Constraint 2 can be first written as: 
12A + 7B + 8C + 10D + 10D2 + 7E + 7E2 =M1 60 

Multiplying by 60 and bringing M1 to the left gives the second constraint. The solution is: 

Optimal solution found at step:         4 
Objective value:                 1777.625 
Variable           Value        Reduced Cost 
       A       0.0000000            1.358334 
       B       0.0000000           0.1854168 
       C        942.5000           0.0000000 
       D       0.0000000           0.1291668 
      D2       0.0000000            1.129167 
       E        20.00000           0.0000000 
      E2       0.0000000           0.9187501 
      M1        128.0000           0.0000000 
      M2        66.50000           0.0000000 
      M3        110.6250           0.0000000 
Product Mix Problems Chapter 6    105  
     Row    Slack or Surplus      Dual Price 
       1        1777.625            1.000000 
       2       0.0000000           0.2979167 
       3       0.0000000           0.6666667E-01 
       4       0.0000000           0.5000000E-01 
       5        20.00000           0.0000000 
       6       0.0000000           0.8125000E-01 
       7       0.0000000            13.87500 
       8        61.50000           0.0000000 
       9        17.37500           0.0000000

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
prob += 3 * A + 3 * B + 3 * C + 3 * D + 2 * D2 + 3 * E + 2 * E2 - 4 * M1 - 4 * M2 - 3 * M3, "Profit"
 
# Ensuite, On définit les contraintes.
prob += 12*A + 7*B + 8*C + 10*D + 10*D2 + 7*E +  7*E2 - 60*M1 == 0
prob += 8*A + 9*B + 4*C + 11*E + 11*E2 - 60*M2 == 0 
prob += 5*A + 10*B + 7*C + 3*D + 3*D2 + 2*E + 2*E2 - 60*M3 == 0 
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
M1 = 128.0
M2 = 66.5
M3 = 110.625

Objective : 1777.625
"""
