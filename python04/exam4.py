import requests
import re
URL = "https://datalab.naver.com/"
# 2월 5일자 패션의류 인기분야 1~10위 출력
# 1 html_data 가져오기
# 2 타이틀에 대한 패턴 찾기

res = requests.get(URL)
html_data = res.text
# print(html_data)

# 2단계
start_title = html_data.find('<a href="#" class="select_btn">패션의류</a>')
temp1 = html_data[start_title:start_title+50]
mat = re.search('<a.*/a>', temp1)
title = re.sub('<.+?>', '', mat.group())


start_data = html_data.find('<div class="keyword_carousel">')
end_data = html_data.find('<div class="keyword_notice">')
temp2 = html_data[start_data:end_data]
latest = temp2.split('<div class="keyword_rank">')[-1]
print(latest)
Len = len(latest.split('<li class="list">'))
# print(Len)
latestDay = re.sub('<.+?>', '', re.search('<span class="title_cell".*/span>', latest.split('<strong class="rank_title".*/strong>')[0]).group())
print('{}\n인기분야 : {}'.format(latestDay, title))

for i in range(1,Len):
    rank_num = re.sub('<.+?>', '', re.search('<em class="num".*/em>', latest.split('<li class="list">')[i]).group())
    object_name = re.sub('<.+?>', '', re.search('<span class="title".*/span>', latest.split('<li class="list">')[i]).group())
    print('{}위\t : {}'.format('{0:02}'.format(int(rank_num)), object_name))




