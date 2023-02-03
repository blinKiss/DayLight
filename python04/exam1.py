import re

text1 = "##s13579##4abcd##ss123"
text2 = "###w13579"
# 패턴 = 문자 + 숫자5개
# 찾아서 출력하기
p = re.search('\w\d{5}', text1)
pa = re.search('\w\d{5}', text2)
print('문자 + 숫자5개만 출력\ntext1 : {}, 타입 : {}\ntext2 : {}, 타입 : {}'.format(p.group(),type(p.group()),pa.group(), type(pa.group())),'\n')

# 병합 후 문자 + 숫자5개
txt12 = text1 + text2
pl = re.findall('\w\d{5}', txt12)
print('문자열 병합 후 추출 : {}, 타입 : {}'.format(pl, type(pl)),'\n')

txtplus = '##'
text2 += txtplus # text2 = ###w13579##
# text1,2 의 영어 소문자, 숫자만 출력
m, n = re.findall('[a-z0-9]+', text1), re.search('[^#]+', text2) #\w+\d+, \w\d+
print('문자열 내의 영어 소문자와 숫자만 출력\ntext : {}, 타입 : {}\ntext2 : {}, 타입 : {}'.format(m, type(m), n.group(), type(n.group())),'\n')

# 문자열로 변환
strm = ' '.join(m).capitalize()
print('text를 list에서 str로 변환 : {}, 타입 : {}'.format(strm, type(strm)),'\n')


# 할거없다
text3 = "#김1##2lee###3박####choi4#####5정######"
text4 = text3.replace('정', '신')
o = re.sub('[#]+',' ', text4).title() 
print('문자열 내의 문자를 변환 : {}, 타입 : {}'.format(o.lstrip(), type(o)))

