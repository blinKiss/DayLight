import requests
from bs4 import BeautifulSoup

# html data 가져오기
url = 'https://rounz.com/home.php'
res = requests.get(url)
html_data = ''
if(res.status_code == 200):
    html_data = res.text
# print(html_data.find('지금 가장 핫한 상품'))
soup = BeautifulSoup(html_data, 'html.parser')
# print(type(soup))
# print(soup.title)
# print(type(soup.head))

