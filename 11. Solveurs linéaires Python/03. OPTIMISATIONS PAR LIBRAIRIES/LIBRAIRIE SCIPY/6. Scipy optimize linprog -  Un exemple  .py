# source : https://yiyibooks.cn/sorakunnn/scipy-1.0.0/scipy-1.0.0/generated/scipy.optimize.linprog.html




# Example

""" 

Minimiser: f = -1*x[0] + 4*x[1]

Sous les contraintes : 

    -3*x[0] + 1*x[1]    <= 6
    1*x[0] + 2*x[1]     <= 4
    x[1]                >= -3

ou : -inf <= x[0] <= inf 

Ce problème s'écarte du problème de programmation linéaire standard. 
Dans la forme standard, les problèmes de programmation linéaire supposent que les variables x sont non négatives. 
Étant donné que les variables n’ont pas de limites standard où 0 <= x <= inf, 
les limites des variables doivent être définies explicitement.
Il existe deux contraintes de limite supérieure, qui peuvent être exprimées comme

point (A_ub, x) <= b_ub

L'entrée de ce problème est la suivante:
"""
from scipy.optimize import linprog
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
from scipy.optimize import linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
              options={"disp": True})



print(res)


# Notez que la valeur réelle de l'objectif est 11,428571. Dans ce cas, nous avons minimisé le négatif de la fonction objectif.




"""  scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None, options=None)[source]

    Minimize a linear objective function subject to linear equality and inequality constraints.

    Linear Programming is intended to solve the following problem form:

    Minimize:     c^T * x

    Subject to:   A_ub * x <= b_ub
                  A_eq * x == b_eq

    Parameters:	

    c : array_like

        Coefficients of the linear objective function to be minimized.

    A_ub : array_like, optional

        2-D array which, when matrix-multiplied by x, gives the values of the upper-bound inequality constraints at x.

    b_ub : array_like, optional

        1-D array of values representing the upper-bound of each inequality constraint (row) in A_ub.

    A_eq : array_like, optional

        2-D array which, when matrix-multiplied by x, gives the values of the equality constraints at x.

    b_eq : array_like, optional

        1-D array of values representing the RHS of each equality constraint (row) in A_eq.

    bounds : sequence, optional

        (min, max) pairs for each element in x, defining the bounds on that parameter. Use None for one of min or max when there is no bound in that direction. By default bounds are (0, None) (non-negative) If a sequence containing a single tuple is provided, then min and max will be applied to all variables in the problem.

    method : str, optional

        Type of solver. ‘simplex’ and ‘interior-point’ are supported.

    callback : callable, optional (simplex only)

        If a callback function is provide, it will be called within each iteration of the simplex algorithm. The callback must have the signature callback(xk, **kwargs) where xk is the current solution vector and kwargs is a dictionary containing the following:

        "tableau" : The current Simplex algorithm tableau
        "nit" : The current iteration.
        "pivot" : The pivot (row, column) used for the next iteration.
        "phase" : Whether the algorithm is in Phase 1 or Phase 2.
        "basis" : The indices of the columns of the basic variables.

    options : dict, optional

        A dictionary of solver options. All methods accept the following generic options:

            maxiter : int

                Maximum number of iterations to perform.
            disp : bool

                Set to True to print convergence messages.

        For method-specific options, see show_options('linprog').

    Returns:	

    A scipy.optimize.OptimizeResult consisting of the following fields:

        x : ndarray

            The independent variable vector which optimizes the linear programming problem.
        fun : float

            Value of the objective function.
        slack : ndarray

            The values of the slack variables. Each slack variable corresponds to an inequality constraint. If the slack is zero, then the corresponding constraint is active.
        success : bool

            Returns True if the algorithm succeeded in finding an optimal solution.
        status : int

            An integer representing the exit status of the optimization:

            0 : Optimization terminated successfully
            1 : Iteration limit reached
            2 : Problem appears to be infeasible
            3 : Problem appears to be unbounded

        nit : int

            The number of iterations performed.
        message : str

            A string descriptor of the exit status of the optimization. """

