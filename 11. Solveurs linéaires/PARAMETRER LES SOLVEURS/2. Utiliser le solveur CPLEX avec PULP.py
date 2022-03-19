path_to_cplex = r'C:/Program Files/IBM/ILOG/CPLEX_Studio_Community201/cplex/bin/x64_win64/cplex.exe'

import pulp as pl


model = pl.LpProblem("Example", pl.LpMinimize)
solver = pl.CPLEX_CMD(path=path_to_cplex)
_var = pl.LpVariable('a')
_var2 = pl.LpVariable('a2')
model += _var + _var2 == 1
print("test")
result = model.solve(solver)


"""
facc58cf08ee0-pulp.sol


Minimize
OBJ: __dummy
Subject To
_C1: a + a2 = 1
Bounds
__dummy = 0
a free
a2 free
End

 """

print(result)