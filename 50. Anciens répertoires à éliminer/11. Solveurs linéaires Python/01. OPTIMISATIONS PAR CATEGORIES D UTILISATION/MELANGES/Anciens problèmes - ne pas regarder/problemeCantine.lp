\* Je_minimise *\
Minimize
OBJ: 0.45 aliment_Bananes + 0.48 aliment_Broccolis + 0.81 aliment_Bœuf
 + 0.09 aliment_Cookie_au_chocoloat + 0.27 aliment_Cookie_poire
 + 0.18 aliment_Haricots + 0.45 aliment_Jambon + 0.06 aliment_Laitue_Iceberg
 + 0.04 aliment_Mais + 0.15 aliment_Pain_blanc + 0.18 aliment_Pain_complet
 + 0.72 aliment_Pommes + 2.52 aliment_Poulet_grillé
 + 2.34 aliment_Spaghettis_en_sauce + 0.48 aliment_Tarte_aux_pommes
 + 0.93 aliment_Tofu + 0.33 aliment_Œufs_pochés
Subject To
_C1: 104.9 aliment_Bananes + 73.8 aliment_Broccolis + 141.8 aliment_Bœuf
 + 78.1 aliment_Cookie_au_chocoloat + 81 aliment_Cookie_poire
 + 171.5 aliment_Haricots + 56.4 aliment_Jambon + 2.6 aliment_Laitue_Iceberg
 + 72.2 aliment_Mais + 65 aliment_Pain_blanc + 65 aliment_Pain_complet
 + 81.4 aliment_Pommes + 277.4 aliment_Poulet_grillé
 + 358.2 aliment_Spaghettis_en_sauce + 67.2 aliment_Tarte_aux_pommes
 + 88.2 aliment_Tofu + 99.6 aliment_Œufs_pochés >= 800
_C10: - 100000 Legume_(bool)_Haricots + aliment_Haricots <= 0
_C11: - 0.1 Legume_(bool)_Tofu + aliment_Tofu >= 0
_C12: - 100000 Legume_(bool)_Tofu + aliment_Tofu <= 0
_C13: - 0.1 Legume_(bool)_Poulet_grillé + aliment_Poulet_grillé >= 0
_C14: - 100000 Legume_(bool)_Poulet_grillé + aliment_Poulet_grillé <= 0
_C15: - 0.1 Legume_(bool)_Spaghettis_en_sauce + aliment_Spaghettis_en_sauce
 >= 0
_C16: - 100000 Legume_(bool)_Spaghettis_en_sauce + aliment_Spaghettis_en_sauce
 <= 0
_C17: - 0.1 Legume_(bool)_Pommes + aliment_Pommes >= 0
_C18: - 100000 Legume_(bool)_Pommes + aliment_Pommes <= 0
_C19: - 0.1 Legume_(bool)_Bananes + aliment_Bananes >= 0
_C2: 104.9 aliment_Bananes + 73.8 aliment_Broccolis + 141.8 aliment_Bœuf
 + 78.1 aliment_Cookie_au_chocoloat + 81 aliment_Cookie_poire
 + 171.5 aliment_Haricots + 56.4 aliment_Jambon + 2.6 aliment_Laitue_Iceberg
 + 72.2 aliment_Mais + 65 aliment_Pain_blanc + 65 aliment_Pain_complet
 + 81.4 aliment_Pommes + 277.4 aliment_Poulet_grillé
 + 358.2 aliment_Spaghettis_en_sauce + 67.2 aliment_Tarte_aux_pommes
 + 88.2 aliment_Tofu + 99.6 aliment_Œufs_pochés <= 2500
_C20: - 100000 Legume_(bool)_Bananes + aliment_Bananes <= 0
_C21: - 0.1 Legume_(bool)_Pain_blanc + aliment_Pain_blanc >= 0
_C22: - 100000 Legume_(bool)_Pain_blanc + aliment_Pain_blanc <= 0
_C23: - 0.1 Legume_(bool)_Pain_complet + aliment_Pain_complet >= 0
_C24: - 100000 Legume_(bool)_Pain_complet + aliment_Pain_complet <= 0
_C25: - 0.1 Legume_(bool)_Cookie_poire + aliment_Cookie_poire >= 0
_C26: - 100000 Legume_(bool)_Cookie_poire + aliment_Cookie_poire <= 0
_C27: - 0.1 Legume_(bool)_Tarte_aux_pommes + aliment_Tarte_aux_pommes >= 0
_C28: - 100000 Legume_(bool)_Tarte_aux_pommes + aliment_Tarte_aux_pommes <= 0
_C29: - 0.1 Legume_(bool)_Œufs_pochés + aliment_Œufs_pochés >= 0
_C3: - 0.1 Legume_(bool)_Broccolis + aliment_Broccolis >= 0
_C30: - 100000 Legume_(bool)_Œufs_pochés + aliment_Œufs_pochés <= 0
_C31: - 0.1 Legume_(bool)_Jambon + aliment_Jambon >= 0
_C32: - 100000 Legume_(bool)_Jambon + aliment_Jambon <= 0
_C33: - 0.1 Legume_(bool)_Bœuf + aliment_Bœuf >= 0
_C34: - 100000 Legume_(bool)_Bœuf + aliment_Bœuf <= 0
_C35: - 0.1 Legume_(bool)_Cookie_au_chocoloat + aliment_Cookie_au_chocoloat
 >= 0
_C36: - 100000 Legume_(bool)_Cookie_au_chocoloat + aliment_Cookie_au_chocoloat
 <= 0
_C37: Legume_(bool)_Haricots + Legume_(bool)_Mais >= 2
_C4: - 100000 Legume_(bool)_Broccolis + aliment_Broccolis <= 0
_C5: - 0.1 Legume_(bool)_Mais + aliment_Mais >= 0
_C6: - 100000 Legume_(bool)_Mais + aliment_Mais <= 0
_C7: - 0.1 Legume_(bool)_Laitue_Iceberg + aliment_Laitue_Iceberg >= 0
_C8: - 100000 Legume_(bool)_Laitue_Iceberg + aliment_Laitue_Iceberg <= 0
_C9: - 0.1 Legume_(bool)_Haricots + aliment_Haricots >= 0
carbohydratesMaximum: 26.7 aliment_Bananes + 13.6 aliment_Broccolis
 + 0.8 aliment_Bœuf + 9.3 aliment_Cookie_au_chocoloat
 + 12.4 aliment_Cookie_poire + 39.9 aliment_Haricots + 0.3 aliment_Jambon
 + 0.4 aliment_Laitue_Iceberg + 17.1 aliment_Mais + 12.4 aliment_Pain_blanc
 + 11.8 aliment_Pain_complet + 21 aliment_Pommes
 + 58.3 aliment_Spaghettis_en_sauce + 9.6 aliment_Tarte_aux_pommes
 + 2.2 aliment_Tofu + 1.3 aliment_Œufs_pochés <= 200
carbohydratesMinimum: 26.7 aliment_Bananes + 13.6 aliment_Broccolis
 + 0.8 aliment_Bœuf + 9.3 aliment_Cookie_au_chocoloat
 + 12.4 aliment_Cookie_poire + 39.9 aliment_Haricots + 0.3 aliment_Jambon
 + 0.4 aliment_Laitue_Iceberg + 17.1 aliment_Mais + 12.4 aliment_Pain_blanc
 + 11.8 aliment_Pain_complet + 21 aliment_Pommes
 + 58.3 aliment_Spaghettis_en_sauce + 9.6 aliment_Tarte_aux_pommes
 + 2.2 aliment_Tofu + 1.3 aliment_Œufs_pochés >= 130
fibresMaximum: 2.7 aliment_Bananes + 8.5 aliment_Broccolis
 + 0.6 aliment_Cookie_poire + 3.2 aliment_Haricots
 + 0.3 aliment_Laitue_Iceberg + 2 aliment_Mais + 1.3 aliment_Pain_blanc
 + 1.1 aliment_Pain_complet + 3.7 aliment_Pommes
 + 11.6 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 1.4 aliment_Tofu <= 150
fibresMinimum: 2.7 aliment_Bananes + 8.5 aliment_Broccolis
 + 0.6 aliment_Cookie_poire + 3.2 aliment_Haricots
 + 0.3 aliment_Laitue_Iceberg + 2 aliment_Mais + 1.3 aliment_Pain_blanc
 + 1.1 aliment_Pain_complet + 3.7 aliment_Pommes
 + 11.6 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 1.4 aliment_Tofu >= 120
grasMaximum: 0.5 aliment_Bananes + 0.8 aliment_Broccolis + 12.8 aliment_Bœuf
 + 4.5 aliment_Cookie_au_chocoloat + 3.3 aliment_Cookie_poire
 + 0.2 aliment_Haricots + 4.3 aliment_Jambon + 0.6 aliment_Mais
 + aliment_Pain_blanc + aliment_Pain_complet + 0.5 aliment_Pommes
 + 10.8 aliment_Poulet_grillé + 12.3 aliment_Spaghettis_en_sauce
 + 3.1 aliment_Tarte_aux_pommes + 5.5 aliment_Tofu + 7.3 aliment_Œufs_pochés
 <= 80
grasMinimum: 0.5 aliment_Bananes + 0.8 aliment_Broccolis + 12.8 aliment_Bœuf
 + 4.5 aliment_Cookie_au_chocoloat + 3.3 aliment_Cookie_poire
 + 0.2 aliment_Haricots + 4.3 aliment_Jambon + 0.6 aliment_Mais
 + aliment_Pain_blanc + aliment_Pain_complet + 0.5 aliment_Pommes
 + 10.8 aliment_Poulet_grillé + 12.3 aliment_Spaghettis_en_sauce
 + 3.1 aliment_Tarte_aux_pommes + 5.5 aliment_Tofu + 7.3 aliment_Œufs_pochés
 >= 60
proteinesMaximum: 1.2 aliment_Bananes + 8 aliment_Broccolis + 5.4 aliment_Bœuf
 + 0.9 aliment_Cookie_au_chocoloat + 1.1 aliment_Cookie_poire
 + 3.7 aliment_Haricots + 3.9 aliment_Jambon + 0.2 aliment_Laitue_Iceberg
 + 2.5 aliment_Mais + 2.2 aliment_Pain_blanc + 2.3 aliment_Pain_complet
 + 0.3 aliment_Pommes + 42.2 aliment_Poulet_grillé
 + 8.2 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 9.4 aliment_Tofu + 6.7 aliment_Œufs_pochés <= 150
proteinesMinimum: 1.2 aliment_Bananes + 8 aliment_Broccolis + 5.4 aliment_Bœuf
 + 0.9 aliment_Cookie_au_chocoloat + 1.1 aliment_Cookie_poire
 + 3.7 aliment_Haricots + 3.9 aliment_Jambon + 0.2 aliment_Laitue_Iceberg
 + 2.5 aliment_Mais + 2.2 aliment_Pain_blanc + 2.3 aliment_Pain_complet
 + 0.3 aliment_Pommes + 42.2 aliment_Poulet_grillé
 + 8.2 aliment_Spaghettis_en_sauce + 0.5 aliment_Tarte_aux_pommes
 + 9.4 aliment_Tofu + 6.7 aliment_Œufs_pochés >= 80
Bounds
0 <= aliment_Bananes
0 <= aliment_Broccolis
0 <= aliment_Bœuf
0 <= aliment_Cookie_au_chocoloat
0 <= aliment_Cookie_poire
0 <= aliment_Haricots
0 <= aliment_Jambon
0 <= aliment_Laitue_Iceberg
0 <= aliment_Mais
0 <= aliment_Pain_blanc
0 <= aliment_Pain_complet
0 <= aliment_Pommes
0 <= aliment_Poulet_grillé
0 <= aliment_Spaghettis_en_sauce
0 <= aliment_Tarte_aux_pommes
0 <= aliment_Tofu
0 <= aliment_Œufs_pochés
Generals
aliment_Bananes
aliment_Broccolis
aliment_Bœuf
aliment_Cookie_au_chocoloat
aliment_Cookie_poire
aliment_Haricots
aliment_Jambon
aliment_Laitue_Iceberg
aliment_Mais
aliment_Pain_blanc
aliment_Pain_complet
aliment_Pommes
aliment_Poulet_grillé
aliment_Spaghettis_en_sauce
aliment_Tarte_aux_pommes
aliment_Tofu
aliment_Œufs_pochés
Binaries
Legume_(bool)_Bananes
Legume_(bool)_Broccolis
Legume_(bool)_Bœuf
Legume_(bool)_Cookie_au_chocoloat
Legume_(bool)_Cookie_poire
Legume_(bool)_Haricots
Legume_(bool)_Jambon
Legume_(bool)_Laitue_Iceberg
Legume_(bool)_Mais
Legume_(bool)_Pain_blanc
Legume_(bool)_Pain_complet
Legume_(bool)_Pommes
Legume_(bool)_Poulet_grillé
Legume_(bool)_Spaghettis_en_sauce
Legume_(bool)_Tarte_aux_pommes
Legume_(bool)_Tofu
Legume_(bool)_Œufs_pochés
End
