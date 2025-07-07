import pandas as pd
dict = {
    'A': [1, 2, 3],         
    'B': [4, 5, 6], 

    'C': [7, 8, 9]
}
df = pd.DataFrame(dict)
print("Original DataFrame:")
print(df)
# Melting the DataFrame
df_melted = pd.melt(df, var_name='Variable', value_name='Value')
print("\nMelted DataFrame:")                