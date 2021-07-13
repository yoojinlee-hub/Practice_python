import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 코드를 작성하세요.
days = samsong_df['요일']
samsongs= samsong_df['문화생활비']
hyundaes=hyundee_df['문화생활비']
dict1 = {
    'day': days, 
    'samsong': samsongs, 
    'hyundee': hyundaes
}
df=pd.DataFrame(dict1)
df