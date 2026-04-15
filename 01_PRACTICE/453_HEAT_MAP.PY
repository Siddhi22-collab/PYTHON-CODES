import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')

corr_df=df.corr(numeric_only=True)
corr_df