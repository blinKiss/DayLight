import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'https://www.naver.com/'
try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    time.sleep(0.1)
    # dict_elem = browser.find_element(By.CSS_SELECTOR, ('.NM_FAVORITE_LIST>li'))
    # print(dict_elem.tag_name)
    dict_elems = browser.find_elements(By.CSS_SELECTOR, ('.NM_FAVORITE_LIST>li'))
    # 첫번째만 가져옴
    dict_elems[0].click()
    time.sleep(5)
except Exception as e:
    print('에러 발생')
finally:
    browser.close