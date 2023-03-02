import pandas as pd

df = pd.read_excel('./DayLight/data/period.xlsx').fillna(0)
# 미세먼지 평균, 분산, 초미세먼지 평균, 분산
# print(df.columns)
# df2 = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
df2 = df.iloc[5:, 1:4]
df2.columns = ['자치구', '미세먼지', '초미세먼지']
temp = df2[(df2['자치구'].str.contains('평균'))].index
city_slice2 = df2.drop(temp)
# print(temp)
mean = round(city_slice2.groupby('자치구').mean())
mean = mean.rename(columns={'미세먼지' : '미세먼지 평균', '초미세먼지' : '초미세먼지 평균'})
# print(city_slice2.groupby('자치구').mean().agg({'미세먼지' : ['미세먼지 평균']}))


var = round(city_slice2.groupby('자치구').var())
var = var.rename(columns={'미세먼지' : '미세먼지 분산', '초미세먼지' : '초미세먼지 분산'})

con = pd.concat([mean, var], axis=1)
print(con)


# print(city_slice)
# cities = city_slice2['자치구'].unique()
# city = sorted( cities )
# print(city)
# city_sort = [(city_slice2[city_slice2['자치구'] == c]) for c in city]
# print(type(city_slice))
# print(city_slice.head(n=10))
# print(city_sort)
# print(city_sort[11]['미세먼지'].values.mean())
# print('기록된 서울시 자치구별 미세먼지\n')
# mise = []
# for c in range(0, len(city_sort)):
#     print('{}의 미세먼지 평균 : {}, 분산 : {}, 초미세먼지 평균 : {}, 분산 {}\n'.
#         format(city[c],
#                mise.appendround(city_sort[c]['미세먼지'].values.mean()), 
#                round(city_sort[c]['미세먼지'].values.var()), 
#                round(city_sort[c]['초미세먼지'].values.mean()), 
#                round(city_sort[c]['초미세먼지'].values.var())))


