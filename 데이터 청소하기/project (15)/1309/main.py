%matplotlib inline
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
T = df.sort_values(by='budget',ascending=True).head(15) #가장 큰 15개 찾기
df.drop(T.index,inplace=True)
df.plot(kind='scatter',x='budget',y='imdb_score')