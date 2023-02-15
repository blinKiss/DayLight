import selenium 
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# 마우스오버기능
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.mcdonalds.co.kr/kor/main.do'
# recruit 라는 메뉴를 클릭해서 페이지를 이동하시오

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    
    # elems = browser.find_element(By.CSS_SELECTOR, '.recruit')
    # elems = browser.find_element(By.LINK_TEXT, 'RECRUIT')
    # elems.click()
    
    # 마우스 올려서 펼치기
    div_menu = browser.find_element(By.CLASS_NAME, 'hMenu')
    
    # 서브메뉴
    li_depth_store = browser.find_elements(By.CSS_SELECTOR, ('.depth1 > li'))
    li_depth2_store = li_depth_store[1].find_elements(By.CSS_SELECTOR, ('.depth2 > li'))
    link_macDeliv = li_depth2_store[1]
    time.sleep(2)
    
    action_mouseover = ActionChains(browser)
    action_mouseover.move_to_element(div_menu).perform()
    link_macDeliv.click()
    time.sleep(2)
except Exception as e:
    print('에러 발생')
    
finally:
    browser.close()