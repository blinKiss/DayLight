# 리스트 변수를 선언해서 학생 3명의 이름, 나이, 점수를 대입해서 각각을 출력하시오
# ex) 이름 = ['김건우', '손의성', '박대용']
#     나이 = 30, 35, 33
#     점수 = 90, 80, 95

name = ['유재석', '정형돈', '노홍철']
age = [52, 46, 45]
score = [98, 92, 88]

# str
print('유 : {},{},{}'.format(name[0],age[0],score[0]))
print('돈 : {},{},{}'.format(name[1],age[1],score[1]))
print('노 : {},{},{}'.format(name[2],age[2],score[2]))

# list
y = list(range(0,3))
d = list(range(0,3))
n = list(range(0,3))
# y = [name[0], age[0], score[0]]
y[0:3] = name[0], age[0], score[0]
# d = [name[1], age[1], score[1]]
d[0:3] = name[1], age[1], score[1]
# n = [name[2], age[2], score[2]]
n[0:3] = name[2], age[2], score[2]


print('{}\n{}\n{}'.format(y,d,n))
print(y,'\n',d,'\n',n) # d앞의 공백을 없애는법은?
print(y,d,n, sep='\n')

# a = y+d+n
# print(a)
