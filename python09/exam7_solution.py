import pandas as pd
import numpy as np

df = pd.read_excel('./DayLight/data/period.xlsx')

# print(df.columns)
# print(set(df['측정소명']))

dfv = df.iloc[5:, 1:4]
dfv.columns = ['자치구', '미세먼지', '초미세먼지']
temp = dfv[dfv['자치구'].str.contains('평균')].index
dfv2 = dfv.drop(temp)
# print(dfv)
print(dfv2.groupby('자치구').mean())
# print('----------------')
# print(dfv2.groupby('자치구').var())
# print('----------------')
# print(dfv2.groupby('자치구').std())