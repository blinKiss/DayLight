# st_name = ['송지우','심현준', '윤호민']
# st_score = [93, 78, 89]

# for i in range(len(st_score)):
#     if(st_score[i] >= 90):
#         grade = 'A'
#     elif(st_score[i] >= 80):
#         grade = 'B'
#     elif(st_score[i] >= 70):
#         grade = 'C'
#     elif(st_score[i] >= 60):
#         grade = 'D'  
#     else:
#         grade = 'F'
#     print('{}님의 학점은 {} 입니다'.format(st_name[i], grade))
    
    
    
st_name = ['송지우','심현준', '윤호민', '이삼사', '마이나', '신짱구']
st_score = [93, 78, 89, 234, -22, 45]

grades = ['F', 'D', 'C', 'B', 'A']
err = '점수는 100 이하의 값이어야 합니다'
for name, score in zip(st_name, st_score):
    if score > 100 or score < 0:
        print('{}님의 점수가 올바르지 않아 학점은 {} 입니다'.format(name, grades[0]))
        continue
    
    if score < 60:
        grade = grades[0]
    else:
        grade = grades[min(score//10 -5, 4)]
    print('{}님의 학점은 {} 입니다'.format(name, grade))
