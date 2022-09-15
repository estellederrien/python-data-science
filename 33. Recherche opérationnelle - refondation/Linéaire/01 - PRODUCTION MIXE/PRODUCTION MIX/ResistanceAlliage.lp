\* MaximiserResistance *\
Maximize
MaximiserSolidite: elements__argent + 2 elements__cuivre + 3 elements__zinc
Subject To
MinProdObjs: elements__argent + elements__cuivre + elements__zinc = 100
MinimumConductivite: 3 elements__argent + 4 elements__cuivre + elements__zinc
 >= 250
min_production_units_for_product_argent: elements__argent >= 10
min_production_units_for_product_cuivre: elements__cuivre >= 10
min_production_units_for_product_zinc: elements__zinc >= 10
End
