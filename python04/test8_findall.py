import re

# text="1 orange#, 2 apple;, 3 banana, 4 mango"
# 단수형 숫자공백영문자
# m = re.search('\d\s\w+', text)
# print(m.group())
# l = re.findall('\d\s\w+', text)
# print(l)
# for x in l:
#   print(x)

# 문제 1
# text = "사과:apple#자동차:car&&호랑이:tiger**친구:friend"
# 패턴 - 문자:문자

txt1 = "사과:apple#자동차:car&&호랑이:tiger**친구:friend"
# fa = re.findall('[가-힣:a-z]+', txt1)
# fa = re.findall('[가-힣]+:[\w]+', txt1)
fa = re.findall('[\w:\w]+', txt1)
# fa = re.findall('[\w]+:[\w]+', txt1)

# for i in fa:
#     print(i)
# print(fa)

# temp = fa[0]
# word = temp.split(':')
# print(word)

for word in fa:
    temp = word.split(':')
    print(temp)