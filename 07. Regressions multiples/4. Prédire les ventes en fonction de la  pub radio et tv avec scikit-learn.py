""" 
# TITRE

Régression multiple linéaire avec scikit-learn
Prédire les ventes en fonction de la  pub radio et tv 

# LE PROBLEME 

    ON VEUT prédire nos ventes en fonction de la somme de  pub radio et tv investies .
    Pour cela, on se sert des informations du passé, de nos DATAS !
    C'est sur que si avec 100 Euros investi en pub pendant 1 an, si on a pas généré plus de 100 euros, on se 
    doute bien que l'année suivante on ne va pas, sauf miracle générer 10 000 euros !C'est logique, sauf que la regression multiple est
    bien plus fiable pour affirmer ce postulat.

    Pour démontrer cette méthode, nous utiliserons un ensemble de données publicitaires très populaire sur les différents coûts 
    encourus pour la publicité par différents supports et les ventes pour un produit particulier.

    Pour ce modèle, nous continuerons d'utiliser l'ensemble de données publicitaires, mais cette fois, 
    nous utiliserons deux variables prédictives pour créer un modèle de régression linéaire multiple. 
    Il s'agit simplement d'un modèle de régression linéaire avec plus d'un prédicteur, et est modélisé par:
    Yₑ = α + β₁X₁ + β₂X₂ +… + βₚXₚ, où p est le nombre de prédicteurs.

    Dans notre exemple, nous prédirons les ventes en utilisant les variables TV et Radio, c'est-à-dire que notre modèle peut s'écrire:
    Ventes = α + β₁ * TV + β₂ * Radio.

TRADUCTION EN FRANCAIS

    Auteur :
    http://faculty.marshall.usc.edu/gareth-james/ 

    Source :
    https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0

    Cours : 
    https://next.tech/xyz/linear-regression?utm_source=medium&utm_medium=referral&utm_campaign=linearregression

    Dépot GITHUB de l'université  Columbia avec énormément de travaux d'élèves !:
    https://github.com/Columbia-Intro-Data-Science


"""

# Librairies
import pandas as pd
from sklearn.linear_model import LinearRegression

# Commençons par importer ce fichier csv en tant que trame de données pandas à l'aide de read_csv ():
advert = pd.read_csv("datasets/Advertising.csv")

# afficher les cinq premières lignes de l'ensemble de données publicitaires
advert.head()

# Tout d'abord, nous initialisons notre modèle de régression linéaire, puis ajustons le modèle à nos prédicteurs et variables de sortie:
predictors = ['TV', 'Radio']
X = advert[predictors]
y = advert['Sales']

# Initialiser et ajuster le modèle
lm = LinearRegression()
model = lm.fit(X, y)

#  Encore une fois, il n'est pas nécessaire de calculer nous-mêmes les valeurs pour alpha et bêta - il suffit d'appeler .intercept_ pour alpha et .coef_ pour un tableau avec nos coefficients beta1 et beta2:
print(f'alpha = {model.intercept_}')
print(f'betas = {model.coef_}')

""" Ca affiche :
alpha = 2.921099912405138
betas = [0.04575482 0.18799423] """

""" Par conséquent, notre modèle peut s'écrire:
Ventes = 2,921 + 0,046 * TV + 0,1880 * Radio.
Nous pouvons prédire des valeurs en utilisant simplement .predict (): """

model.predict(X)

""" 
Maintenant que nous avons adapté un modèle de régression linéaire 
multiple à nos données, 
nous pouvons prédire les ventes à partir de n'importe quelle combinaison de coûts publicitaires TV et radio! 
Par exemple, si nous voulions savoir combien de ventes nous réaliserions si nous investissions 300 $ dans la publicité TV 
et 200 $ dans la publicité Radio… il nous suffit de brancher les valeurs!
 """
new_X = [[300, 200]]
print(model.predict(new_X))

""" Ca affiche que l'on va probablement gagner cette somme en dollars! :
[54.24638977]
""" 
