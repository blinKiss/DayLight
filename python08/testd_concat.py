import pandas as pd

dict1 = {
    'a' : ['red', 'yellow', 'blue', 'green'],
    'b' : ['100px', '200px', '150px', '250px'],
    'c' : ['circle', 'rect', 'rect', 'circle']
}

dict2 = {
    'a' : ['blue', 'green', 'black', 'white'],
    'b' : ['150px', '250px', '300px', '400px'],
    'c' : ['rect', 'circle', 'square', 'square'],
    'd' : ['9px', '99px', '999px', '99px']
}

df1 = pd.DataFrame(dict1)
# print(df1, '\n')
df2 = pd.DataFrame(dict2, index = [3, 4, 5, 6])
# print(df2)
# rst = pd.concat([df1, df2]) # 여러개도 가능 - 기본적으로 상하
# rst = pd.concat([df1, df2], axis = 0, ignore_index = True) # ignore_index 행 번호 무시 
# print(rst)

# rst2 = pd.concat([df1, df2], axis=1) # 기본 중복을 허용 outer
# print(rst2)

# rst3 = pd.concat([df1, df2], axis=1, join='inner')
# print(rst3)

# 1차원 데이터가 초가된다 (2차원에 1차원 추가 : 컬럼이 추가됨)
sr1 = pd.Series(['relative', 'absolute', 'relative', 'absolute'], name='e')
# rst4 = pd.concat([df1, sr1], axis=1)
# print(rst4)
sr2 = pd.Series(['pink', '200px', 'triangle'], name='f')
# print(sr2)
# rst5 = pd.concat([df1, sr2], axis=0)
# print(rst5)

rst6 = pd.concat([sr1, sr2])
print(rst6)
rst7 = pd.concat([sr1, sr2], axis=1)
print(rst7)
