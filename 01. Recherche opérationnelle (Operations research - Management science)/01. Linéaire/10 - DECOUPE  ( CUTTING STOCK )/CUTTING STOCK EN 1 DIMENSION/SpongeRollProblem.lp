\* Cutting_Stock_Problem *\
Minimize
Production_Cost: Patt_A + Patt_B + Patt_C
Subject To
Ensuring_enough_5_cm_rolls: 2 Patt_B + 2 Patt_C >= 150
Ensuring_enough_7_cm_rolls: Patt_A + Patt_B >= 200
Ensuring_enough_9_cm_rolls: Patt_A + Patt_C >= 300
Bounds
0 <= Patt_A
0 <= Patt_B
0 <= Patt_C
Generals
Patt_A
Patt_B
Patt_C
End
