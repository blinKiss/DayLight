import re
# 1번
#text3 = "david,010-3333-9999,test"
# o = re.search('\d{2,3}-[0-9]{4}-\d{4}', text3)
# print(o.group())

# 2번
# 패턴을 바꾸면서 사용시 편리하게
text = "david,010-3333-9999,test"
text2 = "david,010-4444-6666,test"
text3 = "david,010-1234-5678,test"
setting = re.compile('\d{2,3}-\d{4}-\d{4}')


m = setting.search(text)
n = setting.search(text2)
o = setting.search(text3)
print('2-1번의 결과 :',m.group())
print('2-2번의 결과 :',n.group())
print('2-3번의 결과 :',o.group())
