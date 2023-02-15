import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.naver.com'
    browser.get(url)
    time.sleep(5)
    # 작업한 내용 에러가 생기면
    
except Exception as e:
    # 에러 처리 후
    print('에러 발생')
finally:
    browser.close()
    
