

# https://apmonitor.com/pdc/index.php/Main/LinearProgramming

# Exercice : Production de boissons gazeuses

# Un problème simple de planification de la production est donné par l'utilisation 
# de deux ingrédients A et B qui produisent les produits 1 et 2. 
# L'offre disponible est A = 30 unités et B = 44 unités. 
# Pour la production, il faut:

#     3 unités de A et 8 unités de B pour produire le Produit 1
#     6 unités de A et 4 unités de B pour produire le produit 2

# Il y a au plus 5 unités de Produit 1 et 4 unités de Produit 2. 
# Le Produit 1 peut être vendu pour 100 et le Produit 2 peut être vendu pour 125. 
# L'objectif est de maximiser le profit pour ce problème de production. 


from gekko import GEKKO
m = GEKKO()
x1 = m.Var(lb=0, ub=5,integer=True) # Product 1 // Bizarre Integer n'est pas pris en compte
x2 = m.Var(lb=0, ub=4,integer=True) # Product 2
m.Maximize(100*x1+125*x2) # Profit function
m.Equation(3*x1+6*x2<=30) # Units of A
m.Equation(8*x1+4*x2<=44) # Units of B
m.solve(disp=False)
p1 = x1.value[0]; p2 = x2.value[0]
print ('Product 1 (x1): ' + str(p1))
print ('Product 2 (x2): ' + str(p2))
print ('Profit        : ' + str(100*p1+125*p2))

