import pandas as pd

df1 = pd.read_excel('./data/stock price.xlsx')
df2 = pd.read_excel('./data/stock valuation.xlsx')

# df1 중심으로
mg_left = pd.merge(df1, df2, how='outer', left_on='id', right_on='id')
# print(mg_left)
# print(set(df1['id'].unique()))
# print(set(df2['id'].unique()))
# print(set(df1['id'].unique()) - set(df2['id'].unique()))

mg_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(mg_right)



