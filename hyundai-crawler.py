from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


def check_last_button():
    for i in range(1,8):
        try:
            num = 9-i
            btn_css = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child({num}) > button"
            result = driver.find_element(By.CSS_SELECTOR, btn_css).text
            print(result)
            return  result
        except:
            print(f"{num}페이지가 존재하지 않습니다.")
            continue
    return False

def check_element_exist(by, value):
    try:
        # 특정 클래스가 존재하는지 확인
        element = driver.find_element(by,value)
        print("Element found")
        return True
    except NoSuchElementException:
        print("Element not found")
        return False

def get_faq(last_page):
    print_titles()
    if last_page == 1:
        return
    elif last_page < 6:
        for i in range(1, last_page):
            num = i+1
            click_page_num(num)
            print_titles()
        return
    elif last_page == 6:
        for _ in range(2):
            driver.find_element(By.XPATH, next_button_xpath).click()
            print_titles()
        for i in range(4,last_page):
            click_page_num(i)
            print_titles()
        return
    elif last_page == 7:
        for _ in range(3):
            driver.find_element(By.XPATH, next_button_xpath).click()
            print_titles()
        for i in range(5,last_page):
            click_page_num(i)
            print_titles()
        click_page_num(last_page)
        print_titles()
        return
    elif last_page == 8:
        for _ in range(3):
            driver.find_element(By.XPATH, next_button_xpath).click()
            print_titles()
        for i in range(5,last_page):
            click_page_num(i)
            print_titles()
            if i == 5:
                click_page_num(i)
                print_titles()
        return
    else:
        for _ in range(7):
            driver.find_element(By.XPATH, next_button_xpath).click()
            print_titles()
        for i in range(8,last_page-2):
            click_page_num(5)
            print_titles()
        for i in range(6,8):
            click_page_num(i)
            print_titles()
        return

def click_element(title_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, title_css_selector)
        element.click()
        time.sleep(0.05)
    except Exception as e:
        print(f"Error: {e}")
    return

def click_page_num(num):
    css_selector = f'#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > div > ul > li:nth-child({num}) > button'
    try:
        driver.find_element(By.CSS_SELECTOR, css_selector).click()
        time.sleep(0.1)
    except:
        return
    return


def print_titles():
    class_name = "list-content"
    content_css_selector = "#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.list-wrap > div > div > div"
    titles = driver.find_elements(By.CLASS_NAME, class_name)
    num = 0
    for i in titles:
        title = i.text
        col1.append(cate_css)
        col2.append(title)
        print(title)
        num += 1
        title_css_selector = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.list-wrap > div:nth-child({num}) > button > div > span.list-content"
        click_element(title_css_selector)
        print_content(content_css_selector)
        click_element(title_css_selector)
    time.sleep(0.1)
    print("############ ")
    return

def print_content(content_css_selector):
    try:
        element = driver.find_element(By.CSS_SELECTOR, content_css_selector).text
        col3.append(element)
        print(element)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    except Exception as e:
        print(f"Error: {e}")
    return


def scroll_move(scroll_len):
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
col3 = []

# Selenium 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(960, 1080) 
driver.set_window_position(660,0)

# URL 설정
url = "https://www.hyundai.com/kr/ko/e/customer/center/faq"
driver.get(url)

# 다음 페이지 버튼의 xpath설정
next_button_xpath = '//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/button[3]'

# 페이지 로드 대기
driver.implicitly_wait(5)

scroll_move(1150)
time.sleep(2)

cate_css_first = "#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(1) > div.tab-menu > ul > li.tab-menu__icon.active > button > span"
cate_css_first_text = driver.find_element(By.CSS_SELECTOR, cate_css_first).text
last_page_num = int(check_last_button())

cate_css = cate_css_first_text
get_faq(last_page_num)

for i in range(2,10):
    num = i
    cate_css = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(1) > div.tab-menu > ul > li:nth-child({num}) > button"
    cate_css_text = driver.find_element(By.CSS_SELECTOR, cate_css).text

    scroll_move(-300)
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, cate_css).click()
    except:
        print("요소가 존재하지 않습니다.")
    
    # 8번째 카테고리에서 버그가 있어서 9번째 카테고리를 클릭
    if num == 8:
        try:
            num = 9
            cate_css_temp = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(1) > div.tab-menu > ul > li:nth-child({num}) > button"
            driver.find_element(By.CSS_SELECTOR, cate_css_temp).click()
            time.sleep(1)
            num = 8
            cate_css_temp = f"#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(1) > div.tab-menu > ul > li:nth-child({num}) > button"
            driver.find_element(By.CSS_SELECTOR, cate_css_temp).click()
            time.sleep(1)
        except:
            print("요소가 존재하지 않습니다.")

    scroll_move(300)
    time.sleep(0.5)
    
    # 페이지를 제일 처음으로 이동
    navi_css = '#app > div.contant-area > section > div.l-container-body > div > div.l-contents-mid > section > div > div:nth-child(3) > div.pagenation.pagenation > button.btn.btn-prevall.ative'
    try:
        driver.find_element(By.CSS_SELECTOR, navi_css).click()
    except:
        print("페이지가 첫페이지 입니다.")

    last_page_num = int(check_last_button())

    cate_css = cate_css_text
    get_faq(last_page_num)


# 데이터프레임으로 변환
df = pd.DataFrame({'카테고리': col1, '질문': col2,'답변': col3 })

# CSV 파일로 저장
df.to_csv('hyundai-output.csv', index=False)

# 브라우저 닫기
driver.quit()
