\* lp *\
Minimize
Cout: 1.025 brut1Enlitres + 1.03 brut2Enlitres + 1.075 brut3Enlitres
Subject To
CoutTransportMaxiEnEuros: 0.1 brut1Enlitres + 0.09 brut2Enlitres
 + 0.03 brut3Enlitres <= 65
Litres: brut1Enlitres + brut2Enlitres + brut3Enlitres = 1000
commandex1MinimaleEnLitres1: brut1Enlitres >= 100
commandex2MinimaleEnLitres2: brut2Enlitres >= 100
commandex3MinimaleEnLitres3: brut2Enlitres >= 100
disponibiliteFournisseur1: brut1Enlitres <= 450
disponibiliteFournisseur2: brut2Enlitres <= 500
disponibiliteFournisseur3: brut3Enlitres <= 1000
End
