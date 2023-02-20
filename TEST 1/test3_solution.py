import requests
import re

URL = 'https://autobuff.co.kr/1962'
response = requests.get(URL)
html_data = response.text
# print(html_data)

html_figures = html_data.split('<figure class="wp-block-image size-large">')
# print(len(html_figures))
for i in range(len(html_figures)-1):    
    if(i!=4 and i!=5):
        mat = re.search('<h2.*/h2>', html_figures[i])
        html_hp = mat.group()        
    else:
        html_ps = re.findall('<p.*/p>', html_figures[i])
        html_hp = html_ps[1]
    print(re.sub('<.+?>|\(.*\)', '', html_hp))
    # print(re.sub('\(.*\)', '' ,(re.sub('<.+?>', '', html_hp))))
