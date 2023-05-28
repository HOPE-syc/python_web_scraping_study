from requests import get
from bs4 import BeautifulSoup

base_url = "https://search.kyobobook.co.kr/search?keyword="
search_term = "파이썬"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("웹 사이트에 접근할 수 없습니다.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    book_info = soup.find_all("div", class_="prod_info_box")
    for book_info_name_section in book_info:
        book_links = book_info_name_section.find_all("a", class_="prod_info")
        book_link_info = book_links[0]
        book_link_info_link = book_link_info['href']
        book_author_box = book_info_name_section.find_all('div', class_="auto_overflow_inner")
        book_price_main = book_info_name_section.find_all('span', class_="price")
        book_price = book_price_main[0]
        for book_author_section in book_author_box:
            book_authors = book_author_section.find('a', class_="author")
            for book_link in book_links:    
                book_names = book_link.text
                if book_authors is not None:
                    print(book_link_info_link,book_names,book_authors.text,book_price.text)

                
           