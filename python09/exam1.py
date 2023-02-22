import pandas as pd
import numpy as np


df1 = pd.read_csv('./data/emp_data.csv')
df2 = pd.read_csv('./data/dept_data.csv')

# df1에 부서가 없는 사람을 하나 추가해서 테스트
df1.loc[5] = ([1500, '이성철', 50000, None])
# sr1 = pd.Series(([1500, '이성철', 50000, np.NaN]))
mg_data5 = pd.merge(df1, df2, how='outer')
# print(df1)
print(mg_data5)


