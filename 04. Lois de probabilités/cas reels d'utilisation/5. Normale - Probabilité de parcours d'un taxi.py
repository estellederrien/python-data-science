# https://www.maths-et-tiques.fr/telech/LoisTESL.pdf
# https://stackoverflow.com/questions/12412895/calculate-probability-in-normal-distribution-given-mean-std-in-python

# Import des librairies
import scipy.stats


# Problème : 
"""  
Une compagnie de transport possède un parc de 200 taxis. On appelle X, la variable aléatoire qui, à un taxi choisi au hasard associe la distance journalière parcourue.
On suppose que X suit la loi normale (90,14 au carré). (moyenne, écart type)
Quelle est la probabilité qu'un taxi parcourt entre 70 et 100 km par jour ?

"""

# On fait un 'RANGE' pour obtenir l'aire sous la courbe (intégrale)
rv = scipy.stats.norm(90,14)
resultat = rv.cdf(100) - rv.cdf(70)
print("La probabilité qu'un taxi parcours entre 70 et 100kms est de : ", resultat * 100 ,"%" )



# Autres fonctionnalités de la loi normale : 
""" import scipy.stats
scipy.stats.norm(loc=100, scale=12)
#where loc is the mean and scale is the std dev
#if you wish to pull out a random number from your distribution
scipy.stats.norm.rvs(loc=100, scale=12)

#To find the probability that the variable has a value LESS than or equal
#let's say 113, you'd use CDF cumulative Density Function
scipy.stats.norm.cdf(113,100,12)
Output: 0.86066975255037792
#or 86.07% probability

#To find the probability that the variable has a value GREATER than or
#equal to let's say 125, you'd use SF Survival Function 
scipy.stats.norm.sf(125,100,12)
Output: 0.018610425189886332
#or 1.86%

#To find the variate for which the probability is given, let's say the 
#value which needed to provide a 98% probability, you'd use the 
#PPF Percent Point Function
scipy.stats.norm.ppf(.98,100,12)
Output: 124.64498692758187



 """
