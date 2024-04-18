import pulp as pl


cities = ['London', 'Paris', 'Berlin', 'Amsterdam', 'Vienna', 'Prague']
factories = ['A', 'B', 'C', 'D']
city_populations = {'London': 898, 'Paris': 222, 'Berlin': 767, 'Amsterdam': 111, 'Vienna': 854, 'Prague': 908}
factories_service = {'A': ['London', 'Prague'], 'B': ['London', 'Paris', 'Vienna'], 'C': ['Amsterdam', 'Vienna', 'Prague'], 'D': ['London', 'Vienna', 'Prague']}



prob = pl.LpProblem("Factory Coverage",pl.LpMinimize)

factories_vars = pl.LpVariable.dicts("Factories", factories, cat='Binary')
cities_vars = pl.LpVariable.dicts("Cities", cities, cat='Binary')

# Objective function
prob += pl.lpSum(factories_vars)
# Population served is greater than 4000
prob += pl.lpSum([city_populations[c]*cities_vars[c] for c in cities]) >= 2000
# City is served only if there is a factory that serves it
bigM = len(factories)
for c in cities:
    prob +=  bigM * cities_vars[c] >= pl.lpSum([factories_vars[f] for f in factories_vars if c in factories_service[f]])
    prob +=  cities_vars[c] <= pl.lpSum([factories_vars[f] for f in factories_vars if c in factories_service[f]])

prob.solve()

for f in factories_vars:
    print(f, factories_vars[f].value())
for c in cities_vars:
    print(c, cities_vars[c].value())


