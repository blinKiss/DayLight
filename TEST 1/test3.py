import requests
import re

url = 'https://autobuff.co.kr/1962/'

txt_data = requests.get(url).text
temp = txt_data.split('wp-block-image')
rank = re.findall('[0-9]+[가-힣][.][가-힣\s]+[^(]', str(temp))
# print(rank)
rank.sort()
rank.append(rank.pop(0))
for i in rank:
    print(i)
