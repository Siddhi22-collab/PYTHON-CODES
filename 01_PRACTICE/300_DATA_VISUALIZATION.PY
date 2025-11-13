import matplotlib.pyplot as plt
import seaborn as sns

# Pairplot of features
sns.pairplot(data, hue='species')
plt.show()

# Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()
