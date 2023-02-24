import pandas as pd

df_ebo = pd.read_csv('./data/country_timeseries.csv', low_memory=False)
# print(df_ebo)
print(df_ebo.shape[0])

df_ebo_v = df_ebo.iloc[:, [0,1,2,3,10,11]] # 행, 열
# print(df_ebo_v)
df_ebo_long = df_ebo_v.melt(id_vars=['Date', 'Day'])
# print(df_ebo_long)
var_split = df_ebo_long.variable.str.split('_')
# print(var_split) # Series
var_split2 = df_ebo_long.Date.str.split('/')
# print(var_split2)
# print(var_split[0]) # Series
status = var_split.str.get(0)
country = var_split.str.get(1)
df_ebo_long['status'] = status
print(df_ebo_long)

# 시도명_구_동
# 서울특별시 영등포구 당산동

