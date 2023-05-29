from requests import get
from bs4 import BeautifulSoup
from search_funtions.book_search import book_search_function

book = book_search_function("파이썬") 

def get_page_count(keyword):
    base_url = "https://search.kyobobook.co.kr/search?keyword="
    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("웹 사이트에 접근할 수 없습니다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        page_numbers = soup.find_all("div", class_="result_area")
        for page_number in page_numbers:
            page_count = page_number.find_all("div", class_="pagination")
            print(page_count)

book_number = get_page_count("파이썬")

print(book_number)

