\* lp *\
Minimize
Cout: 1.025 brut1Enlitres + 1.04 brut2Enlitres + 1.075 brut3Enlitres
Subject To
CoutTransportEnEuros: 0.1 brut1Enlitres + 0.08 brut2Enlitres
 + 0.03 brut3Enlitres <= 70
Litres: brut1Enlitres + brut2Enlitres + brut3Enlitres = 1000
commandex1MinimaleEnLitres: brut1Enlitres >= 100
commandex2MinimaleEnLitres: brut2Enlitres >= 100
commandex3MinimaleEnLitres: brut2Enlitres >= 100
disponibiliteFournisseur1: brut1Enlitres <= 500
disponibiliteFournisseur2: brut2Enlitres <= 500
disponibiliteFournisseur3: brut3Enlitres <= 1000
End
