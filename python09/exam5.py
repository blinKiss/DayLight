import pandas as pd

df1 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대전_202212.csv')
df2 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대구_202212.csv')
df3 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_제주_202212.csv')
df4 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_세종_202212.csv')
df5 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_울산_202212.csv')

df_total = pd.concat([df1, df2, df3, df4, df5])
df_total_view = df_total[['상호명', '상권업종중분류명']]
# print(df_total_view.head(n=5))
# df_bakery = df_total_view[df_total_view['상권업종중분류명'].str.contains('제과')]
df_bakery = df_total_view[df_total_view['상권업종중분류명'] == '제과제빵떡케익']
# print(df_bakery)

paris = df_bakery[df_bakery['상호명'].str.contains('파리')]
tous = df_bakery[df_bakery['상호명'].str.contains('뚜레')]

if((paris.shape[0] > tous.shape[0]) == True):
    print('빠바가 더 많음')
else:
    print('뚜쥬가 더 많음')
