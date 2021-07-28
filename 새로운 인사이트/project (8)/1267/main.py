import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.
occupation_group = df.groupby('occupation')
occupation_group.mean()
occupation_group.mean().sort_values(by='age')