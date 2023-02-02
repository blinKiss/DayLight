text = "<title>의류쇼핑몰에 오신 것을 환영합니다</title>"
# 인덱싱을 활용
# 첫번째 글자
# print(text[0])
# print(len(text)) # 마지막 인덱스 = 전체길이-1
# 마지막 글자
# print(text[len(text)-1])

# 반복문 0~9번째 글자 출력
for i in text[0:10]:
    print(i, end='')
    if(i == text[9]):
        print()

    
# 의류쇼핑몰 글자만 출력 : for문으로
for i in text[7:12]:
    print(i, end='')

print()
        
# 선생님 코드
result=""
for x in range(7,12):
    result += text[x]
print(result)