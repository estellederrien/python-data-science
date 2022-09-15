\* Probleme_alimentaire *\
Minimize
Cout_total_des_ingrédients_par_boite_de_conserve_de_1kg: 10 Ingr_FARINE
 + 30.5 Ingr_MAIS + 90 Ingr_SOJA
Subject To
calciumRequirementMax: 0.38 Ingr_FARINE + 0.001 Ingr_MAIS + 0.002 Ingr_SOJA
 <= 12
calciumRequirementMin: 0.38 Ingr_FARINE + 0.001 Ingr_MAIS + 0.002 Ingr_SOJA
 >= 8
conservation: Ingr_FARINE + Ingr_MAIS + Ingr_SOJA = 1000
fiberRequirementMax: 0.02 Ingr_MAIS + 0.08 Ingr_SOJA <= 50
max_stock__for_product_FARINE: Ingr_FARINE <= 1000
max_stock__for_product_MAIS: Ingr_MAIS <= 500
max_stock__for_product_SOJA: Ingr_SOJA <= 1000
proteinRequirementMin: 0.09 Ingr_MAIS + 0.5 Ingr_SOJA >= 220
End
