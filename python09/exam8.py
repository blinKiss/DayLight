import pandas as pd

df = pd.read_csv('./data/2020_0918_company_list.csv')


stock_list = df.상장일.str.split('-').dropna()
# print(stock_list)

year = stock_list.str.get(0)
month = stock_list.str.get(1)
day = stock_list.str.get(2)

# df2 = pd.DataFrame({
#     'Year' : year,
#     'Month' : month,
#     'Day' : day        
# })

# print(df2)

df2 = pd.DataFrame(df['회사명'].dropna())
df2 = df2.assign(Year=year, Month=month, Day=day)
print(df2)

