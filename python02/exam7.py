# 튜플 1 2 3 4 5 6 7 8
# 1의 값을 0으로 변경
# 마지막에 9를 추가
# 8을 삭제

tu = 1,2,3,4,5,6,7,8
li = list(tu)
print('초기 : {}, 타입 : {}'.format(tu, type(tu)),'\n')
li[0] = 0
tu = tuple(li)
print('1을 0으로 변경한 후 : {}, 타입 : {}'.format(tu, type(tu)),'\n')
li.append(9)
tu = tuple(li)
print('마지막 요소로 9를 추가한 후 : {}, 타입 : {}'.format(tu, type(tu)),'\n')
# li.pop(7)
# del(li[7])
li.remove(8)
tu = tuple(li)
print('8을 삭제한 후 : {}, 타입 : {}'.format(tu, type(tu)),'\n')