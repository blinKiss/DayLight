# 이벤트 부분 HTML 코드를 출력하고
# 총 이벤트 갯수가 몇개인가?
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.top50glasses.com/shop/event/index#'
res = requests.get(url)
txt_data = res.text
soup = BeautifulSoup(txt_data, 'html.parser')
soupli = soup.find_all('p', class_='card-text text-pd-title h3 crop-text-2')
print(soup)

# for i in soupli:
#     print(i.string,'\n')

print('페이지에 있는 이벤트 갯수는 {}개 입니다'.format(len(soupli)),'\n')

for i in range(0, len(soupli)):
    print('{}.'.format(i+1),soupli[i].string,'\n')


# strsoup = soup.prettify()
# print(strsoup)
# eve = re.compile('[Ee][Vv][Ee][Nn][Tt]')
# print('문자 \'Event(대소문자 구분X)\'의 갯수는 :',len(re.findall(eve, strsoup)))
