""" 
** Problème d'optimisation financière 4 : un portefeuille.

L'optimisation du portefeuille est le processus de sélection du meilleur portefeuille (répartition des actifs), 
parmi l'ensemble de tous les portefeuilles considérés, selon un objectif.
L'objectif maximise généralement les facteurs tels que le rendement attendu 
 et minimise les coûts tels que le risque financier.
-Wikipédia

** Source : 
https://medium.com/@randerson112358/python-for-finance-portfolio-optimization-66882498847
http://www.moneychimp.com/articles/risk/sharpe_ratio.htm
http://www.moneychimp.com/articles/risk/riskintro.htm

Liens IMPORTANT en Français : 
https://www.abcbourse.com/apprendre/19_ratio_de_sharpe.html

 """



""" 
Dans cet article, je vais vous montrer comment créer un programme pour optimiser un portefeuille d'actions 
en utilisant l'algo 'efficent frontier' et Python! 


Dans la théorie moderne du portefeuille, la frontière efficiente est un portefeuille d’investissement qui occupe les parties «efficaces» 
du spectre risque-rendement. Formellement, c'est l'ensemble des portefeuilles qui remplit la condition qu'aucun autre portefeuille 
n'existe avec un rendement attendu plus élevé mais avec le même écart-type de rendement.


Le  Sharpe ratio va plus loin: il vous aide en fait à trouver la meilleure proportion possible de ces actions à utiliser, 
dans un portefeuille.

-  lien Moneychimp


Le Sharpe ratio a été développé par William F. Sharpe en 1966. Le ratio décrit le rendement excédentaire que vous recevez pour 
la volatilité supplémentaire que vous endurez pour détenir un actif plus risqué. 

Il mesure la performance d'un investissement par rapport à un actif sans risque (obligations, bons du Trésor, etc.), après ajustement de son risque.

 Il est défini comme la différence entre le rendement de l'investissement et le rendement sans risque, divisé par l'écart type de l'investissement.

- lien Investopédia https://www.investopedia.com/articles/07/sharpe_ratio.asp


Alors, qu'est-ce qui est considéré comme un bon ratio de Sharpe qui indique un degré élevé de rendement attendu pour un niveau de risque 
relativement faible?

En général, tout ratio de Sharpe supérieur à 1,0 est considéré comme acceptable à bon par les investisseurs. 
Un ratio supérieur à 2,0 est considéré comme très bon. Un ratio de 3,0 ou plus est considéré comme excellent. Un ratio inférieur à 1,0 
est considéré comme sous-optimal.

Si vous préférez ne pas lire cet article et souhaitez une représentation vidéo de celui-ci, 
vous pouvez consulter la vidéo YouTube. Il passe en revue tout dans cet article avec un peu plus de détails et vous aidera à démarrer 
facilement la programmation même si le langage de programmation 

Python n'est pas installé sur votre ordinateur. Ou vous pouvez utiliser les deux comme matériel supplémentaire pour apprendre! """


# Description: Ce programme tente d'optimiser un portefeuille d'utilisateurs en utilisant Efficient Frontier & Python.

# Importer les librairies python
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Créer le portefeuille fictif
""" Obtenez les symboles boursiers / tickers pour le portefeuille fictif. Je vais utiliser les cinq sociétés technologiques américaines les plus populaires et les plus performantes 
connues sous le nom de FAANG, acronyme de Facebook, Amazon, Apple, Netflix et Alphabet (anciennement Google). """

actifs =  ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

# Attribution des invesitssements
""" Ensuite, j'attribuerai des pondérations équivalentes à chaque action du portefeuille, ce qui signifie que 20% de ce portefeuille 
aura des actions dans Facebook (FB), 20% dans Amazon (AMZN), 20% dans Apple (AAPL), 20% dans Netflix (NFLX) ) et 20% dans Google (GOOG).
Cela signifie que si j'avais un total de 100 $ USD dans le portefeuille, alors j'aurais 20 $ USD dans chaque action. """

# Attribuez des poids aux stocks. Les poids doivent être = 1 donc 0,2 pour chacun
poids = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
poids


""" Maintenant, je vais obtenir la date de début des actions qui sera le 1er janvier 2013, et la date de fin qui sera la date actuelle (aujourd'hui). """

# Obtenez la date de début du stock
stockStartDate = '2013-01-01'

# Obtenez la date de fin des actions aka la date d'aujourd'hui et formatez-la sous la forme AAAA-MM-JJ
today = datetime.today().strftime('%Y-%m-%d')

""" Il est temps de créer le bloc de données qui contiendra le prix de clôture ajusté des actions. """


# Créer un dataframe pour stocker le cours de clôture ajusté des actions
df = pd.DataFrame()

# Stocker le prix de clôture ajusté de l'action dans le bloc de données
for stock in actifs:
    df[stock] = web.DataReader(stock,data_source='yahoo',start=stockStartDate , end=today)['Adj Close']
print(df)

# ----------------------------------------------   Montrer visuellement les cours des actions. ----------------------------------------------

# Create the title 'Portfolio Adj Close Price History
title = 'Portfolio Adj. Close Price History    '

# Get the stocks
my_stocks = df

# Créer les points
plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5

# Loop through each stock and plot the Adj Close for each day
for c in my_stocks.columns.values:
    plt.plot( my_stocks[c],  label=c)
#plt.plot( X-Axis , Y-Axis, line_width, alpha_for_blending,  label)plt.title(title)

plt.xlabel('Date',fontsize=18)

plt.ylabel('Adj. Price USD ($)',fontsize=18)

plt.legend(my_stocks.columns.values, loc='upper left')

plt.show()





