# 넘파이 2차원 배열을 선언하고 수학점수, 영어점수, 과학점수
# 100 80 70
# 90 60 70
# 90 80 100
# 데이터프레임 df
# math eng sci
import numpy as np
import pandas as pd

mes = np.array([
    [100, 80, 70],
    [90, 60, 70],
    [90, 80, 100]
])
# print(mes)
# df = pd.DataFrame(mes)
# print(df)
df = pd.DataFrame(mes, columns = ['Math', 'Eng', 'Sci'], index = ['재석', '형돈', '홍철'])
print(df.to_string(index=False)) # 인덱스 번호쪽 출력 x