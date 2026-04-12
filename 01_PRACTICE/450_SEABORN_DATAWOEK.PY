import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('tips')

sns.displot(
    data=df,
    x='total_bill',
    hue='sex',
    kde=True,
    bins=20,
    multiple='stack',
    col='smoker',
    height=6,
    aspect=1.2,
    palette='Set2'
)

plt.suptitle("Distribution of Total bill with seaborn displot parameter",y=1.05)
plt.show()