# import urllib.request
from bs4 import BeautifulSoup
import urllib
import requests
import re

url = 'http://kbsart.co.kr/kr/business/business_list.asp'
res = requests.get(url)
txt_data = res.text

soup = BeautifulSoup(txt_data, 'html.parser')
# soup_temp = []

# for i in range(len(soup.find_all('img'))):
    # soup_temp.append(soup.select('img')[i]['src'])

# print(soup_temp)
# soup_list = soup_temp[3:6]

soup_list = []
for i in range(3, 6):
    soup_list.append(soup.select('img')[i]['src'])


img_save = ['kbs1.jpg', 'kbs2.png', 'kbs3.png']
for j in range(len(soup_list)):
    hangul = re.search('[가-힣]*[가-힣]', soup_list[j]).group()
    encode = urllib.parse.quote(hangul)
    soup_list[j] = re.sub(' ', '%20', re.sub('[가-힣]*[가-힣]', encode, soup_list[j]))
    # print(soup_list[j], img_save[j])
    urllib.request.urlretrieve(soup_list[j], img_save[j])

