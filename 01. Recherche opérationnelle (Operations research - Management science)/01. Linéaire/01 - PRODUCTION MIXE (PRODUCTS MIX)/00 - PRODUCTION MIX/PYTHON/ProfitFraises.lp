\* MaximiserProfit *\
Maximize
MaximiserProfit: 300 elements_fraiseA + 200 elements_fraiseB
Subject To
MaximumUtilisationAcier: elements_fraiseA + 2 elements_fraiseB <= 20
MaximumUtilisationCarburant: 2 elements_fraiseA + elements_fraiseB <= 22
MaximumUtilisationDiamant: elements_fraiseA + elements_fraiseB <= 12
MinProdFraiseA: elements_fraiseA >= 0
MinProdFraiseB: elements_fraiseB >= 0
End
