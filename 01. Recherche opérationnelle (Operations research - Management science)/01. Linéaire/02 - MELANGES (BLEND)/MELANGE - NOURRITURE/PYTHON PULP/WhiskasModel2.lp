\* The_Whiskas_Problem *\
Minimize
Cout_total_des_ingrédients_par_boite_de_conserve_de_100g: 0.013 Ingr_POULET
 + 0.008 Ingr_VIANDE
Subject To
FatRequirement: 0.08 Ingr_POULET + 0.1 Ingr_VIANDE >= 6
PercentagesSum: Ingr_POULET + Ingr_VIANDE = 100
ProteinRequirement: 0.1 Ingr_POULET + 0.2 Ingr_VIANDE >= 8
fibresRequirement: 0.001 Ingr_POULET + 0.005 Ingr_VIANDE <= 2
saltRequirement: 0.002 Ingr_POULET + 0.005 Ingr_VIANDE <= 0.4
End
