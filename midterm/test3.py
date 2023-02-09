# URL = 'sample'
# 쇼핑 트렌드 차트 사이트를 웹크롤링해서 순위 1~5위와 이름을 가져와서 데이터를 출력
import re
import requests
URL = 'https://search.shopping.naver.com/best/home?categoryCategoryId=ALL&categoryDemo=A00&categoryRootCategoryId=ALL&chartDemo=A00&chartRank=1&period=P1D&windowCategoryId=20000049&windowDemo=A00&windowRootCategoryId=20000049'

res = requests.get(URL)
html_data = res.text
start = html_data.find('홈')
end = html_data.find('6위 ~ 10위')
st_en = html_data[start:end]
divide = st_en.split('<li data-testid="BEST_ITEM_KEYWORD"')
# print(len(divide))
for i in range(1, len(divide)):
    object_name = re.sub('<.+?>', '', re.search('</em>.*cQZC_">', divide[i]).group())
    print(i, object_name)
