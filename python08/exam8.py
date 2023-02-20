# concat 123 csv 파일 병합

import pandas as pd

data1 = pd.read_csv('./data/concat_1.csv')
data2 = pd.read_csv('./data/concat_2.csv')
data3 = pd.read_csv('./data/concat_3.csv')

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df2_1 = df2.set_axis(['E', 'F', 'G', 'H'], axis=1)
# df3_1 = df3.set_axis(['I', 'J', 'K', 'L'], axis=1)
df3_1 = df3.rename(columns={'A' : 'I', 'B' : 'J', 'C' : 'K', 'D' : 'L', })

con1 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(con1)

con2 = pd.concat([df1, df2_1, df3_1], axis=1)
print(con2)

# con3 = pd.concat([df1, df2, df3], axis=1)
# print(con3.sort_index(axis=1))

