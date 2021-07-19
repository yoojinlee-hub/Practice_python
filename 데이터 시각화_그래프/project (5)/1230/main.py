%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 코드를 작성하세요.
adobe = (df['company']=='Adobe')&(df['race']=='Overall_totals')&(df['count']!=0)
except_total = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')
abobe_job = df[adobe & except_total]
df[adobe & except_total].set_index('job_category', inplace=False).plot(kind='pie', y= 'count')