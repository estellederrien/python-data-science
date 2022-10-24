# http://benalexkeen.com/linear-programming-with-python-and-pulp-part-3/

# Maximiser le profit 
# Nous consultons un constructeur de voitures de boutique qui produit des voitures de luxe.
# Ils fonctionnent sur des cycles d'un mois (30 jours), nous avons un cycle pour montrer que nous pouvons apporter de la valeur.
# Il y a un robot, 2 ingénieurs et un dessinateur dans l'usine. Le détaillant a des vacances, il ne lui reste donc que 21 jours.
# Les 2 voitures ont besoin de temps différent avec chaque ressource:
# Temps du robot: voiture A - 3 jours; Voiture B - 4 jours.
# Temps ingénieur: voiture A - 5 jours; Voiture B - 6 jours.
# Temps Detailer: Voiture A - 1,5 jours; Voiture B - 3 jours.
# La voiture A génère un bénéfice de 30 000 €, tandis que la voiture B offre un bénéfice de 45 000 €.
# Actuellement, ils produisent 4 voitures par mois, pour un bénéfice de 300 000 €. Pas mal du tout, mais nous pensons que nous pouvons faire mieux pour eux.

# Modélisation
# Maximise la fonction économique :

# Profit=30,000A+45,000B

# Contraintes :

# A≥0
# B≥0
# 3A+4B≤30
# 5A+6B≤60
# 1.5A+3B≤21

# Importer la librairie Pulp 
import pulp 
  
# Créer un programme linéaire de maximisation
model = pulp.LpProblem("Maximiser le profit", pulp.LpMaximize)
  
# Créer les variables du problème 
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')
  
# Function économique objectif
model += 30000 * A + 45000 * B, "Profit"

# Contraintes
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21
  
# Résoudre le problème
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print ("Production of Car A = {}".format(A.varValue))
print ("Production of Car B = {}".format(B.varValue))
  
# Print our objective function value
print (pulp.value(model.objective))

# LES SOLUTIONS pour Maximiser la fonction économique sont A = 2.0 et B = 6.0
