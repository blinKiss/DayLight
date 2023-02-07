import urllib.request

WEB_IMG_URL = 'https://assets.xboxservices.com/assets/e5/4d/e54d4a36-75a4-481d-936d-47956fc448b9.jpg?n=Hogwarts-Legacy_GLP-Page-Hero-1084_1920x1080.jpg'
WEB_HTML_URL = 'https://movie.naver.com/movie/running/current.naver'
# 기본 경로는 파이썬 프로젝트 폴더 // 내 프로젝트명 : DayLight
PC_IMG_SAVE = 'hogwarts.jpg'
PC_HTML_SAVE = 'movie.html'

urllib.request.urlretrieve(WEB_IMG_URL, PC_IMG_SAVE)
urllib.request.urlretrieve(WEB_HTML_URL, PC_HTML_SAVE)
