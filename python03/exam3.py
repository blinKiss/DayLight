# url = "https://www.ajou.ac.kr/kr/ajou/notice.do?mode=view&articleNo=210213&article.offset=0&articleLimit=10"
# params 복수의 dict()만들어서
# requests 모듈을 사용해서 get방식으로 요청결과 text를 출력하시오

import requests

URL = "https://www.ajou.ac.kr/kr/ajou/notice.do"
params = { 'mode' : 'view', 
           'articleNo' : 210213, 
           'article.offset' : 0, 
           'articleLimit' : 10
        }
response = requests.get(URL, params=params)
if(response.status_code==200):
    print("요청 성공")
    print(response.text)
else:
    print('요청 실패')
