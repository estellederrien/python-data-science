\* Fixed_Charge *\
Minimize
OBJ: 4 Xf1d1 + 5 Xf1d2 + 5 Xf1d3 + 4 Xf1d4 + 4 Xf1d5 + 4.2 Xf1d6 + 3.3 Xf1d7
 + 5 Xf1d8 + 2.5 Xf2_d1 + 3.5 Xf2_d2 + 4.5 Xf2_d3 + 3 Xf2_d4 + 2.2 Xf2_d5
 + 4 Xf2_d6 + 2.6 Xf2_d7 + 5 Xf2_d8 + 2 Xf3d1 + 4 Xf3d2 + 5 Xf3d3 + 2.5 Xf3d4
 + 2.6 Xf3d5 + 3.8 Xf3d6 + 2.9 Xf3d7 + 5.5 Xf3d8 + 5000000 Y_f1
 + 4000000 Y_f2_ + 5500000 Y_f3
Subject To
_C1: Xf1d1 + Xf1d2 + Xf1d3 + Xf1d4 + Xf1d5 + Xf1d6 + Xf1d7 + Xf1d8
 - 1000000 Y_f1 <= 0
_C10: Xf1d7 + Xf2_d7 + Xf3d7 >= 250000
_C11: Xf1d8 + Xf2_d8 + Xf3d8 >= 250000
_C2: Xf2_d1 + Xf2_d2 + Xf2_d3 + Xf2_d4 + Xf2_d5 + Xf2_d6 + Xf2_d7 + Xf2_d8
 - 800000 Y_f2_ <= 0
_C3: Xf3d1 + Xf3d2 + Xf3d3 + Xf3d4 + Xf3d5 + Xf3d6 + Xf3d7 + Xf3d8
 - 1250000 Y_f3 <= 0
_C4: Xf1d1 + Xf2_d1 + Xf3d1 >= 200000
_C5: Xf1d2 + Xf2_d2 + Xf3d2 >= 200000
_C6: Xf1d3 + Xf2_d3 + Xf3d3 >= 200000
_C7: Xf1d4 + Xf2_d4 + Xf3d4 >= 200000
_C8: Xf1d5 + Xf2_d5 + Xf3d5 >= 250000
_C9: Xf1d6 + Xf2_d6 + Xf3d6 >= 250000
Binaries
Y_f1
Y_f2_
Y_f3
End
