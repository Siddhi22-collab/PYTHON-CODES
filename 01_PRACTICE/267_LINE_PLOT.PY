import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 20]

# Create plot
plt.plot(x, y, color='blue', marker='o', linestyle='--')
plt.title('Basic Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
