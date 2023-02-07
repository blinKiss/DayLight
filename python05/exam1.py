import urllib.request
# import requests
import re
# re : <[Ii][Mm][Gg]\s+[^>]+>
# 국군의날1.png 추출해서 이미지 다운로드

URL = 'http://kbsart.co.kr/kr/program/program_list.asp'
res = urllib.request.urlopen(URL)

byte_data = res.read()
text_data = byte_data.decode()

start = text_data.find('<div class="set-design-program-con">')
end = text_data.find('<div class="img"><img src="http://kbsart.co.kr/images/content/setdesign_img03.jpg"')
programs = text_data[start:end]
pLength = len(programs.split('<li style="height:300px;">'))
# print(programs)
# new = programs.split('<li style="height:300px;">')[]
# print(new.find('신상'))


for i in range(1, pLength):
    new = programs.split('<li style="height:300px;">')[i]
    if(new.find('신상') != -1):
        break
# print(new)

pattern = 'http.*.jpg'
img_url = re.search(pattern, new).group()
img_url_re = img_url.replace('편스토랑1', '%ED%8E%B8%EC%8A%A4%ED%86%A0%EB%9E%911')
img_save = 'newProduct.jpg'
print(img_url)
urllib.request.urlretrieve(img_url_re, img_save)

# 선생님 답
# text='<div class="img"><img src="http://kbsart.co.kr/data/onlinedata/국군의날 1.png" alt="[행사] 제73주년 국군의 날 이미지"></div>'
# re_img = re.compile("<[Ii][Mm][Gg]\s+[^>]+>", re.MULTILINE) # 간단식 = http.*.png
# img_tag = re_img.findall(text)
# print(img_tag)
# re_img = re.compile("<[Ii][Mm][Gg]\s+[^>]+>")
# img_tag = re_img.findall(text)
# print(img_tag)