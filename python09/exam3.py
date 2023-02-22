import numpy as np
import pandas as pd

df = pd.read_csv('./data/california-history.csv')

# 전체 행 갯수를 구하시오
print('전체 행 갯수 :', df.shape[0])
# hospitalizedCurrently 컬럼에서 결측갯수를 출력하시오
print('hospitalizedCurrently 컬럼 내 결측 개수 :', df['hospitalizedCurrently'].isnull().sum())