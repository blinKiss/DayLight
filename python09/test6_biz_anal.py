import numpy as np
import pandas as pd

df1 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv')
# 5개 데이터 (서울, 경기, 인천, 광주, 부산)
df2 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_경기_202212.csv')
df3 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_인천_202212.csv')
df4 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_광주_202212.csv')
df5 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_부산_202212.csv')
# 5개 도시 데이터 결합
df_total = pd.concat([df1, df2, df3, df4, df5])
# print('서울, 경기, 인천, 광주, 부산 내 총 가게 수 : ', df_total.shape[0])
# print(df1.head(n=5))
# print(df1.columns)
df_total_view = df_total[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명', '시도명']]
print(df_total_view)
df_cafe = df_total_view[df_total_view['상권업종중분류명'] == '커피점/카페']
# print('5대도시 카페 수 :', df_cafe.shape[0])
df_cafe_ediya = df_cafe[df_cafe['상호명'].str.contains('이디야')]
df_cafe_ediya.index = range(len(df_cafe_ediya))
print('5대 도시 이디야 매장 수 :', df_cafe_ediya.shape[0])
# print(df_cafe_ediya.head(n=20))
# print('5대 도시 이디야 매장 수 :', df_cafe_ediya.shape[0])

city = sorted(set(df_total_view['시도명']))
print(city)
cntpercity = [len(df_cafe_ediya[df_cafe_ediya['시도명'] == c]) for c in city]
print(cntpercity)

