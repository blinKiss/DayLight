import pandas as pd
import numpy as np

emp = {
    'emp_id' : [1000, 1100, 1200, 1300, 1400],
    'name' : ['김창섭', '박영권', '이수민', '조민희', '최종철'],
    'salary' : [25000, 30000, 40000, 30000, 30000],
    'dept_id' : [2, 1, 2, 2, 3]
}

dept = {
    'dept_id' : [1, 2, 3, 4],
    'dept_name' : ['영업', '기획', '개발', '총무'],
    'mng_id' : [1100, 1200, 1400, None]
}

df1 = pd.DataFrame(emp)
df2 = pd.DataFrame(dept)

# mg_data1 = pd.merge(df1, df2, how='inner')
# print('inner merge :', '\n', mg_data1)

# mg_data2 = pd.merge(df1, df2, how='left')
# print('left merge :', '\n', mg_data2)

# mg_data3 = pd.merge(df1, df2, how='outer')
# print('outer merge :', '\n', mg_data3)

# mg_data4 = pd.merge(df1, df2, how='right')
# print('right merge :','\n', mg_data4)

# mg_data4 = pd.merge(df1, df2)
# print('full merge :','\n', mg_data4)

# df1에 부서가 없는 사람을 하나 추가해서 테스트
df1.loc[5] = ([1500, '이성철', 50000, None])
# sr1 = pd.Series(([1500, '이성철', 50000, np.NaN]))
mg_data5 = pd.merge(df1, df2, how='outer')
# print(df1)
print(mg_data5)


