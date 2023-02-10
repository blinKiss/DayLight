from bs4 import BeautifulSoup

html_data = '''
<ul>
    <li class="first"><a href="../board/view.php?bdId=notice&sno=11">[NOTICE]&nbsp;2023 설 연휴 고객센터 ...</a></li>
    <li id="demo" class="second"><a href="../board/view.php?bdId=notice&sno=10">[NOTICE]&nbsp;2023.01.02~04 배...</a></li>
    <li class="third"><a href="../board/view.php?bdId=notice&sno=9">[NOTICE]&nbsp;쏠초 프라이데이 이벤트 안내</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=8">[NOTICE]&nbsp;카카오톡 고객상담 불가 안내</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=7">[NOTICE]&nbsp;추석 연휴 배송 일정 안내</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=6">[NOTICE]&nbsp;배송비 인상 안내 (9월부터...</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=5">[NOTICE]&nbsp;💡 교환 반품 안내</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=4">[NOTICE]&nbsp;롯데택배 파업 배송지연 지역...</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=3">[NOTICE]&nbsp;솔트앤초콜릿 회원만 누릴 수...</a></li>
    <li><a href="../board/view.php?bdId=notice&sno=2">[NOTICE]&nbsp;(시행일자 : 2021.02...</a></li>
</ul>
'''

soup = BeautifulSoup(html_data, 'html.parser')
print(soup.li)
print(soup.li['class'])
soup.li['class'] = 'test'

print(soup.a)
print(soup.a['href'])

