\* Minimum_Cost_Flow_Problem_Sample *\
Minimize
Total_Cost_of_Transport: 2 Route_(1,_2) + 2 Route_(1,_3) + Route_(2,_3)
 + 3 Route_(2,_4) + Route_(3,_4)
Subject To
Flow_Conservation_in_Node_1: - Route_(1,_2) - Route_(1,_3) >= -4
Flow_Conservation_in_Node_2: Route_(1,_2) - Route_(2,_3) - Route_(2,_4) >= 0
Flow_Conservation_in_Node_3: Route_(1,_3) + Route_(2,_3) - Route_(3,_4) >= 0
Flow_Conservation_in_Node_4: Route_(2,_4) + Route_(3,_4) >= 4
Bounds
0 <= Route_(1,_2) <= 4
0 <= Route_(1,_3) <= 2
0 <= Route_(2,_3) <= 2
0 <= Route_(2,_4) <= 3
0 <= Route_(3,_4) <= 5
Generals
Route_(1,_2)
Route_(1,_3)
Route_(2,_3)
Route_(2,_4)
Route_(3,_4)
End
