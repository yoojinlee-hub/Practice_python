import pandas as pd

df = pd.read_csv('data/steam_1.csv')

# 코드를 작성하세요.
df['Hours'].dropna(inplace=True) 
# 정답 출력
df