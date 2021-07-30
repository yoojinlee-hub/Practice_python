%matplotlib inline
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
t=df.sort_values(by='budget',ascending=False).head(15) #큰 값 15개 찾기
df.drop(t.index,inplace=True)
df.plot(kind='scatter',x='budget',y='imdb_score')