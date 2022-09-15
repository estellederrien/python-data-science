
""" 
Exemple simple d'optimization de portefeuille de trading :

Supposons que nous souhaitons investir dans deux titres, x et y. 

Nous aimerions connaître le nombre réel d'unités à investir pour 3 unités de titre X et 2 unités de titre Y, 
de sorte que le nombre total d'unités investies soit maximisé, dans la mesure du possible. 

Cependant, certaines contraintes pèsent sur notre stratégie d'investissement: 

• Pour 2 unités de titre X investies et 1 unité de titre Y investie, le volume total ne doit pas dépasser 100 

• Pour chaque unité de titre X et Y investie, le volume total doit ne pas dépasser 80 

• Le volume total autorisé pour investir dans le titre X ne doit pas dépasser 40 

• La vente à découvert n'est pas autorisée pour les deux titres 


Le problème de maximisation peut être mathématiquement représenté comme suit:

Maximize: f(x,y) = 3x+2y :Subject to
2 x + y ≤ 100
x + y ≤ 80
x ≤ 40 
x ≥ 0 , y ≥ 0 

SOURCE : Mastering Python for Finance.pdf

"""



from pulp import *

# On crée les variables de décision
x = LpVariable("x", lowBound=0) 
y = LpVariable("y", lowBound=0)

# On dit que c'est un problème de maximization.
problem = LpProblem("A simple maximization objective",LpMaximize) 

# Voici notre function objectif à maximizer
problem += 3*x + 2*y,"The objective function" 

# Voici nos contraintes
problem += 2*x + y <= 100,"1st constraint" 
problem += x + y <= 80,"2nd constraint" 
problem += x <= 40,"3rd constraint" 

problem.writeLP("finances1.lp")

# On résouds le problème, en fait, on déroule l'algo du simplexe.
problem.solve()


print("Status:", LpStatus[problem.status])

for v in problem.variables():
    print(v.name, "=", v.varValue)
