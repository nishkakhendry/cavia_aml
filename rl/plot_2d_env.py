import matplotlib.pyplot as plt
import numpy as np

# Create the figure and axis
fig, ax = plt.subplots()

# Set the x and y limits
ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])

# Add grid lines
ax.grid(True)

# Optionally, set ticks to be more specific (here 11 ticks from -0.5 to 0.5)
ax.set_xticks(np.linspace(-0.5, 0.5, 11))
ax.set_yticks(np.linspace(-0.5, 0.5, 11))

# Plot a red cross at (0,0)
ax.plot(-0.2, 0.3, 'rx', markersize=15, markeredgewidth=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grid with Red Cross at (-0.2, 0.3)')
plt.show()
