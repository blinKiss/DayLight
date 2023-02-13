# import urllib.request
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import requests
import re

url = 'http://kbsart.co.kr/kr/business/business_list.asp'
res = requests.get(url)
txt_data = res.text

soup = BeautifulSoup(txt_data, 'html.parser')

soup_list = []
for i in range(3, 6):
    soup_list.append(soup.select('img')[i]['src'])


img_save = ['kbs1.jpg', 'kbs2.png', 'kbs3.png']
for j in range(len(soup_list)):
    par = urllib.parse.urlparse(soup_list[j])
    # print(par)
    new_path = urllib.parse.quote(par.path)
    imgsrc = list(par)
    imgsrc[2] = new_path
    unpar = urllib.parse.urlunparse(imgsrc)
    # print(unpar, img_save[j])
    urllib.request.urlretrieve(soup_list[j], img_save[j])

