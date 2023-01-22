""" Résoudre un système d'équations simple 

On me donne ce simple système d'équation :
# 1x + 1y = 35
# 2x + 4y = 94

Résoudre :
1. En utilisant les tableaux (Arrays) et la librairie numpy 
2. En utilisant les symboles et la librairie sympy 


Sources :
Sympy documentation totale :
https://scipy-lectures.org/packages/sympy.html

https://alexandrugris.github.io/maths/2017/04/30/symbolic-maths-python.html

https://apmonitor.com/che263/index.php/Main/PythonSolveEquations

https://medium.com/@GalarnykMichael/solving-system-of-linear-equations-using-python-645ad1904cec
"""

# 1. En utilisant les tableaux (Arrays) et la librairie numpy 
# On voit que l'index 1 des tableaux de a équivalent à x, et que l'index 2 des tableaux de a équivalent à y
import numpy as np
a = np.array([[1, 1],[2,4]])
b = np.array([35, 94])
print("Mon couple de resultats est : ",np.linalg.solve(a,b))

# 2. En utilisant les symboles et la librairie sympy 

import sympy as sp
x, y = sp.symbols('x, y')
eq1 = sp.Eq(x + y, 35)               # 1x + 1y = 35
eq2 = sp.Eq(2*x + 4*y , 94)          # 2x + 4y = 94
ans = sp.solve((eq1, eq2), (x, y))
print("Mon couple de resultats est : ",ans)

