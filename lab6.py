import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame

# tworzenie dataframe na podstawie słownika

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)

# Sample

print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print(df.head())
print(df.head(2))
print(df.head(1))
print(df.tail())
print(df.describe())
print(df.T)

df.loc[3] = ['Polska', 'Warszawa', 38675467]
new_df = df.drop([1])
print(new_df)

df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

print(df.sort_values('Kraj'))

df = pd.read_csv('iris.data', header=0, sep=",", decimal='.')
print(df)
