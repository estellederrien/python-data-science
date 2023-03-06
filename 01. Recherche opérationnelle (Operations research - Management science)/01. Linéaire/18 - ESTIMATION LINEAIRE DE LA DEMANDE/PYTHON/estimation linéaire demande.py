import gekko as op
import itertools as it

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Supply-Chain-Optimization-in-Python
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Supply-Chain-Optimization-in-Python
#============================================================================#

def model (U,T,a,b,solve="y"):
    m = op.GEKKO(remote=False, name='LinearRegressionProblem') 
    x = {i: m.Var(lb=None, ub=None) for i in U}
    z = m.Var(lb=None, ub=None)
    g = {t: m.Var(lb=None,ub=None) for t in T}    
    n_a = {(t,i): a[t][i] for t,i in it.product(T,U)}
    n_b = {t: b[t] for t in T}  
    objs = {0: (2*len(T))**(-1)*sum((g[t]-n_b[t])**2 for t in T)}
    cons = {0: {t: (g[t] == sum(n_a[(t,i)]*x[i] for i in U) + z) for t in T}}
    m.Minimize(objs[0])
    for keys1 in cons:
        for keys2 in cons[keys1]: m.Equation(cons[keys1][keys2])   
    if solve == "y":
        m.options.SOLVER=1
        m.solve(disp=True)
        for keys in x: 
            x[keys] =  x[keys].value[0]
            print(f"x[{keys}]", x[keys])
        z = z.value[0]
        print("z", z)
    return m,x,z

#     Monday   Tuesday    Wednesday   Thursday   Friday   Saturday   Sunday
a = [   [80],    [150],       [200],    [400],    [145],    [350],    [409]]    #Sales
b = [     20,       22,          18,       25,       55,       15,       21]    #Prices
U = range(len(a[0]))  #Set of input features
T = range(len(b))     #Set of the training points

m,x,z = model(U,T,a,b) #Model and solve the problem

#Developer: @KeivanTafakkori, 12 March 2022

def model (x,z):
    m = op.GEKKO(remote=False, name='PricingProblem') 
    q = m.Var(lb=0, ub=None)  
    objs = {0: z*q+x*(q**2)}
    m.Maximize(objs[0])
    m.options.SOLVER=2
    m.solve(disp=True)
    print("total revenue: ", z*q.value[0]+x*(q.value[0]**2), "$")
    print("marginal revenue: ", z+2*x*q.value[0], "$")
    print("optimal price (maximum willingness to pay): ", z+x*q.value[0], "$")
    print("optimal sales (consumption level): ", q.value[0] , "units")
    return m

x = x[0] #predicted slope of the demand function using linear regression
z = z #predicted intercept of the demand function using linear regression

m = model(x,z) #Model and solve the problem