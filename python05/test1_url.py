# 파이썬 2 까지는 import urllib
# 파이썬 3 부터는
import urllib.request

URL = "https://www.naver.com"
req = urllib.request.Request(URL)
# print(req)

# 주소를 열어 통신함
res1 = urllib.request.urlopen(URL)
# print(res1)

byte_data = res1.read(1000)
text_data = byte_data.decode()

# print(res1.read().decode('utf-8'))

# res2 = urllib.request.urlopen(req)
# print(res2)







