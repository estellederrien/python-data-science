\* MinimiserDemande *\
Minimize
MinimiserNbLots: distributeur_distributeur1 + distributeur_distributeur2
Subject To
MinNbDistributeur1: distributeur_distributeur1 >= 0
MinNbDistributeur2: distributeur_distributeur2 >= 0
contrainteMinVilleA: 12 distributeur_distributeur1
 + 9 distributeur_distributeur2 >= 108
contrainteMinVilleB: 8 distributeur_distributeur1
 + 12 distributeur_distributeur2 >= 96
Bounds
distributeur_distributeur1 free
distributeur_distributeur2 free
Generals
distributeur_distributeur1
distributeur_distributeur2
End
