from bs4 import BeautifulSoup
sample_data = '''
<div class="container d-none d-lg-block">
        <ul class="nav sub-menu pb-3 pt-2">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="../goods/?category=10">안경테</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=11">선글라스</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=12">콘택트렌즈</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../goods/?category=13">기타</a>
            </li>
        </ul>
    </div>
'''
soup = BeautifulSoup(sample_data, 'html.parser')
# find함수
# div태그로 찾기
print(soup.find('div'))
# 클래스 active로 찾기
print(soup.find(class_='active'))

# find_all 함수
# li 태그로 찾기
print(soup.find_all('li'))