import pandas as pd
import glob as glob
import numpy as np
import re
math = ['100', '90', 70]
sr = pd.Series(math)

print(pd.to_numeric(sr), '\n')


eng = ['80', 'asd', 90]
sr2 = pd.Series(eng)

print(pd.to_numeric(sr2, errors='coerce'), '\n') # coerce = 알 수 없는 값을 NaN으로

data = {
    'name' : ['유재석', '정형돈', '노홍철'],
    'eng' : ['80', 90, 'asd']
}
df_class = pd.DataFrame(data)
print('사람 수 : {}, 영어점수 총 합 : {}'.
      format(df_class['name'].shape[0] ,pd.to_numeric(df_class['eng'], errors='coerce').sum()), '\n')

data2 = {
    'name' : ['유재석', '정형돈', '노홍철'],
    'math' : ['70', 80, '90']
}
df_class2 = pd.DataFrame(data2)
# print(df_class2)
me = pd.merge(df_class, df_class2)
total = []
for i in range(len(me)):
    name = me['name'][i]
    if(np.isnan(pd.to_numeric(me['eng'][i], errors='coerce')) == True):
        print(f'{name}님의 영어 성적은 숫자가 아닌 값이므로 0점으로 처리됩니다')
        me['eng'][i] = 0
    sum = pd.to_numeric(me['eng'][i], errors='coerce') + pd.to_numeric(me['math'][i])
    print(f'{name}님의 영어,수학 점수 합계는 : {sum}')
    total.append(sum)
me['total'] = total
print(me)
    
# 각 사람의 총합을 구하시오 'total' 컬럼으로
# df_class['eng'] = pd.to_numeric(df_class['eng'], errors='coerce')
# df_class2['math'] = pd.to_numeric(df_class2['math'])
# for i in range(len(eng)):
#     if(np.isnan(eng[i]) == True):
#         eng[i] = 0    
# me = pd.merge(df_class, df_class2)
# me['total'] = me['math'] + me['eng']
# print(me)


