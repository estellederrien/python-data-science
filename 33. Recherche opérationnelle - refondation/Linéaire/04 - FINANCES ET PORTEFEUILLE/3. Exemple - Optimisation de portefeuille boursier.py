""" 
** Problème d'optimisation financière 3 .


Il s'agit d'un problème d'optimisation linéaire du risque et du rendement d'un portefeuille. 
Notre objectif est de minimiser le risque du portefeuille tout en satisfaisant simultanément 5 contraintes:

1. La somme des investissements sera de 100 000 $

2. Le portefeuille a un rendement annuel d'au moins 7,5%

3. Au moins 50% des placements sont notés A

4. Au moins 40% des investissements sont immédiatement liquides

5. Les comptes d'épargne et les certificats de dépôt ne dépassent pas 30 000 dollars.

** Source : 
https://towardsdatascience.com/portfolio-linear-optimization-breakdown-f519546ed1ff

https://github.com/ahershy/Linear-Optimization-Portfolio/blob/master/Optimize%20Portfolio.ipynb


** Modélisation du LP :

Pour revoir le processus de résolution d'un problème d'optimisation linéaire, il y a 3 étapes:

1. Variables de décision: ici, il y a 8 variables de décision. Ce sont nos options d'investissement.
    
2. Objectif Fonction: Nous voulons minimiser le risque pour les 8 investissements. 
Voici les placements multipliés par leurs coefficients de risque respectifs.
0X1 + 0X2 + 25X3 + 30X4 + 20X5 + 15X6 + 65X7 + 40X8

3. Contraintes: Enfin, nous voulons définir exactement quelles sont nos contraintes. 
Celles-ci sont exprimées algébriquement ci-dessous dans le même ordre que nous avons énuméré les contraintes précédemment:

1. ΣXi = 100000
2. .04X1+.052X2+.071X3+.1X4+.82X5+.065X6+.2X7+.125X8 >= 7500
3. X1 + X2 + X5 + X7 >= 40000
4. X1 + X3 + X4 + X7 + X8 >= 40000
5. X1 + X2 <= 30000

Au cas où vous seriez confus au sujet des «7 500» de la contrainte n ° 2, ce serait le rendement annuel de 7,5% que nous recherchons multiplié par notre investissement de 100 000 $.


 """

from pulp import *
import pandas as pd
df = pd.read_excel(r"datasets\Fin_optimization.xls")
print(df)

""" 
Joli look. Cependant, quelques modifications de mise en forme doivent être apportées pour avancer.

    Transformez les colonnes «Liquidité» et «Notes» en valeurs binaires. Ceci concerne les contraintes 3 et 4. 
    Les valeurs de chaîne pertinentes dans ces colonnes sont «Immédiat» pour la liquidité et «A» pour la notation. 
    Distinguer ces valeurs de chaîne des autres est nécessaire pour un calcul ultérieur.
    Créez une nouvelle colonne binaire pour le type d'investissement. 
    La contrainte n ° 5 se concentre sur les types d'investissement d'épargne et de CD, 
    donc les distinguer des autres types d'investissement aidera plus tard.
    Créez une colonne de tous les 1 pour Amt_invested. 
    Cela sera utile pour la contrainte n ° 1: la contrainte de portefeuille total de 100 000 $.
 """


#1's and 0's
df['Liquidity'] = (df['Liquidity']=='Immediate')
df['Liquidity'] = df['Liquidity'].astype(int)

#1's and 0's
df['Rating'] = (df['Rating']=='A')
df['Rating']= df['Rating'].astype(int)

#1's and 0's
savecd = [1,1,0,0,0,0,0,0]
df['Saving&CD'] = savecd

#1's and 0's
amt_invested = [1]*8
df['Amt_Invested'] = amt_invested
df
print(df)

"""   Designation       Potential Investment  Expected Return  Rating  Risk  Liquidity  Saving&CD  Amt_Invested
0          X1             Saving Account            0.040       1     0          1          1             1
1          X2     Certificate of deposit            0.052       1     0          0          1             1
2          X3         Atlantic Lightning            0.071       0    25          1          0             1
3          X4              Arkansas REIT            0.100       0    30          1          0             1
4          X5  Bedrock Insurance Annuity            0.082       1    20          0          0             1
5          X6          Nocal Mining Bond            0.065       0    15          0          0             1
6          X7           Minocompo System            0.200       1    65          1          0             1
7          X8              Antony Hotels            0.125       0    40          1          0             1 """

prob = LpProblem("Portfolio_Opt",LpMinimize)

# Create a list of the inventment items
inv_items = list(df['Potential Investment'])

# Create a dictinary of risks for all inv items
risks = dict(zip(inv_items,df['Risk']))

# Create a dictionary of returns for all inv items
returns = dict(zip(inv_items,df['Expected Return']))

#Create dictionary for ratings of inv items
ratings = dict(zip(inv_items,df['Rating']))

# Create a dictionary for liquidity for all inv items
liquidity = dict(zip(inv_items,df['Liquidity']))

#Create a dictionary for savecd for inve items
savecd = dict(zip(inv_items,df['Saving&CD']))

#Create a dictionary for amt as being all 1's
amt = dict(zip(inv_items,df['Amt_Invested']))



print(risks)

""" Ensuite, nous définissons nos variables de décision comme des investissements et y ajoutons quelques paramètres,

    Nom: pour étiqueter nos variables de décision
    Lowbound = 0: pour s'assurer qu'il n'y a pas d'argent négatif dans notre solution
    Continu: parce que nous avons affaire à des cents pour un dollar. 
"""
inv_vars = LpVariable.dicts("Potential Investment",inv_items,lowBound=0,cat='Continuous')

""" Enfin, nous ajoutons la variable de décision modifiée à notre variable 
de problème que nous avons créée précédemment et nous entrons en outre
 les contraintes. Nous parcourons les dictionnaires en utilisant 
 des «boucles for» pour chaque élément d'investissement. """

# Fonction objectif à minimiser : ON veut minimiser les risques
prob += lpSum([risks[i]*inv_vars[i] for i in inv_items])

# amt
prob += lpSum([amt[f] * inv_vars[f] for f in inv_items]) == 100000, "Investments"
prob += lpSum([returns[f] * inv_vars[f] for f in inv_items]) >= 7500, "Returns"
prob += lpSum([ratings[f] * inv_vars[f] for f in inv_items]) >= 50000, "Ratings"
prob += lpSum([liquidity[f] * inv_vars[f] for f in inv_items]) >= 40000, "Liquidity"
prob += lpSum([savecd[f] * inv_vars[f] for f in inv_items]) <= 30000, "Save and CD"
print(prob)


prob.writeLP("Portfolio_Opt.lp")


prob.solve()


print("Le portefeuille de qualité optimum est \n"+"-"*110)
for v in prob.variables():
        if v.varValue>0:
            print(v.name, "=", v.varValue)

""" Le portefeuille de qualité optimum sous contrainte de risques est
--------------------------------------------------------------------------------------------------------------
Potential_Investment_Arkansas_REIT = 22666.667
Potential_Investment_Bedrock_Insurance_Annuity = 47333.333
Potential_Investment_Certificate_of_deposit = 12666.667
Potential_Investment_Saving_Account = 17333.333 """