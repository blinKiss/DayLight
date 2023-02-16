# 리스트 국어점수 90 60 70 80 100 60 70 80 90 60
# 시리즈를 사용해서 합계를 구하고 총 갯수를 출력
# 리스트는 반복문이 가능하므로 반복문으로 합계를 구하시오
import pandas as pd

korean = pd.Series([90, 60, 70, 80, 100, 60, 70, 80, 90, 60])
print('국어점수 평균 :', korean.mean())
print('국어점수 갯수 :', korean.size)
sum = 0
for i in korean:
    sum += i
print('국어점수 합계 :', sum)