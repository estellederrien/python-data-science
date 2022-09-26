\* Probleme_essence *\
Minimize
Cout_total_des_ingrédients_par_litre_essence_SP95:
 21.7 Fournisseurs_FOURNISSEUR1 + 20.5 Fournisseurs_FOURNISSEUR2
 + 21.5 Fournisseurs_FOURNISSEUR3
Subject To
alcaneRequirementMin: 0.25 Fournisseurs_FOURNISSEUR1
 + 0.26 Fournisseurs_FOURNISSEUR2 + 0.27 Fournisseurs_FOURNISSEUR3 >= 0.25
conservation: Fournisseurs_FOURNISSEUR1 + Fournisseurs_FOURNISSEUR2
 + Fournisseurs_FOURNISSEUR3 = 1
ethanolRequirementMin: 0.075 Fournisseurs_FOURNISSEUR1
 + 0.03 Fournisseurs_FOURNISSEUR2 + 0.15 Fournisseurs_FOURNISSEUR3 = 0.075
End
