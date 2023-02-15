import selenium 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By # 변경함수때문에

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.naver.com'
    browser.get(url)
    time.sleep(5)
    # 작업한 내용 에러가 생기면
    element = browser.find_element(By.ID, 'account')
    print(element.tag_name)

except Exception as e:
    # 에러 처리 후
    print('에러 발생')
finally:
    browser.close()
    
