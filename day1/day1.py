import pandas as pd
import numpy as np

df = pd.read_csv('input.txt', sep='   ', header = None, engine='python')
df.columns = ['ID1', 'ID2']

df_sorted = df.apply(lambda col: col.sort_values().values)

df_sorted['diff'] = df_sorted['ID2'] - df_sorted['ID1']
df_sorted['diff'] = df_sorted['diff'].abs()

tot = df_sorted['diff'].sum()
print('Solution to part one:',tot)

count_col1 = df['ID1'].value_counts().sort_index()

count_col2 = df[df['ID2'].isin(count_col1.index)]['ID2'].value_counts().sort_index()

combined_counts = pd.DataFrame({'number': count_col1.index, 'Count_ID1': count_col1.values})
combined_counts['Count_ID2'] = combined_counts['number'].map(count_col2).fillna(0).astype(int)

combined_counts['similarity_score'] = combined_counts['number'] * combined_counts['Count_ID1'] * combined_counts['Count_ID2'] 
tot_similarity = combined_counts['similarity_score'].sum()
print('Soulution to part two:',tot_similarity)
