\* The_Whiskas_Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.12 Ingr_BEEF + 0.15 Ingr_CHICKEN
 + 0.17 Ingr_MUTTON + 0.12 Ingr_RICE
Subject To
FatRequirement: 0.14 Ingr_BEEF + 0.1 Ingr_CHICKEN + 0.13 Ingr_MUTTON
 + 0.16 Ingr_RICE >= 6
PercentagesSum: Ingr_BEEF + Ingr_CHICKEN + Ingr_MUTTON + Ingr_RICE = 100
ProteinRequirement: 0.13 Ingr_BEEF + 0.17 Ingr_CHICKEN + 0.16 Ingr_MUTTON
 + 0.8 Ingr_RICE >= 8
End
