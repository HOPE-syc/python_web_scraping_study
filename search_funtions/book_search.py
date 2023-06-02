from requests import get
from bs4 import BeautifulSoup

def book_search_function(keyword):
    page = 1
    results = []  # 결과를 저장할 리스트

    base_url = "https://search.kyobobook.co.kr/search?keyword="
    number_url = "&target=total&gbCode=TOT&page="f"{page}"
    response = get(f"{base_url}{keyword}{number_url}")
    if response.status_code != 200:
        print("웹 사이트에 접근할 수 없습니다.")
    else:
        while True:
            number_url = "&target=total&gbCode=TOT&page="f"{page}"
            response = get(f"{base_url}{keyword}{number_url}")
            soup = BeautifulSoup(response.text, "html.parser")
            book_info_first = soup.find("ul", class_="prod_list")
            if book_info_first is None:
                break
            book_info = book_info_first.find_all("li", class_="prod_item", recursive=False)
            if len(book_info) == 0:
                break
            page += 1
            book_info = soup.find_all("div", class_="prod_info_box")
            for book_info_name_section in book_info:
                book_links = book_info_name_section.find_all("a", class_="prod_info")
                book_link_info = book_links[0]
                book_link_info_link = book_link_info['href']
                book_author_box = book_info_name_section.find_all('div', class_="auto_overflow_inner")
                book_price_main = book_info_name_section.find_all('span', class_="val")
                book_price = book_price_main[0]
                for book_author_section in book_author_box:
                    book_authors = book_author_section.find('a', class_="author")
                    for book_link in book_links:    
                        book_names_id = book_link.select('span[id]')
                        for span_tag in book_names_id:
                            if '해외주문' not in span_tag.text:
                                book_names = span_tag.text
                        if book_authors is not None:
                            book_data = {
                                'book_link' : book_link_info_link,
                                'book_name' : book_names,
                                'book_author' : book_authors.string,
                                'book_price' : book_price.string
                            }
                            results.append(book_data)

    return results

   
