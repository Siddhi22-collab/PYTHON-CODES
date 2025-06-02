import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=df, palette="Set2")
sns.swarmplot(x='day', y='total_bill', data=df, color=".25")
plt.title("Box Plot with Swarm Overlay")
plt.show()
