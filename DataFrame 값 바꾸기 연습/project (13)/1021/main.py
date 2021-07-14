import pandas as pd

df = pd.read_csv('data/body_imperial2.csv', index_col=0)

# 코드를 작성하세요.
df.loc[0:10,'Gender']='Male'
df.loc[11:20,'Gender']='Female'
df['비만도']='정상'
# 정답 출력
df