import numpy as np
import matplotlib.pyplot as plt

# Load the points from the text file
points = np.loadtxt("points.dat", delimiter=',', max_rows=len(list(open("./points.dat")))-1)

# Extract the x and y coordinates
x = points[:, 0]
y = points[:, 1]

# Define points
V = np.array([points[0, 0], points[0, 1]])
Y = np.array([points[1, 0], points[1, 1]])
X = np.array([points[2, 0], points[2, 1]])

# Define arbitrary non-unit vectors a and b
a = np.array([1, 3])  # Example vector
b = np.array([2, 1])  # Example vector

# Print the vectors
print("Vector a:", a)
print("Vector b:", b)

# Create a new figure for the plot
plt.figure(figsize=(10, 8))

# Plot points V, Y, and X
plt.plot(V[0], V[1], 'ro', label='Point V')  # Green dot for point V
plt.plot(Y[0], Y[1], 'bo', label='Point Y')  # Blue dot for point Y
plt.plot(X[0], X[1], 'go', label='Point X')  # Blue dot for point X

# Display the coordinates of each point near the point marker
plt.text(V[0], V[1], f'({V[0]:.2f}, {V[1]:.2f})', fontsize=12, ha='right', color='green')
plt.text(Y[0], Y[1], f'({Y[0]:.2f}, {Y[1]:.2f})', fontsize=12, ha='right', color='blue')
plt.text(X[0], X[1], f'({X[0]:.2f}, {X[1]:.2f})', fontsize=12, ha='right', color='blue')

# Plot line segment XY with dashed line
plt.plot([X[0], Y[0]], [X[1], Y[1]], color='black', linestyle='--', label='Line segment XY')

# Plot line segment VX with dotted line
plt.plot([V[0], X[0]], [V[1], X[1]], color='black', linestyle=':', label='Line segment VX')

# Plot the vectors a and b
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Assuming Vector a = i + 3j', linewidth=2)
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Assuming Vector b = 2i + j', linewidth=2)

# Set limits and labels
plt.xlim(-17, 11)
plt.ylim(-17, 11)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='blue', linestyle='--', linewidth=0.5)
plt.title('Plot of Points X, Y, V and Vectors a, b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

