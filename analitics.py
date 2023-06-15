import pandas as pd
df = pd.read_csv("file.csv", sep = ",")
# print(df.head(n=10))
# input("     Press Enter")
# print(df.tail(n=10))
# input("     Press Enter")
# print(df.shape)
# input("     Press Enter")
# print(df.isnull().sum())
# input("     Press Enter")
# print(df.dtypes)
# input("     Press Enter")
# print(df.columns)
# input("     Press Enter")
# print(df[['City', 'Country']])
# input("     Press Enter")
# print(df[(df['Latitude'] >0) & (df['Longitude'] >0)])
# input("     Press Enter")
# print(df[(df['Latitude'] >0) & (df['Longitude'] >0)][['City', 'Latitude', 'Longitude']])
# input("     Press Enter")

# Простая статистика

# print(df['Latitude'].max(), df['Latitude'].min())
# print(df['Latitude'].mean(), df['Latitude'].sum())
# print(df[['Latitude','Longitude']].median())
# input("     Press Enter")
# print(df.describe())
# input("     Press Enter")

import seaborn as sns 
sns.scatterplot(data=df, x='Latitude', y='Longitude')
