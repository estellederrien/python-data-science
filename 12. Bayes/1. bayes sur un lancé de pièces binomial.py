# SOURCE  :  https://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Ch1_Introduction_PyMC2.ipynb
# Le code ci-dessous peut être passé, car il n'est actuellement pas important, plus il
# utilise des sujets avancés que nous n'avons pas encore abordés. REGARDEZ LA PHOTO, MICHAEL!
# %matplotlib inline
from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
figsize(11, 9)

import scipy.stats as stats

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
data = stats.bernoulli.rvs(0.5, size=n_trials[-1])
x = np.linspace(0, 1, 100)

# Pour les déjà préparés, j'utilise le conj de Binomial. avant.

for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials) / 2, 2, k + 1)
    plt.xlabel("$p$, probability of piles") \
        if k in [0, len(n_trials) - 1] else None
    plt.setp(sx.get_yticklabels(), visible=False)
    piles = data[:N].sum()
    y = dist.pdf(x, 1 + piles, 1 + N - piles)
    plt.plot(x, y, label="observer% d lancers, \ n% d piles" % (N, piles))
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)


plt.suptitle("Mise à jour bayésienne des probabilités postérieures",
             y=1.02,
             fontsize=14)

plt.tight_layout()

# Afficher les graphiques

plt.show() 