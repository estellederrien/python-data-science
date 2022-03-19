""" 

Python niveau Lycée / Fac  :

Tracer 3 lois normales



Sources :
https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html

"""
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)

print(plt.hist(x1, **kwargs))
print(plt.hist(x2, **kwargs))
print(plt.hist(x3, **kwargs))

plt.show()

