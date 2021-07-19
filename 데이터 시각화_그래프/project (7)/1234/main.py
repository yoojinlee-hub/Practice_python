%matplotlib inline
import pandas as pd

df = pd.read_csv('data/starbucks_drinks.csv')

# 코드를 작성하세요.
df.plot(kind='box',y=' Total Carbohydrates (g) ')