# http://www.learningaboutelectronics.com/Articles/How-to-solve-quadratic-equations-in-Python-using-sympy.php

from sympy import Symbol, solve

x= Symbol('x')

expression= x**2+7*x+6

roots= solve(expression, dict=False)

print(roots)

print(roots[0])