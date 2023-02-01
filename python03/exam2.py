# URL = "https://www.google.com/search?"
# param = q=machine
# requests 모듈을 사용해서 get방식으로 요청결과를 text로 출력

import requests
URL = "https://www.google.com/search"
param = { 'q' : 'machine'}
response = requests.get(URL, param)
print(response.text)
