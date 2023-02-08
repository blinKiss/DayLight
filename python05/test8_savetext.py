import urllib.request

URL = 'https://cheese10yun.github.io/'
res = urllib.request.urlopen(URL)
byte_data = res.read() 
# print(byte_data) # 바이너리 데이터
f = open('blog.html', 'wb')
f.write(byte_data)
f.close