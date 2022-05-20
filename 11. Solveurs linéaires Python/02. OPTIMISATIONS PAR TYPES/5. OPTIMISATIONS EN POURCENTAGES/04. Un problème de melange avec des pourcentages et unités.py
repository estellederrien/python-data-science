""" 
Lien : http://yetanothermathprogrammingconsultant.blogspot.com/2020/01/small-blending-problem-in-pulp.html

Il existe différentes matières premières en acier qui doivent être mélangées (mélangées) dans un matériau final 

répondant à certaines spécifications. Dans ce cas, les spécifications sont des limites sur les éléments Carbone (C), 

Cuivre (Cu) et Manganèse (Mn). Nous supposons que les choses se mélangent linéairement.

Blending est une application de programmation linéaire traditionnelle, et les modèles se trouvent dans de 

nombreux manuels.

Le problème est petit, alors essayons PuLP ici.

Je vais essayer d'écrire un peu sur l'indexation à l'aide de chaînes (au lieu d'entiers) et 

de comparer PuLP avec CVXPY et GAMS. 

Comme le modèle est petit, j'ajouterai également quelques manipulations de données (en utilisant des blocs de données) 

et quelques rapports simples (en utilisant également des blocs de données). 

J'utilise l'indexation des chaînes dans Pulp (avec GAMS, c'est standard).


 Bien sûr, CVXPY est très différent : il est basé sur une matrice. Donc, les choses dépendent de la position. 
 
 L'idée est d'extraire des données du bloc de données de manière à ce que les positions soient prévisibles.

 Problem data

The data for the problem is as follows:

Demand: 5000 Kg

Specification of final material:

    Element      %Minimum %Max   
    Carbon       2         3     
    Copper       0.4       0.6   
    Manganese    1.2       1.65  


Raw material inventory:

Alloy          C%   Cu%   Mn%     Stocks kg Price € / kg
Iron alloy     2.50 0.00  1.30    4000      1.20
Iron alloy     3.00 0.00  0.80    3000      1.50
Iron alloy     0.00 0.30  0.00    6000      0.90
Copper alloy   0.00 90.00 0.00    5000      1.30
Copper alloy   0.00 96.00 4.00    2000      1.45
Aluminum alloy 0.00 0.40  1.20    3000      1.20
Aluminum alloy 0.00 0.60  0.00   2,500      1.00

Le modèle : 

On veut minimiser le cout : 
min∑ Costi⋅Usei

Minj ≤ ∑Elementi,j⋅Usei /  ∑iUsei ≤ Maxj

∑i Usei = Demand

0 ≤ Usei ≤ Availablei


i           Types of raw material in stock
j           Element with limits
Costi       Unit cost of raw material
Minj,Maxj   Limits on element content in final product
Elementi,j  Content of elements in raw material
Demand      Demand for final product
Availablei  Availability of raw material
Usei        Decision variable: how much raw material to use


 """


from io import StringIO
import pandas as pd
import pulp as lp

# for inputting tabular data below
def table(s):
  return pd.read_csv(StringIO(s),sep='\s+',index_col='ID')

#------------------------------------------------------------------
# data
#------------------------------------------------------------------

demand = 5000

requirements = table("""
   ID  Element      Min   Max
   C   Carbon       2     3
   Cu  Copper       0.4   0.6
   Mn  Manganese    1.2   1.65
    """)

supplyData = table("""
  ID  Alloy             C       Cu     Mn     Stock   Price
  A   "Iron alloy"      2.50    0.00   1.30   4000    1.20
  B   "Iron alloy"      3.00    0.00   0.80   3000    1.50
  C   "Iron alloy"      0.00    0.30   0.00   6000    0.90
  D   "Copper alloy"    0.00   90.00   0.00   5000    1.30
  E   "Copper alloy"    0.00   96.00   4.00   2000    1.45
  F   "Aluminum alloy"  0.00    0.40   1.20   3000    1.20
  G   "Aluminum alloy"  0.00    0.60   0.00   2500    1.00
  """)

print("----- Data-------")
print(requirements)
print(supplyData)


#------------------------------------------------------------------
# derived data
#------------------------------------------------------------------

# our sets are stockItems ["A","B",..] and elements ["C","Cu",...] 
Items = supplyData.index
Elements = requirements.index

print("----- Indices-------")
print(Items)
print(Elements)

#------------------------------------------------------------------
# LP Model
#------------------------------------------------------------------


use = lp.LpVariable.dicts("Use",Items,0,None,cat='Continuous')
content = lp.LpVariable.dicts("Content",Elements,0,None,cat='Continuous')

model = lp.LpProblem("Steel", lp.LpMinimize)

# objective : minimize cost
model += lp.lpSum([use[i]*supplyData.loc[i,'Price'] for i in Items ])

# upper bounds wrt availability
for i in Items:
  model += use[i] <= supplyData.loc[i,'Stock']

# final content of elements and their bounds  
for j in Elements:
  model += demand*content[j] == lp.lpSum([use[i]*supplyData.loc[i,j] for i in Items])
  model += content[j] >= requirements.loc[j,'Min']
  model += content[j] <= requirements.loc[j,'Max']

# meet demand
model += lp.lpSum([use[i] for i in Items]) == demand


# for debugging
#print(model)


#------------------------------------------------------------------
# Solve and reporting
#------------------------------------------------------------------

model.solve()


print("----- Model Results-------")
print("Status:", lp.LpStatus[model.status])
print("Objective:",lp.value(model.objective))


# collect results
L = []
for i in Items: 
  L.append(['use',i,0.0,use[i].varValue,supplyData.loc[i,'Stock']])
for j in Elements:
  L.append(['content',j,requirements.loc[j,'Min'],content[j].varValue,requirements.loc[j,'Max']])
results = pd.DataFrame(L,columns=['Variable','Index','Lower','Value','Upper'])
print(results)

