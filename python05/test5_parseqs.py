import urllib.request
import urllib.parse

URL = "https://prod.danawa.com/info/?pcode=17033585&cate=112758"
parse = urllib.parse.urlparse(URL)
# print(parse)
query = parse[4]
QS_DICT = urllib.parse.parse_qs(query) # 사전 형식으로 반환
print(QS_DICT['pcode'])
QS_DICT['pcode'] = ['11115555'] # 변경이 가능
# print(QS_DICT['pcode']) # 확인

# 리스트형식으로 반환 // 잘 쓰이지않음
# QS_LIST = urllib.parse.parse_qsl(query)
# print(QS_LIST)