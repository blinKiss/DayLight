import selenium 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

url = 'https://map.kakao.com'

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    element = browser.find_element(By.ID, 'search.keyword')
    print(element.tag_name)
    time.sleep(5)

except Exception as e:
    print('에러 발생')
    
finally:
    browser.close