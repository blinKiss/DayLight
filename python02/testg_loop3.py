# 학생들의 키
# TALL 170.5, 180.6, 174.3
# 평균키를 구하시오
TALL = [170.5, 180.6, 174.3]
sum = 0
for i in TALL:
    sum += i
cnt = len(TALL)
avg = round(sum / cnt, 1)
# print(round(sum/len(TALL), 1))
print(avg)