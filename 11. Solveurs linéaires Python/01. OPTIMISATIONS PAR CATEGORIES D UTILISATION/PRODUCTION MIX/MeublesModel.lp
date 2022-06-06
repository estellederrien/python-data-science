\* MaximiserProfit *\
Maximize
MaximiserBenefice: 12 produits__arc + 8 produits__automobile
 + 12 produits__cycle1 + 14 produits__cycle2 + 16 produits__dragon
 + 9 produits__nounours + 13 produits__poupee
Subject To
MaxAcier: 5 produits__arc + produits__automobile + 2 produits__cycle1
 + 3 produits__cycle2 + 3 produits__dragon + 2 produits__nounours
 + 2 produits__poupee <= 124
MaxBois: produits__arc + produits__automobile + produits__cycle1
 + 2 produits__cycle2 + 2 produits__dragon + produits__nounours
 + 5 produits__poupee <= 117
MaxPlastique: 2 produits__arc + 2 produits__automobile + 4 produits__cycle1
 + 5 produits__cycle2 + 7 produits__dragon + produits__nounours
 + 4 produits__poupee <= 142
min_production_units_for_product_arc: produits__arc >= 5
min_production_units_for_product_automobile: produits__automobile >= 5
min_production_units_for_product_cycle1: produits__cycle1 >= 5
min_production_units_for_product_cycle2: produits__cycle2 >= 5
min_production_units_for_product_dragon: produits__dragon >= 5
min_production_units_for_product_nounours: produits__nounours >= 5
min_production_units_for_product_poupee: produits__poupee >= 5
End
