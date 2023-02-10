from bs4 import BeautifulSoup

sample_data = '''
    <a href="https://www.w3schools.com" class="w3-bar-item w3-button w3-hover-none w3-left w3-padding-16" title="Home" style="width:77px">
        <i id='demo' style="position:relative;font-size:42px!important;"></i>
        <i id='demo2' style="position:relative;font-size:42px!important;"></i>
    </a>
'''

soup = BeautifulSoup(sample_data, 'html.parser')
print(soup.find('a'),'\n') # 태그만 사용
print(soup.find(class_='w3-bar-item'),'\n') # 속성만 사용

print(soup.find('i', id='demo2'))


