import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7, 8]

salary = [30, 35, 40, 45, 50, 55, 60, 65]

# Dots
plt.scatter(experience, salary)

# Line
plt.plot(experience, salary)

plt.xlabel("Experience")
plt.ylabel("Salary")

plt.title("Experience vs Salary")

plt.show()