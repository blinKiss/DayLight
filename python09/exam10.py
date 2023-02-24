import pandas as pd

# 중복값 제거
shoes = [
    ['2022-01-01','BL0001', 20000, '검정색'],
    ['2022-01-01','SF0001', 10000, '하얀색'],
    ['2022-01-01','SA0001', 12000, '분홍색'],
    ['2022-01-01','BH0003', 30000, '검정색'],
    ['2022-01-05','SF0001', 9000, '하얀색'],
    ['2022-01-20','BL0001', 19000, '검정색'],
    ['2022-01-10','BH0003', 25000, '검정색'],
    ['2022-01-22','BL0001', 17500, '검정색'],
    ['2022-01-19','SA0001', 10000, '하얀색']
]
df = pd.DataFrame(shoes, columns=['regdate', 'prod_code', 'price', 'color'])
# print(df)

df_pcode = df[['prod_code']]

df_modify = df_pcode.drop_duplicates()

print(df.drop_duplicates(['prod_code']))