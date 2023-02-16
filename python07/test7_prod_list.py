import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url = 'https://ediyastore.com/index.html'

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    
    ediShop_menu = browser.find_elements(By.CLASS_NAME, 'xans-record-')
    ediShop_menu[1].click()

    html_src = browser.page_source

    # bs4 모듈을 사용해서 가져옵니다
    soup = BeautifulSoup(html_src, 'html.parser')
    # print(soup.prettify())
    prod_list = soup.select('.prdList .name')
    prod_temp = soup.select('.xans-product-listitem span')
    # print(prod_temp)
    prod_price = prod_temp[1:len(prod_temp):3]
    # print(prod_price)
    for i in range(len(prod_list)):
        print(f'{prod_list[i].get_text()}, 가격 : {prod_price[i].get_text()}')
    time.sleep(2)
except Exception as e:
    print('에러 내용 : ', str(e))
finally:
    browser.close()
