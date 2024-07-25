from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time


def scroll_move(scroll_len):
    # 현재 스크롤 좌표 추출
    current_scroll_position = driver.execute_script("return window.pageYOffset")
    print(f"Current scroll position: {current_scroll_position}")
    # 지정 좌표로 스크롤 이동
    driver.execute_script(f"window.scrollTo(0, {current_scroll_position + scroll_len})")
    # 스크롤 후 대기


# 특정 요소가 있는지 확인하는 함수
def check_element_exists(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

def click_title(title_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, title_css_selector)
        element.click()
        time.sleep(0.05)
    except Exception as e:
        print(f"Error: {e}")
    return

def print_content(content_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, content_css_selector).text
        data.append(element)
        print(element)
    except Exception as e:
        print(f"Error: {e}")
    return

def print_titles():
    faq_q_class_name = "cmp-accordion__title"
    faq_a_class_name = "faqinner__wrap"
    titles = driver.find_elements(By.CLASS_NAME, faq_q_class_name)
    # result = check_element_exists(By.CLASS_NAME, faq_a_class_name)
    faq_a_list = driver.find_elements(By.CLASS_NAME, faq_a_class_name)

    num = 0
    for i in titles:
        i.click()
        time.sleep(0.05)
        title = i.text
        col1.append(title)
        print(title)
        num += 1
    
    for i in faq_a_list:
        faq_a = i.text
        col2.append(faq_a)
        print(faq_a)
        num += 1

    time.sleep(0.1)
    print("############ ")
    return

def scroll_down(scroll_len):
    # 현재 스크롤 좌표 추출
    current_scroll_position = driver.execute_script("return window.pageYOffset")
    print(f"Current scroll position: {current_scroll_position}")
    # 지정 좌표로 스크롤 이동
    driver.execute_script(f"window.scrollTo(0, {current_scroll_position + scroll_len})")
    # 스크롤 후 대기
    

# 데이터 저장을 위한 리스트 초기화
data = []

col1 = []
col2 = []

# Selenium 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(960, 1080) 
driver.set_window_position(760,0)

# URL 설정
url = "https://www.kia.com/kr/customer-service/center/faq"
driver.get(url)

# 페이지 로드 대기
driver.implicitly_wait(5)

# FAQ 항목이 나올때 까지 기다림
faq_title = "#accordion-item0-button > span.cmp-accordion__title"
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, faq_title))
    )
    print("FAQ가 로드되었습니다.")
except Exception as e:
    print(f"Error: {e}")
    print("실패")

scroll_down(500)

print_titles()


# 데이터프레임으로 변환
df = pd.DataFrame({'질문': col1,'답변': col2 })

# CSV 파일로 저장
df.to_csv('kia-output.csv', index=False)

time.sleep(300)

# 브라우저 닫기
driver.quit()
