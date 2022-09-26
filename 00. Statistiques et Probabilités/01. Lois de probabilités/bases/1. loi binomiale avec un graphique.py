# https://towardsdatascience.com/fun-with-the-binomial-distribution-96a5ecabf65b

# Lancer une pièce 10 * 10000 fois avec p = 0.5

# Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# variables

# Nombres d'essais
trials = 1000

# Nombre d'expériences indépendante dans chaque essai
n = 10

# Probabilité de succès pour chaque expérience
p = 0.5

# Function qui exécute le lancement de pièces
# heads is a list of the number of successes from each trial of n experiments
def run_binom(trials, n, p):
    heads = []
    for i in range(trials):
        tosses = [np.random.random() for i in range(n)]
        heads.append(len([i for i in tosses if i>=0.50]))
    return heads# Run the function

# Préparer le graphique
heads = run_binom(trials, n, p)
fig, ax = plt.subplots(figsize=(14,7))
ax = sns.distplot(heads, bins=11, label='resultats de simulation')
ax.set_xlabel("Nombre de succès",fontsize=16)
ax.set_ylabel("Frequence",fontsize=16)

# Dessiner la distribution pour checker que c'est plausible
from scipy.stats import binom
x = range(0,11)
ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()