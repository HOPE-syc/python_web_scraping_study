from requests import get
from bs4 import BeautifulSoup
from search_funtions.book_search import book_search_function

book = book_search_function("파이썬") 

maximum = 0
page = 1

def get_page_count(keyword):
    base_url = "https://search.kyobobook.co.kr/search?keyword="
    number_url = "&target=total&gbCode=TOT&page="f"{page}"
    response = get(f"{base_url}{keyword}{number_url}")

    if response.status_code != 200:
        print("웹 사이트에 접근할 수 없습니다.")
    else:
        while 1:
            page_

book_number = get_page_count("파이썬")

print(book_number)

