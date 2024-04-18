# A simple bar chart
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data =[5.,25.,50.,20.]
x = range(len(data)) # creates a range of 0 to 4

plt.bar(x, data)

plt.show()