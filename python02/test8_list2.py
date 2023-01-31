L = [1,2,3,4,5,6,7,8,9]
print(L[0:4])
print(len(L))
print(L[4:len(L)])
# 홀수번째 값을 10으로 수정
L[0] = 10
L[2] = 10
L[4] = 10
L[6] = 10
L[8] = 10

print('홀수번째 값을 하나 하나 10으로 수정 :', L)
L.append(11) # 마지막 배열에 추가
print('마지막 배열에 11이란 값 추가 :', L)


# 짝수번째 값을 Even으로 수정
li = [1,2,3,4,5,6,7,8,9]
for i in range(len(li)):
    if i%2 == 1:
        li[i] = 'Even'

print('반복문으로 짝수번째 값을 Even으로 수정한 결과 :', li)
