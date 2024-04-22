# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory)
                           , options=chrome_options)



# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
# mongoClient = MongoClient("mongodb://192.168.10.10:27017")
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["polaris_get"]
# collection 작업
news_get = database['share_contents']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By

url = 'https://www.polarishare.com/new'

browser.get(url)
time.sleep(2)

element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')

# main_window_handle = browser.current_window_handle # 초기 창 핸들로 저장

contents_list = browser.find_elements(by=By.CSS_SELECTOR,value='#COMMON__CONTENT > div > div.common__body > div > div > div > div')

for element in contents_list:
    content = element.find_element(by=By.CSS_SELECTOR,value='div')
    content.click()

    element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')
    
    title = element_body.find_element(by=By.CSS_SELECTOR,value='#CONTAINER > section > article.detail_page__details > h1')
    print(title)
    break