
# 단독 문자열 변수를 3개 만들어서
# orange banana apple 각각 넣어서 출력
# 리스트 변수를 만들어서 각각 출력

o = 'orange'
b = 'banana'
a = 'apple'

print(o + ' ' + b + ' ' + a)

ol = list()
bl = list()
al = list()

ol.append(o)
bl.append(b)
al.append(a)
print(ol)
print(bl)
print(al)

fl = ol + bl + al
print(fl)



l = list()
l.append(o)
l.append(b)
l.append(a)
print(l)

li = list()
li.extend(ol)
li.extend(bl)
li.extend(al)
print(li)