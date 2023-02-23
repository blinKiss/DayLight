import numpy as np
import pandas as pd

df = pd.read_csv('./data/country_timeseries.csv')

# 결측값을 모두 0으로 바꾸시오
print(df.fillna(0)) # NaN -> 모두 0으로 변경
# print(df.fillna(0).head(n=10)) # 10개만 출력

# 결측값을 method=ffill을 사용해서 바꾸시오
print(df.fillna(method='ffill'))
# print(df.fillna(method='bfill'))
print(df.shape[0]) # 전체 갯수 = 122
print(df['Cases_Liberia'].fillna(method='ffill').count()) # ffill로 채운 갯수 = 120, 채우지 못한 갯수 = 2