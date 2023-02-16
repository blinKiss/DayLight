import pandas as pd
'''
ID,LAST_NAME,AGE
1,KIM,30
2,CHOI,25
3,LEE,41
4,PARK,19
5,LIM,36
'''

# vsproject_project 루트 폴더
# data 폴더 생성

df = pd.read_csv('./data/test_file.csv')
# print(df)
# print(df.loc[0:1])
print(df.loc[:3, 'LAST_NAME']) # 행과 열이름 동시에 만족하는 값
