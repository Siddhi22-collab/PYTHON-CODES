

import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
sns.violinplot(df)
plt.title("VIOLIN PLOT OF ALL NUMERICAL COLUMN")
plt.show()