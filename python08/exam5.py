# movie.csv파일을 읽어온다
'''
구분,사고(건),사망(명),부상(명)
2016년1월,192,5,387
'''
import pandas as pd

df = pd.read_csv('./data/2016_sleep_driver_accdent.csv')
# 7월에 있는 사고 건수, 부상자 수 출력
print('기간 : {}, 사고 건수 : {}, 부상자 수 {}'.format(df.loc[6, '구분'], df.loc[6, '사고(건)'], df.loc[6, '부상(명)']),'\n')
# df2 = df.drop(['사망(명)'], axis='columns')
# df.drop(['사망(명)'], axis=1, inplace=True)
# print(df2.loc[6])

# 부상자 컬럼의 총 합
print('2016년도 졸음운전 사고 부상자 수 : {}'.format(df['부상(명)'].sum()))

