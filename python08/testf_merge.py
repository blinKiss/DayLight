import pandas as pd

df1 = pd.read_excel('./data/stock price.xlsx')
df2 = pd.read_excel('./data/stock valuation.xlsx')
print(df1, '\n', df2, '\n')
mg_inner = pd.merge(df1, df2, left_on='stock_name', right_on = 'name')      # 기본값 = inner
print(mg_inner)
mg_outer = pd.merge(df1, df2, how = 'outer') 
print(mg_outer)





