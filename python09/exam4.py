import pandas as pd
import re

df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_전남_202212.csv')

df_temp = df[['상호명', '상권업종중분류명']]
# print(df_temp)
# kind = set(df_temp['상권업종중분류명'])
# print(kind)
lib = re.compile('도.*실')
df_library = df_temp[df_temp['상권업종중분류명'].str.contains(lib)]
# 상권업종중분류명=='도서관'
# # 전남에 있는 도서관의 갯수는?
print('전남 지역 내 도서관은?\n{}\n그 갯수는? {}'.format(df_library, df_library.shape[0]))
# df_library_rainbow = df_temp[df_temp['상호명'] == '무지개공부방']
# print(df_library_rainbow)
