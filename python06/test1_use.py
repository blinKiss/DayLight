from bs4 import BeautifulSoup

# 객체지향으로 인스턴스변수를 선언
html_data = '<head><title>홈페이지</title></head>'  #requests 가져온 데이터
soup = BeautifulSoup(html_data, 'html.parser')
# print(html_data)
print(soup.prettify())