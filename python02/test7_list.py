age=[20,30,40]
print(type(age))
print(age[0])

# 몇명인지 모름
age2 = list()
print(type(age2))
age2.append(20)
age2.append(40)
print(age2)

# 내 친구의 이름, 나이, 몸무게
# 리스트로 저장해서 출력
myfriend = ['김유리', 37, 52]
print('현재 내 친구 : {}'.format(myfriend))


mfname = '김유리' # 이름
mfage = 16 # 나이
mfweight = 40 # 몸무게

fnl = []
fal = []
fwl = []

fnl.append(mfname)
fal.append(mfage)
fwl.append(mfweight)

mf = fnl + fal + fwl
print('한희정 - 우리 처음 만난 날? : {}'.format(mf))

mf2name = ['김혜미']
mf2age = [18] # 나이
mf2weight = [45] # 몸무게

mf2 = []
mf2.extend(mf2name)
mf2.extend(mf2age)
mf2.extend(mf2weight)
print('Acoustic Collabo - 설렘 가득 : {}'.format(mf2))