%matplotlib inline
import pandas as pd

df = pd.read_csv('data/gdp.csv', index_col=0)

# 코드를 작성하세요.
nations = pd.Series(df.columns)
nations[nations.str.contains('Korea')] #Korea_Rep
nations[nations.str.contains('German')] #Germany
nations[nations.str.contains('China')] #China
nations[nations.str.contains('United')] #United_States , United_Kingdom
nations[nations.str.contains('Japan')] #Japan

df[['Korea_Rep','United_States','United_Kingdom','Germany','China','Japan']].plot()