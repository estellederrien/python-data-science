\* MinimiserLpAlliage *\
Minimize
AlliageCost: 1.2 input_mat_al_1 + input_mat_al_2 + 1.3 input_mat_cu_1
 + 1.45 input_mat_cu_2 + 1.2 input_mat_iron_1 + 1.5 input_mat_iron_2
 + 0.9 input_mat_iron_3
Subject To
MaxCarbon: 0.025 input_mat_iron_1 + 0.03 input_mat_iron_2 <= 0.03
MaxCu: 0.004 input_mat_al_1 + 0.006 input_mat_al_2 + 0.9 input_mat_cu_1
 + 0.96 input_mat_cu_2 + 0.003 input_mat_iron_3 <= 0.006
MaxMn: 0.012 input_mat_al_1 + 0.04 input_mat_cu_2 + 0.013 input_mat_iron_1
 + 0.008 input_mat_iron_2 <= 0.0165
MinCarbon: 0.025 input_mat_iron_1 + 0.03 input_mat_iron_2 >= 0.02
MinCu: 0.004 input_mat_al_1 + 0.006 input_mat_al_2 + 0.9 input_mat_cu_1
 + 0.96 input_mat_cu_2 + 0.003 input_mat_iron_3 >= 0.004
MinMn: 0.012 input_mat_al_1 + 0.04 input_mat_cu_2 + 0.013 input_mat_iron_1
 + 0.008 input_mat_iron_2 >= 0.012
conservation: input_mat_al_1 + input_mat_al_2 + input_mat_cu_1
 + input_mat_cu_2 + input_mat_iron_1 + input_mat_iron_2 + input_mat_iron_3 = 1
End
