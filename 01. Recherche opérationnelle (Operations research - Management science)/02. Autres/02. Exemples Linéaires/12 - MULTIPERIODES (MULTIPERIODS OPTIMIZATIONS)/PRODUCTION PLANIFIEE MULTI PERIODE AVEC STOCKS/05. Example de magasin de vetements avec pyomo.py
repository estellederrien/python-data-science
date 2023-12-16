# https://www.quantmetry.com/blog/pyomo-optimisation-python/


import pyomo.environ as pyo

model = pyo.ConcreteModel(doc="Optimization model")

model.months = pyo.Set(initialize=(i for i in df.index),
doc="Index of variables")

def func_bounds_sales(model, month):
    return (0, df["Forecasted demand"].to_dict()[month])

model.sales = pyo.Var(model.months,
domain=pyo.NonNegativeIntegers,
bounds=func_bounds_sales,
doc="Optimized sales")

model.stocks = pyo.Var(model.months,
domain=pyo.NonNegativeIntegers,
doc="Optimized stocks")

model.sale_price = pyo.Param(default=10, doc="Unit selling price")
model.prod_cost = pyo.Param(default=4, doc="Unit production cost")
model.stock_cost = pyo.Param(default=1.1, doc="Monthly unit storage cost")
model.initial_stocks = pyo.Param(default=200, doc="Initial stocks")

def func_objective(model):
    objective_expr = sum([
    (model.sales[v] * model.sale_price)
    - (model.productions[v] * model.prod_cost)
    - (model.stocks[v] * model.stock_cost)
    for v in model.months
    ])
    return objective_expr
    model.objective = pyo.Objective(rule=func_objective,
    sense=pyo.maximize,
    doc="Objective function: maximize margin")

model.constraint_sales_prod_stocks = pyo.ConstraintList(doc="Balance sales, productions and stocks")

for month in model.months:
    if month==1: # January constraint
        model.constraint_sales_prod_stocks.add(
        model.sales[1] <= model.initial_stocks + model.productions[1]
        )
else: # Constraints from February to December
    model.constraint_sales_prod_stocks.add(
    model.sales[month] <= model.stocks[month - 1] +
    model.productions[month]
    )

model.constraint_stocks = pyo.ConstraintList(doc="Stocks constraints")
for month in model.months:
    if month==1: # January constraint
        model.constraint_stocks.add(
        model.stocks[1] == model.productions[1] - model.sales[1] + model.initial_stocks
        )
else: # Constraints from February to December
    model.constraint_stocks.add(
    model.stocks[month] == model.productions[month] - model.sales[month] + model.stocks[month-1]
    )

from pyomo.opt import SolverFactory

solver = SolverFactory("cbc", executable="../solvers/cbc-osx/cbc")
results = solver.solve(model)


print(model.sales[10].value)