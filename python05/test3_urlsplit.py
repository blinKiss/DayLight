import urllib.request
import urllib.parse

URL = 'http://homepage.bluevation.co.kr/shop/list.php?ca_id=10'
result_url = urllib.parse.urlparse(URL)
print(type(result_url))
print(result_url[0]) # 프로토콜 : 통신규약
print(result_url[1]) # 도메인
print(result_url[2]) # path
