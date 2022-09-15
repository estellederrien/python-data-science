 # https://www.researchgate.net/publication/313795195_Optimization_of_Fixed_Charge_Problem_in_Python_using_PuLP_Package
 import libraries
from pulp import *
# variable assignment
 facility = [‘f1’,’f2 ’,’f3’]
 location = [‘d1’,’d2’,’d3’,’d4’,’d5’,’d6’,’d7’,’d8’]
 f  =  dict(zip(facility, [5000000, 4000000, 5500000]))
  K  =  dict(zip(facility, [1000000, 800000, 1250000]))
  D  =  dict(zip(location, [200000, 200000, 200000, 200000,
      250000, 250000, 250000, 250000]))
  C  =  dict(zip(facility,[dict(zip(location, [4, 5, 5, 4, 4, 4.2, 3.3, 5])),
      dict(zip(location, [2.5, 3.5, 4.5, 3, 2.2, 4, 2.6, 5])),
      dict(zip(location, [2, 4, 5, 2.5, 2.6, 3.8, 2.9, 5.5]))]))
 p = 2
# decision variables  X  =  Lp Variable.dicts (‘X%s%s’, (facility, location),
 cat = ‘Continuous’, 
 lowBound = 0,
 up Bound = None)
 Y = LpVariable.dicts(‘Y%s’, facility, 
 cat = ‘Binary’, 
446 Anand Jayakumar A, Krishnaraj C and Raghunayagan P
 lowBound = 0,
 upBound = 1)
# create the LP object, set up as a MINIMIZATION problem
 prob  =  LpProblem(‘Fixed Charge’, LpMinimize)
 tmp1 = sum(f [i] * Y[i] for i in facility)
 tmp2 = sum(sum(C[i][j] * X[i][j] for j in location) for i in facility)
  prob +  =  tmp1 + tmp2
# setup constraints  prob +  =  sum(Y[i] for i in facility) == p
for i in facility:  prob +  =  sum(X[i][j] for j in location) <= K[i]*Y[i]
for j in location:  prob +  =   sum(X[i][j] for i in facility) >= D[j]
# save the model to a lp ﬁ le
prob.writeLP(“ﬁ xed-charge.lp”)
# view the model
print(prob)
# solve the model
prob.solve()
print(“Status:”,LpStatus[prob.status])
print(“Objective: “,value(prob.objective))
for v in prob.variables():
print (v.name , “=”, v.varValue)