def save_to_file(file_name, book_search):
    file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
    file.write("name,author,price,link\n")

    for info in book_search:
        book_name = info['book_name']
        book_author = info['book_author']
        book_price = info['book_price']
        book_link = info['book_link']

        # 가격 정보를 따옴표로 감싸서 저장
        file.write(f"\"{book_name}\",\"{book_author}\",\"{book_price}\",\"{book_link}\"\n")

    file.close()