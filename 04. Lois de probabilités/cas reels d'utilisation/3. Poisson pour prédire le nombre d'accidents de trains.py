# http://villemin.gerard.free.fr/aMaths/Probabil/Poisson.htm
# https://www.tutorialspoint.com/python_data_science/python_poisson_distribution.htm

# Import des librairies
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

"""   

CAS NUMERO 1 
Sur ce trajet ferroviaire, nous avons constaté deux incidents par an.

"""


# 1. Quelle est la probabilité qu'il y en ait exactement dix en dix ans?
""" 
 lambda = quantité moyenne  = 2 par an, soit 2 x 10 = 20 en 10 ans
    
"""
ma_probabilite = ma_probabilite = poisson.pmf(10, 20)
ma_probabilite = ma_probabilite * 100
print("proba: ", ma_probabilite, "%")

# 2. Quelle est la probabilité qu'il y en ait dix ou moins en dix ans?
""" 
 P(de 0 à 10, 20)

= P(0; 20) + P(1; 20) + … +  P(10; 20)
    
"""

i = 0
total = 0
while i <= 10:
	print(f'{total:9.9f}')
	total += poisson.pmf(i, 20)
	i += 1
  
print("total:",f'{total * 100  :9.9f}' , "%" )


# Ou alors, plus simplement, avec la bonne fonction ...
poisson.cdf(10, 20)
print("total:", poisson.cdf(10, 20))


# GRAPHIQUES
# poisson = np.random.poisson(10, 20)
# plt.hist(poisson)
# plt.show()

# s = np.random.poisson(10,20)

# print(s)

# count, bins, ignored = plt.hist(s, 14, normed=True)
# plt.show()