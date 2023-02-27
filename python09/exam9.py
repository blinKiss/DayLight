import pandas as pd

# 데이터형식 name, math-eng-comp
# 김건우, 90-100-80
# 윤호민, 80-70-60
# 손의성, 100-90-80
# 박선호, 80-80-70
# 이석호, 90-90-60

# 열을 분리하고 수학 영어 컴퓨터 합계 평균 분산

df = pd.DataFrame({
    'name' : ['김건우', '윤호민', '손의성', '박선호', '이석호'],
    'scores' : ['90-100-80', '80-70-60', '100-90-80', '80-80-70', '90-90-60']
})


scores = df.scores.str.split('-')
# print(scores)

name = df.name.str.title()
math = pd.to_numeric(scores.str.get(0))
eng = pd.to_numeric(scores.str.get(1))
comp = pd.to_numeric(scores.str.get(2))

# df['Math'] = math
# df['Eng'] = eng
# df['Comp'] = comp
df = df.assign(Math=math, Eng=eng, Comp=comp)
df = df.drop('scores', axis=1)
# print(df)
# print(df['Math'].sum())

student_score = df[['Math', 'Eng', 'Comp']]

for i in range(len(name)):
    sum = student_score.sum(axis=1)[i]
    avg = round(student_score.mean(axis=1)[i])
    var = round(student_score.var(axis=1)[i])
    print(f'{name[i]}님의 3과목 합계 : {sum}, 평균 : {avg}, 분산 : {var}')



