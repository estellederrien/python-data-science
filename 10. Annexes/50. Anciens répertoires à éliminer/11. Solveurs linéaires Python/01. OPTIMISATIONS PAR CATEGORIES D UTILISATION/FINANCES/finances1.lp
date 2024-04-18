\* A_cost_minimization_problem *\
Minimize
Minimize_portfolio_cost: 4000 orders_X + 2000 orders_Y + 6000 orders_Z
 + 500 quantity_X + 350 quantity_Y + 450 quantity_Z
Subject To
Boundary_of_total_volume_of_X: - 100 orders_X + quantity_X <= 0
Boundary_of_total_volume_of_Y: - 90 orders_Y + quantity_Y <= 0
Boundary_of_total_volume_of_Z: - 70 orders_Z + quantity_Z <= 0
Total_contracts_required: quantity_X + quantity_Y + quantity_Z = 150
Bounds
0 <= quantity_X
0 <= quantity_Y
0 <= quantity_Z
Generals
quantity_X
quantity_Y
quantity_Z
Binaries
orders_X
orders_Y
orders_Z
End
