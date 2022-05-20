""" #
Dans cette exemple de Stuart Mitchell, 
On ne trouve que des pourcentages exprimés en décimales dans les contraintes.
Il y a aussi la contrainte finale qui stipule que le total des variables de décision est de 100 ( 100 %)
Il n'y a pas de contraintes qui font des "mixes" entre unités et pourcentages.
https://rstudio-pubs-static.s3.amazonaws.com/274314_43b04185a4b84a0fb1113819d59b55c0.html
# """



import pulp
from pulp import *

prob = LpProblem("The Whiskas Problem",LpMinimize)
LpVariable("example", None, 100)
x1=LpVariable("ChickenPercent",0,None,LpInteger)
x2=LpVariable("BeefPercent",0)
prob += 0.013*x1 + 0.008*x2, "Total Cost of Ingredients per can"
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100*x1 + 0.200*x2 >= 8.0, "ProteinRequirement"
prob += 0.080*x1 + 0.100*x2 >= 6.0, "FatRequirement"
prob += 0.001*x1 + 0.005*x2 <= 2.0, "FibreRequirement"
prob += 0.002*x1 + 0.005*x2 <= 0.4, "SaltRequirement"

prob.writeLP("WhiskasModel.lp")
prob.solve()
print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients per can = ", value(prob.objective))
#The 2 outputs above tell us that chicken makes up 33.33% and Beef makes up 66.67%. 

#The total cost of ingredients per can is 96 cents.