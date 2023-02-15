import pandas as pd
s = pd.Series([90, 60, 80, 70])
# print(s)

# 160 ~ 190 사이 값으로 아무거나 넣어서 출력
s_tall = pd.Series([183.2, 178.8, 170.4, 185.0])
# print(s_tall.values) # index, .dtype 등

# 사전 집합 자료와 호환
# 온도
s_temp = pd.Series([10, 5, 9, 7], index = ['Sun', 'Mon', 'Tue', 'Wed'])
# print(s_temp)
# 습도 : 실수 10.0 ~ 70.0 사이로(일 ~ 수)
s_hum = pd.Series([52.4, 33.8, 36.5, 19.2], index = ['Sun', 'Mon', 'Tue', 'Wed'])
# print(s_hum)
# 미세먼지
s_dust = pd.Series({'Sun' : 60, 'Mon' : 30, 'Tue' : 100, 'Wed' : 70})
# print(s_dust)

# 길이 얼마?
# print(s.size)
# 상품명 (과일 7개)
s_prod_list = pd.Series(['포도', '딸기', '파인애플', '오렌지', '배', '체리', '수박'])
print(s_prod_list.size)