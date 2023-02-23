import pandas as pd

df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv')

print('행 갯수 :', df.shape[0])

df_my = df[['상호명', '상권업종중분류명']]

# print(df_my.head(n=5))

kind = set(df_my['상권업종중분류명'])

# print(kind)
# print(sorted(kind))

df_mystore = df_my[df_my['상권업종중분류명'] == '커피점/카페']
print(df_mystore)