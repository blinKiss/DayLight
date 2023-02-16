import pandas as pd

df = pd.DataFrame({
    'id' : ['Kim', 'Lee', 'Song', 'Sohn', 'Jeon'],
    'pw' : ['1234', '4321', '0987', '1029', '3847'],
    'name' : ['김태희', '이지은', '송승헌', '손예진', '전현무']
})

# print(df[0:3]) # 기존 슬라이싱 마지막 번호 = 크기 - 1
# print(df.loc[0:2]) # 마지막 번호 = 크기(인덱스)
# print(df.loc[:1, 'id':'pw'])
df.loc[5] = ['park', '2323', '박지성'] # 인덱스 5번 추가
print('인덱스 5 추가','\n',df)
df.drop(index = [5], axis = 0, inplace=True) # 인덱스 5번 삭제
# df.drop(df.index[4:6], axis = 0, inplace=True) # 인덱스 4~5번 삭제
print('인덱스 5 삭제','\n',df)