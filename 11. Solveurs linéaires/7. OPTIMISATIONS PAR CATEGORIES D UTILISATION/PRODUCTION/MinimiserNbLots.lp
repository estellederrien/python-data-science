\* MinimiserDemande *\
Minimize
MinimiserNbLots: lots_lot1 + lots_lot2
Subject To
MinNbLots1: lots_lot1 >= 0
MinNbLots2: lots_lot2 >= 0
contrainteMinVilleA: 12 lots_lot1 + 9 lots_lot2 >= 108
contrainteMinVilleB: 8 lots_lot1 + 12 lots_lot2 >= 96
End
