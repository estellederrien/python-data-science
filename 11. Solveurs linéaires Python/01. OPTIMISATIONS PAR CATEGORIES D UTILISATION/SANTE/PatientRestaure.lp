\* Un_patient_restauré *\
Maximize
Health_restored;_to_be_maximized: 25 Medicine_1_units + 20 Medicine_2_units
Subject To
Herbe_A_contrainte: 3 Medicine_1_units + 4 Medicine_2_units <= 25
Herbe_B_contrainte: 2 Medicine_1_units + Medicine_2_units <= 10
Bounds
0 <= Medicine_1_units
0 <= Medicine_2_units
Generals
Medicine_1_units
Medicine_2_units
End
