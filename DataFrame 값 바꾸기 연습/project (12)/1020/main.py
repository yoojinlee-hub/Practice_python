import pandas as pd

df = pd.read_csv('data/body_imperial1.csv', index_col=0)

# 코드를 작성하세요.
df.loc[1,'Weight (Pound)']=200
df.drop(21,axis='index',inplace=True)
df.loc[20]=[70,200]
# 정답 출력
df