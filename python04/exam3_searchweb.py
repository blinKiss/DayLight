import requests
import re

URL = "https://www.nate.com/?f=news"
res = requests.get(URL)
html_data = res.text
# print(html_data)

# start_idx = html_data.find('<div class="bizCnt">')
# print(html_data[start_idx:start_idx+500])

# 2단계
start_sub = html_data.find('<div class="isKeyword">')
# print(start_sub)
end_sub = html_data.find('<ol class="isKeywordList"')
# print(end_sub)
# print(html_data[start_sub:end_sub])
temp2 = html_data[start_sub:end_sub]
mat = re.search("<h4.*/h4>", temp2)
subject = re.sub('<.+?>', '', mat.group())
# print(subject)

# 3단계
start_key = html_data.find('<div class="isKeyword">')
end_key = html_data.find('<form id="frmKeyword"')
temp3 = html_data[start_key:end_key]

# print(temp3.split('<li>')[0])
Len = len(temp3.split('<li>'))
# print(Len) # 0~5 6개
mat2 = re.search('<span class="num_rank".*/span>', temp3.split('<li>')[1])
num = re.sub('<.+?>', '', mat2.group())
# print(num)

mat3 = re.search('<span class="txt_rank".*/span>', temp3.split('<li>')[2])
txt = re.sub('<.+?>', '', mat3.group())
# print(txt)

# 1~5위 아니면 6~10위
mat4 = re.search('<span class="num_rank".*/span>', temp3.split('<li>')[1]) #[1] = 이 부분이 등수
num2 = re.sub('<.+?>', '', mat4.group())
print('등수 = '+num2)

# li = []
# for i in range(1, Len):
#     add = '{}위 or {}위 : '.format(re.sub('<.+?>', '', re.search('<span class="num_rank".*/span>', temp3.split('<li>')[i]).group())) + (re.sub('<.+?>', '', re.search('<span class="txt_rank".*/span>', temp3.split('<li>')[i]).group()))
#     li.append(add)
    
# for j in li:
#     print(j)

for i in range(1, Len):
    print('{}위 : '.format(re.sub('<.+?>', '', re.search('<span class="num_rank".*/span>', temp3.split('<li>')[i]).group())) + re.sub('<.+?>', '', re.search('<span class="txt_rank".*/span>', temp3.split('<li>')[i]).group()))

for j in range(1, Len):
    rn = re.search('<span class="num_rank".*/span>', temp3.split('<li>')[j]).group()
    cutn = re.sub('<.+?>', '', rn)
    rt = re.search('<span class="txt_rank".*/span>', temp3.split('<li>')[j]).group()
    cutt = re.sub('<.+?>', '', rt)
    dcutn = '{0:02d}'.format(int(cutn))
    print('{}위 : {}'.format(dcutn, cutt))


