import pulp

#liste des solveurs dsiponibles avec pulp
solver_list = pulp.listSolvers(onlyAvailable=True)
print(solver_list)
#['PULP_CBC_CMD', 'PULP_CHOCO_CMD']
# On voit qu'il n'y a ni CPLEX ni gurobi