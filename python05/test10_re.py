import re
import urllib.request

URL = 'http://search.naver.com/search.naver?query='
query = 'python'
keyword = '파이썬'
keyword2 = '직군별'
keyword3 = '개발자'
newURL = URL + query

req = urllib.request.Request(newURL)
res = urllib.request.urlopen(req)
text_data = res.read().decode() # 보안으로 막히지 않음
# print(text_data)
# print(text_data.find(keyword))
result_keyword = text_data.split(keyword)[1]
# print(result_keyword.find('직군별'))
result_keyword2 = result_keyword.split(keyword2)[0]
# print(result_keyword2)
result_keyword3 = result_keyword.split(keyword3)[1]
# print(result_keyword3) # 일부분의 html 태그


# 정규식
result_sub = re.sub('<.+>', '', result_keyword3)
result_final = result_sub.replace('  ', ' ').strip()
# print(result_final)
f = open('python05/sample.txt', 'w', encoding = 'UTF-8') # 한글깨짐 방지
f.write(result_final)
f.close()