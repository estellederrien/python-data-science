\* Elements_Concentration_Problem *\
Maximize
Total_Utilization_is_maximized: Util_CONC_1 + Util_CONC_2 + Util_CONC_3
Subject To
IronPercent: 0.571428571429 Util_CONC_1 + 0.285714285714 Util_CONC_2
 + 0.714285714286 Util_CONC_3 <= 0.35
MercuryPercent: 0.882352941176 Util_CONC_1 + 1.05882352941 Util_CONC_2
 + 0.705882352941 Util_CONC_3 <= 0.17
SilverPercent: 1.07142857143 Util_CONC_1 + 1.42857142857 Util_CONC_2
 + 0.714285714286 Util_CONC_3 <= 0.28
Bounds
Util_CONC_1 <= 1
Util_CONC_2 <= 1
Util_CONC_3 <= 1
End
