''' 
Optimisation de portefeuille avec la méthode Markovitz (La méthode et les concepts de base à connaitre)

Url : https://colab.research.google.com/github/cvxgrp/cvx_short_course/blob/master/applications/portfolio_optimization.ipynb#scrollTo=-BeEx_yHd7CB
url : https://www.centralcharts.com/fr/gm/1-apprendre/3-bourse/5-gestion-portefeuille/211-theorie-du-portefeuille-selon-markowitz 

Vecteur d'allocation de portefeuille

Dans cet exemple, nous montrons comment optimiser un portefeuille à l'aide de CVXPY. Commençons par les définitions de base. Dans l'optimisation de portefeuille, nous avons une certaine somme d'argent à investir dans l'un des n actifs différents. Nous choisissons quelle fraction wi de notre argent investir dans chaque actif i, i=1,…,n.

Nous appelons w∈Rn le vecteur d'allocation de portefeuille. 
Nous avons bien sûr la contrainte que 1Tw=1. 
L'allocation wi<0 signifie une position courte sur l'actif i, ou que nous empruntons des actions à vendre maintenant que nous devons remplacer plus tard. L'allocation w≥0 est un portefeuille long only. La quantité
w∥1=1Tw++1Tw− est connu sous le nom de levier.

Rendement des actifs

Nous ne modéliserons que les investissements détenus pendant une période. 
Les prix initiaux sont pi>0. 
Les prix de fin de période sont p+i>0. 
Les rendements (fractionnels) des actifs sont ri=(p+i−pi)/pi. 
Le rendement du portefeuille (fractionnel) est R=rTw.
Un modèle courant est que r est une variable aléatoire avec une moyenne Er=μ et une covariance E(r−μ)(r−μ)T=Σ. 
Il s'ensuit que R est une variable aléatoire avec ER=μTw et var(R)=wTΣw. 
ER est le rendement (moyen) du portefeuille. 
var(R) est le risque du portefeuille. (Le risque est aussi parfois donné par std(R)=var(R)−−−−−−√.)
L'optimisation de portefeuille a deux objectifs concurrents : un rendement élevé et un faible risque. 

Optimisation de portefeuille classique (Markowitz)

L'optimisation de portefeuille classique (Markowitz) résout le problème d'optimisation
maximisersous réserve deμTw−γwTΣw1Tw=1,w∈W,

où w∈Rn est la variable d'optimisation, W est un ensemble de portefeuilles autorisés 
(par exemple, W=Rn+ pour un portefeuille long only), et γ>0 est le paramètre d'aversion au risque.

L'objectif μTw−γwTΣw est le rendement ajusté en fonction du risque. 
La variation de donne le compromis risque-rendement optimal. 
Nous pouvons obtenir le même compromis risque-rendement en fixant le rendement et en minimisant le risque.

'''
# Generate data for long only portfolio optimization.
import numpy as np
import scipy.sparse as sp
np.random.seed(1)
n = 10
mu = np.abs(np.random.randn(n, 1))
Sigma = np.random.randn(n, n)
Sigma = Sigma.T.dot(Sigma)

# Long only portfolio optimization.
import cvxpy as cp


w = cp.Variable(n)
gamma = cp.Parameter(nonneg=True)
ret = mu.T@w 
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Maximize(ret - gamma*risk), 
               [cp.sum(w) == 1, 
                w >= 0])

# Compute trade-off curve.
SAMPLES = 100
risk_data = np.zeros(SAMPLES)
ret_data = np.zeros(SAMPLES)
gamma_vals = np.logspace(-2, 3, num=SAMPLES)
for i in range(SAMPLES):
    gamma.value = gamma_vals[i]
    prob.solve()
    risk_data[i] = cp.sqrt(risk).value
    ret_data[i] = ret.value

# Plot long only trade-off curve.
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'

markers_on = [29, 40]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(risk_data, ret_data, 'g-')
for marker in markers_on:
    plt.plot(risk_data[marker], ret_data[marker], 'bs')
    ax.annotate(r"$\gamma = %.2f$" % gamma_vals[marker], xy=(risk_data[marker]+.08, ret_data[marker]-.03))
for i in range(n):
    plt.plot(cp.sqrt(Sigma[i,i]).value, mu[i], 'ro')
plt.xlabel('Standard deviation')
plt.ylabel('Return')
plt.show()
