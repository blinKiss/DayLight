import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
res = requests.get(url)
# print(res.status_code) #200
html_data = res.text
# print(html_data)
# print(html_data.find('바빌론')) # 위치값 13227

soup = BeautifulSoup(html_data, 'html.parser')
rank_list = soup.find_all('td', class_='title')
print(rank_list)

for i in range(10):
    print(str(i+1), '위 :', rank_list[i].get_text().strip())  