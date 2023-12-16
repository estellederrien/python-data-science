from pulp import *
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

problem = pulp.LpProblem("A simple max problem", LpMaximize)

problem += 300*x + 250*y, "The objective function"

# Constraints
problem += 1.4*x + y <= 35000, "1st constraint"
problem += 0.51*x + y <= 17000, "2nd constraint"
problem += x <= 22500, "3rd constraint"
problem += y <= 15000, "4th constraint"

problem.solve()

print ("Optimal Result:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)

print ("Total net max profit:")
print (value(problem.objective))

constraints = problem.constraints
print(f'The constraints are held in a {type(constraints)}')

for name in constraints.keys():
    value = constraints.get(name).value()
    slack = constraints.get(name).slack
    print(f'constraint {name} has value: {value:0.2e} and slack: {slack:0.2e}')

#     ...
# Optimal Result:
# x = 20224.719
# y = 6685.3933
# Total net max profit:
# 7738764.025
# The constraints are held in a <class 'collections.OrderedDict'>
# constraint 1st_constraint has value: -1.00e-04 and slack: -0.00e+00
# constraint 2nd_constraint has value: -1.00e-05 and slack: -0.00e+00
# constraint 3rd_constraint has value: -2.28e+03 and slack: 2.28e+03
# constraint 4th_constraint has value: -8.31e+03 and slack: 8.31e+03