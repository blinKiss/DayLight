from bs4 import BeautifulSoup
html_data = '''
<div class="container d-none d-lg-block">
    <ul class="nav sub-menu pb-3 pt-2" id="mymenu">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="../goods/?category=10">안경테
                <span>qwdqde</span>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="../goods/?category=11">선글라스</a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="../goods/?category=12">콘택트렌즈</a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="../goods/?category=13">기타</a>
        </li>
    </ul>
</div>
'''

soup = BeautifulSoup(html_data, 'html.parser')
# print(soup.prettify())
# print(soup.select_one('li')) # 태그
# print(soup.select('ul > li')) # 부모 > 자녀
# print(soup.select('ul a')) # A B = A 내부의 태그 B (자녀 손자 모두가능)
# print(soup.select_one('#mymenu')) # #어쩌구 << '어쩌구'란 아이디 찾기 (보통 1개)
# print(soup.select('.nav-link')) # .클래스 << (보통 다수)



