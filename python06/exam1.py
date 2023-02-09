# 간단한 html 소스를 이용해서 bs로 깔끔하게 출력하기

from bs4 import BeautifulSoup

html_data = '''
<nav id="mobile-bottom-nav" class="navbar fixed-bottom bg-gray-900 px-3 py-3 d-lg-none" style="display:block;">
    <div class="row text-center">
        <div class="col">
            <a href="/shop/index/">
                <span class="d-block h3 text-gray-500 mb-0"><img src="/shop/_images/icons/home.svg"/></span>
                <small class="text-black">홈</small>
            </a>
        </div>
        <div class="col">
            <a href="/shop/goods/category.php">
                <span class="d-block h3 text-gray-500 mb-0"><img src="/shop/_images/icons/category.svg"/></span>
                <small class="text-black">카테고리</small>
            </a>
        </div>
 </div>
</nav>
'''
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())