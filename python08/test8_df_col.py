import pandas as pd

df = pd.DataFrame({
    'id' : ['Kim', 'Lee', 'Song', 'Sohn', 'Jeon'],
    'pw' : ['1234', '4321', '0987', '1029', '3847'],
    'name' : ['김태희', '이지은', '송승헌', '손예진', '전현무']
})

# print(df[['id', 'name']])
df['age'] = [20, 15, 19, 17, 26]
df['gender'] = ['f', 'f', 'm', 'f', 'm']

# 논리값 True / False
# df['adult'] = df['age'] >= 19

# 문자열 숫자 비교해서 추가
df['age_group'] = ['adult' if a >= 19 else 'junior' for a in df['age']]
# 삭제
del df['age_group']
print(df)