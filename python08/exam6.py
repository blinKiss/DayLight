import pandas as pd

df = pd.read_excel('./data/stock price.xlsx')

# 주식회사 총 몇개?
print(df['stock_name'].count())
# 주식값(price)의 평균?
print(df['price'].mean())
# 주식가치(value)의 중간값?
print(df['value'].median())