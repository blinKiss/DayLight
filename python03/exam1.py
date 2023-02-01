# URL = "http://homepage.bluevation.co.kr"
# reqests 모듈을 사용해서 get으로 링크를 요청하고 성공여부를 출력
import requests
URL = "http://homepage.bluevation.co.kr"
response = requests.get(URL)
if(response.status_code == 200 ):
    print('요청 성공')
else:
    print('요청 실패')