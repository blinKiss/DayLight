import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.naver.com'
browser.get(url)
time.sleep(5)