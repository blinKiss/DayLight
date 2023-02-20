import pandas as pd

class1_std = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
class1_kor = [90, 65, 35, 45, 100, 80, 60, 75, 100, 95]
class1_math = [95, 75, 25, 55, 95, 85, 70, 60, 90, 90]
class1_eng = [100, 60, 30, 40, 100, 90, 65, 80, 95, 95]
class1_dict = {}
# 남자 1 ~ 끝난 뒤 여자 
# 1~5 남자 6~10 여자
# 남자인 신, 여자인 선이 전학
# 특정 위치에 추가 = insert(n, [값])
# new1 = ['신', 50, 100, 95]
# class1_std.insert(4, (new1[0]))
# class1_kor.insert(4, (new1[1]))
# class1_math.insert(4, (new1[2]))
# class1_eng.insert(4, (new1[3]))
# new2 = ['선', 95, 80, 100]
# class1_std.insert(8, (new2[0]))
# class1_kor.insert(8, (new2[1])) 
# class1_math.insert(8, (new2[2])) 
# class1_eng.insert(8, (new2[3]))
 
# 새 전학생 추가 new뒤에 숫자 변경
new_student = [input('번호 : '), input('이름 : '), input('국어점수 : '), input('수학점수 : '), input('영어점수 : ')]
class1_std.insert(int(new_student[0]), new_student[1])
class1_kor.insert(int(new_student[0]), int(new_student[2])) 
class1_math.insert(int(new_student[0]), int(new_student[3])) 
class1_eng.insert(int(new_student[0]), int(new_student[4]))

# print('2학년 1반 성적')
# for i in range(len(class1_std)):
#     class1_dict[str(i+1) + '번'] = f'이름 : {class1_std[i]}, 국어 : {class1_kor[i]}, 수학 : {class1_math[i]}, 영어 : {class1_eng[i]}'
#     print(class1_dict[f'{i+1}번'])


# for i in range(len(class1_std)):
#     class1_dict = {f'{i+1}번': f'이름 : {class1_std[i]}, 국어 : {class1_kor[i]}, 수학 : {class1_math[i]}, 영어 : {class1_eng[i]}'}
    
class1_dict = {f"{i+1}번": f"이름 : {class1_std[i]}, 국어 : {class1_kor[i]}, 수학 : {class1_math[i]}, 영어 : {class1_eng[i]}" for i in range(len(class1_std))}
for i in class1_dict.values():
    print(i)


class1_dict = {
    '이름' : class1_std,
    '국어점수' : class1_kor,
    '수학점수' : class1_math,
    '영어점수' : class1_eng 
}    
df = pd.DataFrame(class1_dict)
print(class1_dict)