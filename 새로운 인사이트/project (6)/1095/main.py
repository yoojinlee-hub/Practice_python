import pandas as pd

df = pd.read_csv('data/museum_1.csv')

#콜럼 추가
df['분류']='일반'
#대학이 포함된 것
#그렇지 않은 것 df[df['시설명'].str.contains('대학')==False]
univ=df[df['시설명'].str.contains('대학')].index
# univ에 포함되는 '분류'컬럼을 '대학'으로  수정
df.loc[univ,'분류']='대학'
df
