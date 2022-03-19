''' https://randerson112358.medium.com/python-for-finance-portfolio-optimization-66882498847

L'optimisation de portefeuille est le processus de sélection du meilleur portefeuille 
(répartition des actifs), parmi l'ensemble de tous les portefeuilles considérés, en fonction d'un objectif. 
L'objectif maximise généralement des facteurs tels que le rendement attendu et minimise les coûts 
tels que le risque financier.
-Wikipédia

Dans cet article, je vais vous montrer comment créer un programme pour optimiser un portefeuille d'actions 
en utilisant la frontière efficace et Python ! 
Dans la théorie moderne du portefeuille, la frontière efficace est un portefeuille 
d'investissement qui occupe les parties « efficaces » du spectre risque-rendement. 
Formellement, c'est l'ensemble des portefeuilles qui satisfont à la condition qu'il n'existe 
pas d'autre portefeuille avec un rendement attendu supérieur mais avec le même écart-type de rendement.

Le Ratio de Sharpe va plus loin : il vous aide en fait à trouver la meilleure proportion possible de ces actions à utiliser, dans un portefeuille.
- Moneychimp

Le ratio de Sharpe a été développé par William F. Sharpe en 1966. 
Le ratio décrit le rendement excédentaire que vous recevez pour la volatilité supplémentaire que vous endurez 
pour détenir un actif plus risqué. 
Il mesure la performance d'un investissement par rapport à un actif sans risque 
(obligations, bons du Trésor…), après ajustement de son risque. 
Il est défini comme la différence entre les rendements de l'investissement et le rendement sans risque, 
divisé par l'écart-type de l'investissement.
-Investopedia

Alors, qu'est-ce qui est considéré comme un bon ratio de Sharpe qui indique un degré élevé de rendement attendu 
pour un niveau de risque relativement faible ?

Habituellement, tout ratio de Sharpe supérieur à 1,0 est considéré comme acceptable à bon par les investisseurs. 
Un ratio supérieur à 2,0 est considéré comme très bon. Un ratio de 3,0 ou plus est considéré comme excellent. 
Un ratio inférieur à 1,0 est considéré comme sous-optimal.

Si vous préférez ne pas lire cet article et souhaitez une représentation vidéo de celui-ci, 
vous pouvez consulter la vidéo YouTube . 
Il passe en revue tout dans cet article avec un peu plus de détails et vous aidera à commencer facilement à programmer 
même si le langage de programmation Python n'est pas installé sur votre ordinateur. 
Ou vous pouvez utiliser les deux comme matériel supplémentaire pour l'apprentissage !


La programmation:

La première chose que j'aime faire avant d'écrire une seule ligne de code est de mettre une description dans 
les commentaires de ce que fait le code. De cette façon, je peux regarder en arrière sur mon code et savoir 
exactement ce qu'il fait. '''


# Description : Ce programme tente d'optimiser un portefeuille d'utilisateurs en utilisant Efficient Frontier & Python.

## Import the python libraries
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Créer le portefeuille fictif

''' Obtenez les symboles boursiers/tickers pour le portefeuille fictif. 
Je vais utiliser les cinq sociétés technologiques américaines les plus populaires 
et les plus performantes connues sous le nom de FAANG, qui est un acronyme pour Facebook, Amazon, Apple, 
Netflix et Alphabet (anciennement Google). '''

assets =  ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

''' Ensuite, j'attribuerai des pondérations équivalentes à chaque action au sein du portefeuille, 
ce qui signifie que 20% de ce portefeuille aura des actions dans Facebook (FB), 20% dans Amazon (AMZN), 
20% dans Apple (AAPL), 20% dans Netflix (NFLX ) et 20 % dans Google (GOOG).

Cela signifie que si j'avais un total de 100 USD dans le portefeuille, 
j'aurais alors 20 USD dans chaque action. '''

# Attribuez des poids aux actions. Les poids doivent = 1 donc 0,2 pour chacun
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
weights

# Maintenant, je vais obtenir la date de début des stocks qui sera le 1er janvier 2013 
# et la date de fin qui sera la date du jour (aujourd'hui).

#Obtenir la date de début de stock
stockStartDate = '2021-01-01'
# Get the stocks ending date aka todays date and format it in the form YYYY-MM-DD
today = datetime.today().strftime('%Y-%m-%d')

# Il est temps de créer la trame de données qui contiendra le prix de clôture ajusté des actions.

#Créez une base de données pour stocker le prix de clôture ajusté des actions
df = pd.DataFrame()

#Stocker le prix de clôture ajusté du stock dans le bloc de données
for stock in assets:
    df[stock] = web.DataReader(stock,data_source='yahoo',start=stockStartDate , end=today)['Adj Close']

#Affichez le bloc de données et le prix de clôture ajusté de chaque action.
print(df)

# Create the title 'Portfolio Adj Close Price History
title = 'Portfolio Adj. Close Price History    '

# Afficher visuellement les cours des actions.

#Get the stocks
my_stocks = df

#Create and plot the graph
plt.figure(figsize=(12.2,4.5)) 

#width = 12.2in, height = 4.5# Loop through each stock and plot the Adj Close for each day
for c in my_stocks.columns.values:
  plt.plot( my_stocks[c],  label=c)
  
#plt.plot( X-Axis , Y-Axis, line_width, alpha_for_blending,  label)plt.title(title)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Adj. Price USD ($)',fontsize=18)
plt.legend(my_stocks.columns.values, loc='upper left')
plt.show()



''' Calculs financiers

J'ai fini de créer le portfolio fictif. 
Maintenant, je veux montrer les rendements simples quotidiens qui sont un calcul du 
(nouveau_prix + -ancien_prix)/ancien_prix ou (nouveau_prix / ancien_prix)-1. '''

#Afficher les rendements simples quotidiens, REMARQUE : Formule = nouveau_prix/ancien_prix - 1

returns = df.pct_change()
print(returns)


''' Créez et affichez la matrice de covariance annualisée. 
La matrice de covariance est un concept mathématique qui est couramment utilisé dans les statistiques 
lors de la comparaison d'échantillons de données de différentes populations et est utilisé pour déterminer 
dans quelle mesure deux variables aléatoires varient ou se déplacent ensemble 
(c'est donc la relation directionnelle entre deux prix d'actifs).

La diagonale de la matrice sont les variances et les autres entrées sont les covariances. 
La variance est une mesure de la différence entre un ensemble d'observations. 
Si vous prenez la racine carrée de la variance, vous obtenez la volatilité, également appelée écart type.

Pour afficher la matrice de covariance annualisée, nous devons multiplier la matrice de covariance 
par le nombre de jours de bourse pour l'année en cours. 
Dans ce cas, le nombre de jours de bourse sera de 252 pour cette année. '''

cov_matrix_annual = returns.cov() * 252
print(cov_matrix_annual)

# Calculez et affichez maintenant la variance du portefeuille à l'aide de la formule :
# Variance attendue du portefeuille = WT * (Matrice de covariance) * W

port_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))
print(port_variance)

# Enfin, je vais montrer et calculer le rendement simple annuel du portefeuille.

portfolioSimpleAnnualReturn = np.sum(returns.mean()*weights) * 252
print(portfolioSimpleAnnualReturn)

#Affichez le rendement annuel attendu, la volatilité ou le risque et la variance.
percent_var = str(round(port_variance, 2) * 100) + '%'
percent_vols = str(round(port_volatility, 2) * 100) + '%'
percent_ret = str(round(portfolioSimpleAnnualReturn, 2)*100)+'%'print("Expected annual return : "+ percent_ret)
print('Annual volatility/standard deviation/risk : '+percent_vols)
print('Annual variance : '+percent_var)


# Donc, maintenant je peux voir le rendement annuel attendu sur les investissements qui est de 32% 
# et le montant du risque pour ce portefeuille qui est de 23%, mais puis-je faire mieux ? Je crois pouvoir.



''' Optimisation du portefeuille








