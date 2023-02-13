import selenium
from selenium import webdriver
import time

driver_path = 'C:/god\Download/chromedriver_win32/chromedriver'
browser = webdriver.Chrome(driver_path)

browser.get('https://www.naver.com')
time.sleep(5)