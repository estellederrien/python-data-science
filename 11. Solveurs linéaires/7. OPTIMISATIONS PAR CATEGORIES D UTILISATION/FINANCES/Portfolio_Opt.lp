\* Portfolio_Opt *\
Maximize
OBJ: 0.18 Maximisation_de_profit_bitcoin
 + 0.18 Maximisation_de_profit_euthereum
 + 0.35 Maximisation_de_profit_litecoin + 0.16 Maximisation_de_profit_ripple
Subject To
budget: Maximisation_de_profit_bitcoin + Maximisation_de_profit_euthereum
 + Maximisation_de_profit_litecoin + Maximisation_de_profit_ripple = 100
fiability: 0.09 Maximisation_de_profit_bitcoin
 + 0.05 Maximisation_de_profit_euthereum
 + 0.08 Maximisation_de_profit_litecoin + 0.13 Maximisation_de_profit_ripple
 >= 9
Bounds
10 <= Maximisation_de_profit_bitcoin
8 <= Maximisation_de_profit_euthereum
10 <= Maximisation_de_profit_litecoin
5 <= Maximisation_de_profit_ripple
End
