# 조건문
# 수학점수가 90이상이면 A라고 출력
# 80점 이상이면 B라고 출력
# 70점 이상이면 C라고 출력
# 60점 이상이면 D라고 출력
# 60점 미만이면 F라고 출력

mscore = int(input('수학점수 입력 : '))
grade = ''
print(mscore)
if(mscore >= 90):
    grade = 'A'
elif(mscore >= 80):
    grade = 'B'
elif(mscore >= 70):
    grade = 'C'
elif(mscore >= 60):
    grade = 'D'
else:
    grade = 'F'
    
print('학점 : {}'.format(grade))