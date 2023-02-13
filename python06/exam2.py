# URL = 'https://www.top50glasses.com/shop/index/'
# 타이틀 제목을 출력하시오

import requests
from bs4 import BeautifulSoup
URL = 'https://www.top50glasses.com/shop/index/'
res = requests.get(URL)
html_data = res.text
soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.title)
print(soup.title.string)