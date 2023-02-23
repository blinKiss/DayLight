import numpy as np
import pandas as pd

df = pd.read_csv('./data/country_timeseries.csv')
# print(df.head(n=5))
# print(df.shape[0]) # 0은 행의 수, 1은 열의 수
# print(df['Cases_Guinea'].count())

print('기니 총 사망자 수 : {}, 사망자 없는 날 수 : {}'.format(df['Deaths_Guinea'].count(), df.shape[0] - df['Deaths_Guinea'].count()))


# total_row = df.shape[0]
# count_row = df['Deaths_Guinea'].count()
# print(total_row)
# print(count_row)
# result_row = total_row - count_row
# print(result_row)

# # 다른방법
# print(df.isnull().head(n=5))
# print(np.count_nonzero( df['Deaths_Guinea'].isnull()))





