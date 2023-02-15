import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = 'https://www.mcdonalds.co.kr/kor/main.do'
try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    time.sleep(1)
    mcSearch = browser.find_element(By.CLASS_NAME, 'topSearch')
    mcQuery = browser.find_element(By.ID, 'commonSearchWord')
    mcClick = browser.find_elements(By.CLASS_NAME, 'btnMC')
    # mcClick = browser.find_element(By.CSS_SELECTOR, '.topSearch .btnMC')
    
    mcSearch.click()
    time.sleep(1)
    mcQuery.send_keys('영등포')
    time.sleep(1)
    mcClick[0].click()
    
    time.sleep(5)
except Exception as e:
    print('에러 내용 : ', str(e))
finally:
    browser.close()