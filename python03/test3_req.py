# requests 요청
import requests

# URL = "https://naver.com"
# response = requests.get(URL)
# print(response.status_code)
# print(response.text)

# https://search.naver.com/search.naver?

URL = "https://search.naver.com/search.naver"
param = { 'query' : 'bigdata'}
response = requests.get(URL, param)
print(response.status_code)
print(response.text)