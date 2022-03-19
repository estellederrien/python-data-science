\* Probleme_de_transport_acier *\
Minimize
Coût_total_du_transport: 0.4 Route_('Lille',_'Lorient')
 + 0.35 Route_('Lille',_'Rennes') + 0.45 Route_('Lille',_'Strasbourg')
 + 0.45 Route_('Lille',_'Toulouse') + 0.6 Route_('Lorient',_'Bruxelles')
 + 0.12 Route_('Lorient',_'Toulouse') + 0.375 Route_('Paris',_'Lorient')
 + 0.5 Route_('Paris',_'Nice') + 0.35 Route_('Paris',_'Rennes')
 + 0.45 Route_('Paris',_'Strasbourg') + 0.55 Route_('Rennes',_'Bordeaux')
 + 0.35 Route_('Rennes',_'Nice') + 0.375 Route_('Strasbourg',_'Bordeaux')
 + 0.65 Route_('Strasbourg',_'Bruxelles')
Subject To
Conservation_du_flot_d'acier_dans_le_nœud_Bordeaux:
 Route_('Rennes',_'Bordeaux') + Route_('Strasbourg',_'Bordeaux') >= 7000
Conservation_du_flot_d'acier_dans_le_nœud_Bruxelles:
 Route_('Lorient',_'Bruxelles') + Route_('Strasbourg',_'Bruxelles') >= 4000
Conservation_du_flot_d'acier_dans_le_nœud_Lille: - Route_('Lille',_'Lorient')
 - Route_('Lille',_'Rennes') - Route_('Lille',_'Strasbourg')
 - Route_('Lille',_'Toulouse') >= -15000
Conservation_du_flot_d'acier_dans_le_nœud_Lorient: Route_('Lille',_'Lorient')
 - Route_('Lorient',_'Bruxelles') - Route_('Lorient',_'Toulouse')
 + Route_('Paris',_'Lorient') >= 0
Conservation_du_flot_d'acier_dans_le_nœud_Nice: Route_('Paris',_'Nice')
 + Route_('Rennes',_'Nice') >= 3000
Conservation_du_flot_d'acier_dans_le_nœud_Paris: - Route_('Paris',_'Lorient')
 - Route_('Paris',_'Nice') - Route_('Paris',_'Rennes')
 - Route_('Paris',_'Strasbourg') >= -10000
Conservation_du_flot_d'acier_dans_le_nœud_Rennes: Route_('Lille',_'Rennes')
 + Route_('Paris',_'Rennes') - Route_('Rennes',_'Bordeaux')
 - Route_('Rennes',_'Nice') >= 0
Conservation_du_flot_d'acier_dans_le_nœud_Strasbourg:
 Route_('Lille',_'Strasbourg') + Route_('Paris',_'Strasbourg')
 - Route_('Strasbourg',_'Bordeaux') - Route_('Strasbourg',_'Bruxelles') >= 0
Conservation_du_flot_d'acier_dans_le_nœud_Toulouse:
 Route_('Lille',_'Toulouse') + Route_('Lorient',_'Toulouse') >= 6000
Bounds
0 <= Route_('Lille',_'Lorient') <= 4000
0 <= Route_('Lille',_'Rennes') <= 2000
2000 <= Route_('Lille',_'Strasbourg') <= 3000
0 <= Route_('Lille',_'Toulouse') <= 2000
0 <= Route_('Lorient',_'Bruxelles') <= 2000
0 <= Route_('Lorient',_'Toulouse') <= 4000
0 <= Route_('Paris',_'Lorient') <= 5000
0 <= Route_('Paris',_'Nice') <= 1000
0 <= Route_('Paris',_'Rennes') <= 3000
1000 <= Route_('Paris',_'Strasbourg') <= 5000
0 <= Route_('Rennes',_'Bordeaux') <= 6000
1000 <= Route_('Rennes',_'Nice') <= 5000
0 <= Route_('Strasbourg',_'Bordeaux') <= 4000
0 <= Route_('Strasbourg',_'Bruxelles') <= 4000
Generals
Route_('Lille',_'Lorient')
Route_('Lille',_'Rennes')
Route_('Lille',_'Strasbourg')
Route_('Lille',_'Toulouse')
Route_('Lorient',_'Bruxelles')
Route_('Lorient',_'Toulouse')
Route_('Paris',_'Lorient')
Route_('Paris',_'Nice')
Route_('Paris',_'Rennes')
Route_('Paris',_'Strasbourg')
Route_('Rennes',_'Bordeaux')
Route_('Rennes',_'Nice')
Route_('Strasbourg',_'Bordeaux')
Route_('Strasbourg',_'Bruxelles')
End
