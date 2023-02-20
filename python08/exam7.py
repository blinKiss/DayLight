# 분산 표준편차
# 강아지 5마리 [600mm, 470mm, 170mm, 430mm, 300mm]
# 평균값
# 분산값
# 표준편차값

import pandas as pd

Dog = {
    'size' : [600, 470, 170, 430, 300]
}

df = pd.DataFrame(Dog)
# print(f'평균 : { df.mean()[0] }\n분산 : { df.var()[0] }\n표준편차 : { df.std()[0] }')
print('평균 : {}\n분산 : {}\n표준편차 : {}'.format(df['size'].mean(), df['size'].var(),  df['size'].std()))


