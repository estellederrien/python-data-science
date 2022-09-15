# Lists (sets / Array) of Customers and Facilities
Customer = [1,2,3,4,5]
Facility = ['Fac-1', 'Fac-2', 'Fac-3']

# Dictionary of distances in kms
distance = {'Fac-1' : {1 : 54, 2 : 76, 3 : 5, 4 : 76, 5 : 76},
            'Fac-2' : {1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1},
            'Fac-3' : {1 : 45, 2 : 23, 3 : 54, 4 : 87, 5 : 88}
            }

# Setting the Problem
prob = LpProblem("pb", LpMinimize)

# Defining our Decision Variables
use_facility = LpVariable.dicts("Use Facility", Facility, 0, 1, LpBinary)
ser_customer = LpVariable.dicts("Service", [(i,j) for i in Customer for j in Facility], 0)

# Setting the Objective Function = Minimize amount of facilities and arcs
prob += lpSum(use_facility['Fac-1']+use_facility['Fac-2']+use_facility['Fac-3']) + lpSum(distance[j][i]*ser_customer[(i,j)] for j in Facility for i in Customer)

# Constraints,to be covered,an arc has to be shorter than 5 kms
for i in Customer:
    prob += lpSum(ser_customer[(i,j)] for j in Facility) < 5

prob.solve()

# Print the solution of Decision Variables
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the solution of Binary Decision Variables
Tolerance = 0.0001
for j in Facility:
    if use_facility[j].varValue > Tolerance:
        print("Estalish Facility at site = ", j)


