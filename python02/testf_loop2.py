# score = 90, 80, 95
# 총합을 구하시오 sum에 저장
score = [90, 80, 95]
sum = 0
for i in range(len(score)):
    sum += score[i]
    
print(sum)

sum2 = 0
for i in score:
    sum2 += i
    
print(sum2)