st_name = ['송지우','심현준', '윤호민']
st_score = [93, 78, 89]

for i in range(len(st_score)):
    if(st_score[i] >= 90):
        grade = 'A'
    elif(st_score[i] >= 80):
        grade = 'B'
    elif(st_score[i] >= 70):
        grade = 'C'
    elif(st_score[i] >= 60):
        grade = 'D'  
    else:
        grade = 'F'
    print('{}님의 학점은 {} 입니다'.format(st_name[i], grade))