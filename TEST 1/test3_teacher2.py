import requests
import re

URL = "https://autobuff.co.kr/1962/"

response = requests.get(URL) 
html_data = response.text
# print(html_data)

# 2022년 10월, 국산차 판매량 순위 TOP 10 출력
start_key = html_data.find('<header class="post-header">')
end_key = html_data.find('</header>')
temp = html_data[start_key:end_key]
# print(temp)
mat = re.search("<h1.*/h1>", temp)
subject = re.sub("<.+?>", "", mat.group())
print(subject)

# 순위, 이름 출력
start_key2 = html_data.find('<div class="post-content">')
end_key2 = html_data.find('<p>6위. 기아 스포티지(4,950대)</p>')
temp2 = html_data[start_key2:end_key2]
# print(temp2)
LENGTH = len(temp2.split('<h2>'))
# print(LENGTH)

print('등수')

for h in range(1, LENGTH):
    
    mat = re.search('<h2>.*</h2>', 
    temp2.split('<p>')[h])
    txt = re.sub('<.+?>', '', mat.group())
    print(txt)
    
start_key3 = html_data.find('="" class="wp-image-1967')
end_key3 = html_data.find(' (adsbygoogle = wind')
temp3 = html_data[start_key3:end_key3]
# print(temp3)
LENGTH2 = len(temp3.split('.</p>'))
# print(LENGTH2)

for p in range(1, LENGTH2):

    mat = re.search('<p>.*</p>', 
    temp3.split('.</p>')[p])
    txt = re.sub('<.+?>', '', mat.group())
    print(txt)
    
start_key4 = html_data.find('d-slot="5612075361')
end_key4 = html_data.find('<p>오토버프(knh@autobu')
temp4 = html_data[start_key4:end_key4]
# print(temp4)
LENGTH4 = len(temp4.split('<h2>'))
# print(LENGTH4)

for h2 in range(1, LENGTH4):
    
    mat = re.search('<h2>.*</h2>', 
    temp4.split('<figure class')[h2])
    txt = re.sub('<.+?>', '', mat.group())
    print(txt)