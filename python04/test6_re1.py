import re

text = '1111<head>안녕하세요</head>2222'
# <head>안녕하세요</head>
# re.search(정규식, 검색할 문자열)
m = re.search('<head.*/head>', text) # match 객체 none
print(m.group())

text2 = "###event result###"
# evenet result
n = re.search('[a-z]*\s[a-z]*', text2)
print(n.group())

text3 = "david,010-3333-9999,test"
# 010-3333-9999를 추출하여 출력
o = re.search('\d{2,3}-[0-9]{4}-\d{4}', text3)
print(o.group())


