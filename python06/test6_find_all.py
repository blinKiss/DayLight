from bs4 import BeautifulSoup

sample_data = '''
    <div>
        <p class='color'>빨강</p>
        <p class='color'>빨강</p>
        <p class='bgcolor'>빨강</p>
    </div>    
'''
soup = BeautifulSoup(sample_data, 'html.parser')
# print(soup.find_all('p'))
print(soup.find_all('p', class_='color'))

