import pandas as pd

df = pd.read_excel('./data/codefilex.xlsx')

print('전국 은행 지점 수 :', df.shape[0])
df_slice = df[['은행코드', '점포명', '주소', '전화번호']]
# print(df_slice)
df_woori = df_slice[df_slice['점포명'].str.contains('우리.*은행')]
print(df_woori)

