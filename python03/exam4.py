import requests

URL = "https://jsonplaceholder.typicode.com/comments"
# requests 모듈을 사용해서 get방식으로 요청결과 json()함수를 써서 dict값을 출력

response = requests.get(URL)
li = []
if(response.status_code == 200):
    print('요청 성공')
    li = response.json()
print(li[0])