import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.ediya.com/'

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    ediyaMenu = browser.find_element(By.CLASS_NAME, 'main') # 자바스크립트 소스 위치
    ediyaSub = browser.find_elements(By.CLASS_NAME, 'sub')
    ediyaBrand = ediyaSub[5].find_elements(By.CSS_SELECTOR, 'a')
    
    mouseover = ActionChains(browser)
    mouseover.move_to_element(ediyaMenu).perform()
    time.sleep(3)
    # ediyaBrand[1].click()
    ediyaBrand[1].send_keys(Keys.ENTER) # 자바스크립트 소스가 걸려있으면 click 대신 Keys로
    time.sleep(2)
    
    
except Exception as e:
    print('에러 내용 : ', str(e))
finally:
    browser.close()

# while(True):
#     pass