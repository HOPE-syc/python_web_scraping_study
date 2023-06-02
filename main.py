from requests import get
from bs4 import BeautifulSoup
from search_funtions.book_search import book_search_function

keyword = input("어떤 책을 찾으십니까?")

book_search = book_search_function(keyword)

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
file.write("name,author,price,link\n")

for info in book_search:
    book_name = info['book_name']
    book_author = info['book_author']
    book_price = info['book_price']
    book_link = info['book_link']

    # 가격 정보를 따옴표로 감싸서 저장
    file.write(f"\"{book_name}\",\"{book_author}\",\"{book_price}\",\"{book_link}\"\n")

file.close()

