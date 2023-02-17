import requests
import re

url = 'https://autobuff.co.kr/1962/'

res = requests.get(url)
txt_data = res.text
start_rank = txt_data.find('<div class="post-content">')
end_rank = txt_data.find('src="https://i0.wp.com/autobuff.co.kr/wp-content/uploads/2022/11/포터_2_일렉트릭')
temp = txt_data[start_rank:end_rank]
# rankh2 = re.findall('<h2.*/h2>', temp)
# rankp = re.findall('<p.*/p>', temp)
rank = re.findall('[0-9]+[가-힣][.].*[(]', temp)
# print(rank)
for i in rank:
    print(re.sub('[(]', '', i))




