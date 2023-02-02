# find : 해당 문자가 없으면 -1
# index : 해당 문자가 없으면 에러
text = "<title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>"
print(text.find('의')) # [0] ~ 처음찾은 것을 표시 = [7](에 있다)
print(text.find('손')) # 결과값 = -1(없다)
print(text.find('메인')) # [14] = 찾은 첫 글자가 [14]에 있음

print(text.index('의'))
# print(text.index('손')) # 에러가 생기면 멈춘다
print(text.index('메인'))

