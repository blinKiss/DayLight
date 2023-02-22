import numpy as np
import pandas as pd

print(np.NaN) # 값이 없다 : 0이나 ''과는 다른 의미
print(np.NaN == 0)
print(np.NaN == '')
print(np.NaN == np.NaN)

x = None
print(np.NaN == x)

data = {
    'A' : [1,2,3,4,5],
    'B' : [6,7,8,9,np.NaN]    
}
data2 = {
    'C' : [2,4,6,8,10],
    'D' : [1,3,5,7,9]
}

df = pd.DataFrame(data)
# print(df['A'].count())
# print(df['B'].count())
# print(df['B'].sum())
# print(pd.isnull(np.NaN))
print(df, '\n')
df2 = pd.DataFrame(data2)
print(df2, '\n')
df3 = pd.concat([df, df2], ignore_index='True')
print(df3)

