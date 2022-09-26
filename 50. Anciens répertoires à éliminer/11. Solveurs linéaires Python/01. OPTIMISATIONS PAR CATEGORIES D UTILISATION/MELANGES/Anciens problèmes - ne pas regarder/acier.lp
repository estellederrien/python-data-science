\* MinimiserLpAlliage *\
Minimize
CoutAlliages: 1.2 Alliage_d'alu_1 + Alliage_d'alu_2 + 1.3 Alliage_de_cuivre_1
 + 1.45 Alliage_de_cuivre_2 + 1.2 Alliage_de_fer_1 + 1.5 Alliage_de_fer_2
 + 0.9 Alliage_de_fer_3
Subject To
MaxStock: Alliage_de_fer_1 <= 4000
MaxStock1: Alliage_de_fer_2 <= 3000
MaxStock2: Alliage_de_fer_3 <= 6000
MaxStock3: Alliage_de_cuivre_1 <= 5000
MaxStock4: Alliage_de_cuivre_2 <= 2000
MaxStock5: Alliage_d'alu_1 <= 3000
MaxStock6: Alliage_d'alu_2 <= 2500
QuantitéDemandée: Alliage_d'alu_1 + Alliage_d'alu_2 + Alliage_de_cuivre_1
 + Alliage_de_cuivre_2 + Alliage_de_fer_1 + Alliage_de_fer_2
 + Alliage_de_fer_3 = 5000
carBmax: 0.0002 Alliage_d'alu_1 + 0.0002 Alliage_d'alu_2
 + 0.0002 Alliage_de_cuivre_1 + 0.0002 Alliage_de_cuivre_2
 + 0.0005 Alliage_de_fer_1 + 0.0006 Alliage_de_fer_2 + 0.0002 Alliage_de_fer_3
 <= 3
carBmin: 0.0002 Alliage_d'alu_1 + 0.0002 Alliage_d'alu_2
 + 0.0002 Alliage_de_cuivre_1 + 0.0002 Alliage_de_cuivre_2
 + 0.0005 Alliage_de_fer_1 + 0.0006 Alliage_de_fer_2 + 0.0002 Alliage_de_fer_3
 >= 2
cuBmax: 8e-05 Alliage_d'alu_1 + 0.00012 Alliage_d'alu_2
 + 0.018 Alliage_de_cuivre_1 + 0.0192 Alliage_de_cuivre_2
 + 0.0002 Alliage_de_fer_1 + 0.0002 Alliage_de_fer_2 + 6e-05 Alliage_de_fer_3
 <= 0.6
cuBmin: 8e-05 Alliage_d'alu_1 + 0.00012 Alliage_d'alu_2
 + 0.018 Alliage_de_cuivre_1 + 0.0192 Alliage_de_cuivre_2
 + 0.0002 Alliage_de_fer_1 + 0.0002 Alliage_de_fer_2 + 6e-05 Alliage_de_fer_3
 >= 0.4
mgBmax: 0.00024 Alliage_d'alu_1 + 0.0002 Alliage_d'alu_2
 + 0.0002 Alliage_de_cuivre_1 + 0.0008 Alliage_de_cuivre_2
 + 0.00026 Alliage_de_fer_1 + 0.00016 Alliage_de_fer_2
 + 0.0002 Alliage_de_fer_3 <= 1.65
mgBmin: 0.00024 Alliage_d'alu_1 + 0.0002 Alliage_d'alu_2
 + 0.0002 Alliage_de_cuivre_1 + 0.0008 Alliage_de_cuivre_2
 + 0.00026 Alliage_de_fer_1 + 0.00016 Alliage_de_fer_2
 + 0.0002 Alliage_de_fer_3 >= 1.2
End
