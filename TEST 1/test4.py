from bs4 import BeautifulSoup
import requests

url = "https://euler.synap.co.kr/problem=1"
res = requests.get(url)
txt_data = res.text
soup = BeautifulSoup(txt_data, 'html.parser')
problem = soup.find_all('p')[1]
div3 = 0
div5 = 0
for i in range(1, 1000):
    if(i % 3 == 0):
        div3 += i
    if(i % 5 == 0):
        div5 += i
answer = div3 + div5
print('문제 : {}\n정답 : {}'.format(problem.string, answer))

