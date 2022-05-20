# https://stackoverflow.com/questions/56626611/pulp-taking-too-much-time-to-solve
# https://drive.google.com/drive/folders/1Ih8Y8baIRQ3Z8SIXOzGHIeorcLcK1DWn
def allocator(item_mass, item_vol, truck_mass, truck_vol, truck_cost, id_series):
    n_items = len(item_vol)
    set_items = range(n_items)
    n_trucks = len(truck_cost)
    set_trucks = range(n_trucks)


    y = pulp.LpVariable.dicts('truckUsed', set_trucks,
        lowBound=0, upBound=1, cat=LpInteger)

    x = pulp.LpVariable.dicts('itemInTruck', (set_items, set_trucks), 
        lowBound=0, upBound=1, cat=LpInteger)

    # Model formulation
    prob = LpProblem("Truck allocation problem", LpMinimize)

    # Objective
    prob += lpSum([truck_cost[i] * y[i] for i in set_trucks])
    # Constraints
    for j in set_items:
        # Every item must be taken in one truck
        prob += lpSum([x[j][i] for i in set_trucks]) == 1

    for i in set_trucks:
        # Respect the mass constraint of trucks
        prob += lpSum([item_mass[j] * x[j][i] for j in set_items]) <= truck_mass[i]*y[i]

        # Respect the volume constraint of trucks
        prob += lpSum([item_vol[j] * x[j][i] for j in set_items]) <= truck_vol[i]*y[i]
    # Ensure y variables have to be set to make use of x variables:
    for j in set_items:
        for i in set_trucks:
            x[j][i] <= y[i]

    s = id_series  # id_series

    prob.solve()