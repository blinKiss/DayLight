num = 10
if(num%2==0):
    print('짝수')
else:
    print('홀수')

# 임의의 숫자 양수, 0 음수
num2 = int(input('정수 입력 : '))
result = ''
print(num2)
if(num2 > 0):
    result = '양수'
elif(num2 < 0):
    result = '음수'
else:
    result = '정수 0'
    
print('입력한 값은 {}'.format(result))

