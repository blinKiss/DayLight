# for 반복문을 사용하여 1에서 100까지 짝수의 합과 홀수의 합을 각각 출력하시오
oddSum = 0
evenSum = 0

for i in range(1,101):
    if(i%2 == 1):
        oddSum += i
    else:
        evenSum += i

print('홀수의 합은 : {}, 짝수의 합은 : {}'.format(oddSum, evenSum))

li = list(range(1,101))
oddSum2 = 0
evenSum2 = 0
for j in li:
    if(j%2 == 1):
        oddSum2 += j
    else:
        evenSum2 += j
        
print('홀수의 합은 : {}, 짝수의 합은 : {}'.format(oddSum2, evenSum2))
