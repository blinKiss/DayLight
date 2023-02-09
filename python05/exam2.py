# Daum 에서 파이썬 검색 결과페이지를 urllib.request.urlopen 으로 열어서
# 키워드 = python 이라는 단어를 찾아서 출력
# 다음은 막혀서 야후로 대체

import re
import urllib.request

URL = 'https://search.yahoo.com/search?p='
query = urllib.parse.quote('파이썬')
newURL = URL + query
keyword = 'python'

req = urllib.request.Request(newURL, headers = {'User-agent' :'Mozilla/5.0'})
res = urllib.request.urlopen(req)
text_data = res.read().decode()
# print(text_data)
pickKeyword = re.findall(keyword, text_data)
print('뽑기 : {}\n갯수 : {}개'.format(pickKeyword, len(pickKeyword)))
# 출력값 안나와서 임의의 문자열로 대체
# txt = '<span class="wsn"><a href="?w=tot&m=&q=python&nzq=%ED%8C%8C%EC%9D%B4%EC%8D%AC&DA=NSJ" class="keyword" data-log="dc=NSJ&pg=1&r=12&p=1&e1=python&rc=1">python</a></span>'
# print(re.findall(keyword, txt))


