import re
# text = "게시판*hello;오라클+spring:빅데이터#취미&뉴스...."
# 패턴 : [단어]
# findall 리스트를 만드시오

text = "게시판*hello;오라클+spring:빅데이터#취미&뉴스...."
fa = re.findall('[\w]+', text)


for i in fa:
    print(i)

print(fa)



text2 = "게시판*hello;오라클+spring:빅데이터#취미&뉴스...."
fa2 = re.findall('[\w]+', text2)
li = []
for i in range(len(fa)):
    add = str(i+1) + '. ' + fa[i].capitalize()
    li.append(add)
print(li)
