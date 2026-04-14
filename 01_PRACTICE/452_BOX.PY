import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

df.groupby('day',observed=False)["total_bill"].describe().T
