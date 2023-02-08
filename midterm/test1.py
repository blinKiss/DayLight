# 1 영어점수 = 75
# 90이상 학점 A
# 90~94 A 아니면 95이상이면 A+ ~
# 60이상 학점 D
# 60~64 D 65이상 D+
# 나머지 F
score = int(input('점수를 입력하세요 : '))
grade = ''

if(score >= 90):
    if(score >= 95):
        grade = 'A+'
    else:
        grade = 'A'
elif(score >= 80):
    if(score >= 85):
        grade = 'B+'
    else:
        grade = 'B'
elif(score >= 70):
    if(score >= 75):
        grade = 'C+'
    else:
        grade = 'C' 
elif(score >= 60):
    if(score >= 65):
        grade = 'D+'
    else:
        grade = 'D'  
else:
    grade = 'D'
    

print('당신의 학점은 {} 입니다'.format(grade))