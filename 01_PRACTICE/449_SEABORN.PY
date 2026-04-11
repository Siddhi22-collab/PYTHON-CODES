import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(data=tips,x='total_bill',bins=10,color='r',kde=True)
plt.title("Histogram of Total Bill")
plt.show()