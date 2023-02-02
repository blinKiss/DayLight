URL = "https://jsonplaceholder.typicode.com/comments"
param = {'postId' : 1}
# request 모듈을 사용해서 get방식으로 요청결과 json() 함수를 써서 dict값을 출력
import requests
res = requests.get(URL, params=param)
if(res.status_code == 200):
    print('요청 성공')
    print(res.json()[0])