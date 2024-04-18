# TRACER UNE FUNCTION SIN
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-15,15,100) # 100 linearly spaced numbers
y = np.sin(x)/x # computing the values of sin(x)/x

# compose plot
plt.plot(x,y) # sin(x)/x
plt.plot(x,y,'co') # same function with cyan dots
plt.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
plt.plot() # trace the plot

# show the plot
plt.show()