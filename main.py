from selenium import webdriver
# sudo apt-get install chromium-chromedriver
from selenium.webdriver.common.by import By
import time

# WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
driver = webdriver.Chrome(options=options)

try:
    # URL 열기
    driver.get("https://v.daum.net/v/20240526184846482")

    # 페이지가 로드될 때까지 잠시 대기
    time.sleep(2)  # 필요에 따라 조정

    # 기사 제목과 본문 찾기
    title = driver.find_element(By.TAG_NAME, "h3").text
    content = driver.find_element(By.CLASS_NAME, "article_view").text

    print("기사 제목:", title)
    print("기사 내용:", content)

finally:
    # WebDriver 종료
    driver.quit()
