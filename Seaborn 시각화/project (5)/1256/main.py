%matplotlib inline
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/insurance.csv')

# 코드를 작성하세요.
sns.catplot(data=df,x='smoker',y='charges',kind='violin')