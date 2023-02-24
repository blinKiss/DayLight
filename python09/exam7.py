import pandas as pd

df = pd.read_excel('./data/period.xlsx').fillna(0)
# 미세먼지 평균, 분산, 초미세먼지 평균, 분산
# print(df.columns)
city_list = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
city_slice = city_list[5:len(city_list)]
city_slice.columns = ['자치구', '미세먼지', '초미세먼지']
temp = city_slice[(city_slice['자치구'].str.contains('평균'))].index
city_slice2 = city_slice.drop(temp)
# print(temp)

# print(city_slice)
cities = city_slice2['자치구'].unique()
city = sorted( cities )
# print(city)
city_sort = [(city_slice2[city_slice2['자치구'] == c]) for c in city]
# print(type(city_slice))
# print(city_slice.head(n=10))
# print(city_sort)
# print(city_sort[11]['미세먼지'].values.mean())
print('기록된 서울시 지역별 미세먼지\n')
for c in range(0, len(city_sort)):
    print('{}의 미세먼지 평균 : {}, 분산 : {}, 초미세먼지 평균 : {}, 분산 {}\n'.
        format(city[c],
               round(city_sort[c]['미세먼지'].values.mean()), 
               round(city_sort[c]['미세먼지'].values.var()), 
               round(city_sort[c]['초미세먼지'].values.mean()), 
               round(city_sort[c]['초미세먼지'].values.var())))

