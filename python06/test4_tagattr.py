from bs4 import BeautifulSoup

sample_data = '''
<div id="darkmodemenu"
    class="ws-black"
    onmouseover="mouseoverdarkicon()"
    onmouseout="mouseoutdarkicon()">
    <h2>테스트코드</h2>
</div>
'''


soup = BeautifulSoup(sample_data, 'html.parser')
print(soup.h2)
# h2 전체를 출력
print(soup.h2.string)
# div의 클래스속성 출력
print(soup.div['class'])
# div의 onmouse 출력
print(soup.div['onmouseover'],soup.div['onmouseout'])
# 아이디 출력
print(soup.div['id'])

