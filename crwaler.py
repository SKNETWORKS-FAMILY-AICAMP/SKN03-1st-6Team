import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time


def click_title(title_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, title_css_selector)
        element.click()
        print("Element clicked successfully")
        time.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")
    return

def print_content(content_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, content_css_selector).text
        print(element)
    except Exception as e:
        print(f"Error: {e}")
    return

# 특정 요소가 있는지 확인하는 함수
def check_element_exists(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
    
def print_titles():
    class_name = "list-content"
    content_css_selector = "#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.list-wrap > div > div > div"
    titles = driver.find_elements(By.CLASS_NAME, class_name)
    num = 0
    for i in titles:
        title = i.text
        print(title)
        num += 1
        title_css_selector = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.list-wrap > div:nth-child({num}) > button > div > span.list-content"
        click_title(title_css_selector)
        print_content(content_css_selector)
        click_title(title_css_selector)
    time.sleep(1)
    print("############ ")
    return

def scroll_down():
    # 현재 스크롤 좌표 추출
    current_scroll_position = driver.execute_script("return window.pageYOffset")
    print(f"Current scroll position: {current_scroll_position}")
    # 지정 좌표로 스크롤 이동
    driver.execute_script(f"window.scrollTo(0, {current_scroll_position + 1150})")
    # 스크롤 후 대기
    


# Selenium 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(960, 1080) 
driver.set_window_position(760,0)

# URL 설정
url = "https://www.hyundai.com/kr/ko/e/customer/center/faq"
driver.get(url)

# 다음 페이지 버튼의 xpath설정
next_button_xpath = '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/button[3]'

# 페이지 로드 대기
driver.implicitly_wait(5)

# BeautifulSoup을 사용하여 페이지 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')

# soup 내용을 HTML 파일로 저장
with open("faq_page.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

scroll_down()
time.sleep(3)
print_titles()


while True:
    #xpath를 이용한 click
    for _ in range(3):
        driver.find_element(By.XPATH, next_button_xpath).click()
        time.sleep(0.1)
        print_titles()

    #xpath 3회 이후, 5, 5, 6, 7을 셀렉터로 클릭해야함. 
    css_selector = '#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child(5) > button'
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    time.sleep(0.1)
    print_titles()

    css_selector = '#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child(5) > button'
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    time.sleep(0.1)
    print_titles()

    css_selector = '#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child(6) > button'
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    time.sleep(0.1)
    print_titles()

    css_selector = '#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child(7) > button'
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    time.sleep(0.1)
    print_titles()

    
    time.sleep(200)

# 브라우저 닫기
driver.quit()
