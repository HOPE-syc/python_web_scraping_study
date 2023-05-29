from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_count(keyword):
    # 셀레니움 웹 드라이버 초기화
    driver = webdriver.Chrome("경로/크롬 드라이버")  # 본인의 크롬 드라이버 경로로 바꿔주세요

    base_url = "https://search.kyobobook.co.kr/search?keyword="

    try:
        # 페이지 접속
        driver.get(f"{base_url}{keyword}")

        # 페이지 로딩을 위해 명시적 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pagination")))

        # 페이지 번호 가져오기
        page_numbers = driver.find_elements(By.CLASS_NAME, "pagination")
        for page_number in page_numbers:
            print(page_number.text)

    finally:
        # 셀레니움 웹 드라이버 종료
        driver.quit()

get_page_count("파이썬")
