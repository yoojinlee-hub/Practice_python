import pandas as pd

museum = pd.read_csv("data/museum_3.csv", dtype={'지역번호': str})
number = pd.read_csv("data/region_number.csv", dtype={'지역번호': str})

# 코드를 작성하세요.
pd.merge(museum,number,on='지역번호',how='left')