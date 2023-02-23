import numpy as np
import pandas as pd

data = {
    'A' : [2,4,np.NaN,8,10,12,14,16,18,20],
    'B' : [np.NaN,3,5,np.NaN,9,11,13,15,17,19],
    'C' : [10, np.NaN, 30, 40, 50, np.NaN, 70, 80, 90, 100]
}

df = pd.DataFrame(data)
print(df, '\n')
# print(df.fillna(method = 'ffill')) # NaN -> 앞쪽 값 복제
# print(df.fillna(method = 'bfill')) # NaN -> 뒤쪽 값 복제
# print(df.interpolate()) # 중간 값 채우기
print(df.dropna())