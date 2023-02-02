import requests

# URL = "http://homepage.bluevation.co.kr/shop/introduce_ceo.jsp"
# response = requests.get(URL)
# print(response.status_code)

URL = "https://comic.naver.com/webtoon/detail"
params = { 'titleId' : 805737, 'no' : 2}
response = requests.get(URL, params=params)
if(response.status_code==200):
    print('요청 성공')
else:
    print('요청 실패')