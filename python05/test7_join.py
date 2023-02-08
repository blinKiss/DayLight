import urllib.request
import urllib.parse

URL = 'https://www.nate.com/aaa/bbb'

parse = urllib.parse.urlparse(URL)
print(parse)
newURL = urllib.parse.urljoin(URL+'/', 'ccc')
# 앞의 path에 / 가 없다면 마지막 path가 치환
# 앞의 path에 / 가 있다면 유지한채로 결합
print(newURL)

newURL2 = urllib.parse.urljoin(URL, '/ccc')
# path 앞에 / 를 붙이면 루트라는 의미
# path 앞에 ./ 를 붙이면 현재 path 라는 의미
# path 앞에 ../ 를 붙이면 상위 path 라는 의미

print(newURL2)
