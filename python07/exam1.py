import selenium 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

url = 'https://map.kakao.com'

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    # 단수
    # element1 = browser.find_element(By.ID, 'search.keyword')
    # element2 = browser.find_element(By.CLASS_NAME, 'box_searchbar')
    # element3 = browser.find_element(By.CSS_SELECTOR, '.btn_search')
    # element4 = browser.find_element(By.CSS_SELECTOR, '#mapMenus')
    # 복수
    # elems1 = browser.find_elements(By.CLASS_NAME, 'screen_out')
    elems2 = browser.find_elements(By.CSS_SELECTOR, ('.list_option > li'))
    for i in range(6):
        print(elems2[i].get_attribute('innerText'))
    time.sleep(5)

except Exception as e:
    print('에러 발생')
    
finally:
    browser.close