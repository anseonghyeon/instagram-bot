from selenium import webdriver # 크롬 웹 드라이버 구동
from selenium.webdriver.common.keys import Keys # 엔터, 컨트롤 등 키 입력
from selenium.webdriver.common.by import By # 웹 요소를 찾을 때 기준이 되는 요소 호출
from selenium.common.exceptions import NoSuchElementException # 오류 정의 및 호출
import time # 웹페이지가 로딩되는 동안 기다리는 시간을 설정
import random # 로봇으로 인식되는 것을 방지하기 위해 시간을 랜덤으로 눌러줌

options = webdriver.ChromeOptions()

# 크롬 드라이버로 인스타에 접속했을 때 모바일 환경으로 인식하도록 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25')
options.add_argument("--start-maximized")

# 인스타그램으로 접속하는 코드
driver = webdriver.Chrome('chromedriver', options=options)
driver.get('https://instagram.com')
driver.implicitly_wait(15)
print('로그인 진행중...')
# 로그인 클릭
btn= driver.find_elements(By.TAG_NAME,'button')[1]
btn.click()
# 아이디 입력
inputbox = driver.find_elements(By.TAG_NAME,'input')[0]
inputbox.click()
inputbox.send_keys('anseonghyeon@naver.com')
# 비밀번호 입력
inputbox = driver.find_elements(By.TAG_NAME,'input')[1]
inputbox.click()
inputbox.send_keys('ash0927@')
# 엔터 입력
inputbox.send_keys(Keys.ENTER)
time.sleep(10)

# 잡다한거 패스하기
inputbox = driver.find_elements(By.TAG_NAME,'button')
for s in inputbox:
    if s.get_attribute('class') == "_acan _acao _acas _aj1-":
        s.click()
        driver.refresh()
        time.sleep(4)
        

inputbox = driver.find_elements(By.TAG_NAME,'button')
for s in inputbox:
    if s.get_attribute('class') == "_a9-- _a9_1":
        s.click()
        driver.refresh()
        time.sleep(4)

inputbox = driver.find_elements(By.TAG_NAME,'button')
for s in inputbox:
    if s.get_attribute('class') == "_a9-- _a9_1":
        s.click()
        time.sleep(4)

# 좋아요 클릭
while True:
    span = driver.find_element(By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]')
    like_btn = span.find_element(By.TAG_NAME, 'button')
    btn_svg = like_btn.find_element(By.TAG_NAME, 'svg') 
    svg = btn_svg.get_attribute('aria-label')

    if svg == '좋아요' : 
        like_btn.click() 
        print('좋아요를 눌렀습니다.') 
        time.sleep(5)
    else :
        print('이미 작업한 피드입니다.')               
        time.sleep(5)
    driver.refresh()
    time.sleep(5)

    