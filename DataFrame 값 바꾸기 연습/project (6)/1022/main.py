import pandas as pd
    
df = pd.read_csv('data/toeic.csv')

# 코드를 작성하세요.
pass_total = df['LC'] + df['RC'] > 600
pass_both = (df['LC'] >= 250) & ( df['RC'] >= 250)
df['합격 여부'] = pass_total & pass_both
# 정답 출력
df