from requests import get
from bs4 import BeautifulSoup


keyword = "풍수전쟁"

page = 1

base_url = "https://search.kyobobook.co.kr/search?keyword="
number_url = "&target=total&gbCode=TOT&page="f"{page}"
response = get(f"{base_url}{keyword}{number_url}")

if response.status_code != 200:
    print("웹 사이트 접근 불가")
else:
    while True:
        number_url = "&target=total&gbCode=TOT&page="f"{page}"
        response = get(f"{base_url}{keyword}{number_url}")
        soup = BeautifulSoup(response.text, "html.parser")
        book_info_first = soup.find("ul", class_="prod_list")
        book_info = book_info_first.find_all("li", class_="prod_item", recursive=False)
        if len(book_info) == 0:
            break
        print(f"{base_url}{keyword}{number_url}")
        page += 1


        
        










"""from selenium import webdriver
from selenium.webdriver.common.by import By

# 셀레니움 웹 드라이버 초기화
driver = webdriver.Chrome()

# 웹 페이지 로드
base_url = "https://search.kyobobook.co.kr/search?keyword="
keyword = "역행자"
driver.get(f"{base_url}{keyword}")

# div 태그에 class="pagination"을 가지고 있는 요소를 찾기
pagination_div = driver.find_elements(By.CSS_SELECTOR, 'a.btn_page_num')

# pagination_div 내부의 데이터 개수 알아내기
data_count = len(pagination_div)

# 결과 출력
print("데이터 개수:", data_count)

# 드라이버 종료
driver.quit()"""





