# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.array(range(10))
y = x ** 2

# Create the plot
plt.plot(x,y,label='y = x**2')
plt.plot(x,(1/2)* y + 7,label='y = (1/2) * (x**2) + 7')
plt.plot(x,y + 3,label='y = x**2 + 3')
plt.plot(x,y - 5,label='y = x**2 - 5')
plt.plot(x,y - 3,label='y = x**2 - 3')

# Add a title
plt.title('Mes premiers tracés de fonction avec python')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()