from requests import get
from bs4 import BeautifulSoup

base_url = "https://search.kyobobook.co.kr/search?keyword="
search_term = "파이썬"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("웹 사이트를 막았습니다.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    book_info = soup.find_all("div", class_="prod_info_box")
    print(book_info)
    """
    book_info_name = soup.find_all("a", class_="prod_info"), soup.find_all("a", class_="author rep")
    """
    for book_info_name_section in book_info:
        book_links = book_info_name_section.find_all("a", class_="prod_info")
        book_link_info = book_links[0]
        book_link_info_link = book_link_info['href']
        book_author = book_info_name_section.find('a', class_="author rep")
        print(book_author.text)
        for book_link in book_links:    
            book_names = book_link.find("span")
            # print(book_link_info_link, book_names.string)
           