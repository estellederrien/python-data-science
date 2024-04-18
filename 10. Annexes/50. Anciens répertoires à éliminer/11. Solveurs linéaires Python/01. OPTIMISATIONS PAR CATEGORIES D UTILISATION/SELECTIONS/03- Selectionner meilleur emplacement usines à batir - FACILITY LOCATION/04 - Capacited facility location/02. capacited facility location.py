# https://stackoverflow.com/questions/72309038/facility-location-problem-in-python-with-pulp
from pulp import *

Customer = [1, 2, 3, 4]
Facility = ['Fac-1', 'Fac-2', 'Fac-3']
Demand = {1: 50, 2: 50, 3: 75, 4: 75}
Max_Supply = {'Fac-1': 100, 'Fac-2': 100, 'Fac-3': 500}
fixed_cost = {'Fac-1': 100.123, 'Fac-2': 100.456, 'Fac-3': 100.789}
transportation_cost = {'Fac-1': {1: 100.1, 2: 100.4, 3: 200.7, 4: 200.1}, 'Fac-2': {1: 200.2, 2: 200.5, 3: 100.8, 4: 200.11}, 'Fac-3': {1: 2000.3, 2: 2000.6, 3: 2000.9, 4: 100.12}}

prob = LpProblem("Capacitated_Facility_Location_Problem", LpMinimize)

use_facility = LpVariable.dicts("Use Facility", Facility, 0, 1, LpBinary)

ser_customer = LpVariable.dicts("Service", [(i,j) for i in Customer for j in Facility], 0)

fixed = lpSum(fixed_cost[j]*use_facility[j] for j in Facility)
transpo = lpSum(transportation_cost[j][i]*ser_customer[(i,j)] for j in Facility for i in Customer)  
prob += fixed + transpo

for i in Customer:
    prob += lpSum(ser_customer[(i,j)] for j in Facility) == Demand[i]

for j in Facility:
    prob += lpSum(ser_customer[(i,j)] for i in Customer) <= Max_Supply[j]*use_facility[j]

for i in Customer:
    for j in Facility:
        prob += ser_customer[(i,j)] <= Demand[i]*use_facility[j]

prob.solve()
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)