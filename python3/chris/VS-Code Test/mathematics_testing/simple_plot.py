import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-5, 5, 500)

# Create y values (example: sine function and quadratic function)
y_sine = 5*np.sin(x)
y_quad = 3*x**2+2*x+1

# Plot the graphs
plt.plot(x, y_sine, label='Sine Function', color='blue')
plt.plot(x, y_quad, label='Quadratic Function', color='red')
plt.title('Plot of Sine and Quadratic Functions')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Display the graph
plt.show()
