import urllib.request
import urllib.parse

URL = 'https://www.nate.com/?f=auto_news'
# 도메인명을 www.naver.com으로 변경 : 튜플 -> 리스트 변경필요
temp = urllib.parse.urlparse(URL)
lt = list(temp)
lt[1] = 'www.naver.com'
result = urllib.parse.urlunparse(lt)
print(result)

