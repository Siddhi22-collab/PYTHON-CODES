import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate coefficients (slope and intercept)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
slope = numerator / denominator
intercept = y_mean - slope * x_mean

# Prediction line
y_pred = slope * x + intercept

# Print coefficients
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")

# Plot
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear Regression (Manual)')
plt.show()
