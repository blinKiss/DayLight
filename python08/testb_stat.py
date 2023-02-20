import pandas as pd

sampleData = {
    'name' : ['김건우', '윤호민', '손의성'],
    'age' : [20, 25, 35],
    # 'tall' : [170.5, 167.8, None]
    'tall' : [170.5, 167.8, 180.5]
}
df = pd.DataFrame(sampleData)
# print(df)
print(df.sum()) # 기본값 = 열의 합
print(df.sum(axis=0)[1]) # 열의 합
# print(df.sum(axis=1)[1]) # 행의 합

# print(df.mean())


# print(df.min()) # 기본값은 열의 최소, 최대값
# print(df.max())

# print(df.count()) # 기본값은 열의 갯수(단 빈값 None은 제외)

# print(df.median()) # 중간값 찾기

# print(df.sort_values(by='tall', ascending=True)) # 'tall' 을 오름차순으로 정렬 False = 내림차순