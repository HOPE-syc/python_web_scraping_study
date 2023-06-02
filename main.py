from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_args
from search_funtions.book_search import book_search_function
app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search_main():
    keyword = request.args.get("keyword")
    page = request.args.get('page', type=int, default=1)
    
    if keyword in db:
        books_search = db[keyword]
    else:
        books_search = book_search_function(keyword)
        db[keyword] = books_search
    
    per_page = 20
    offset = (page - 1) * per_page
    pagination_books = books_search[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(books_search))
    
    return render_template("search.html", keyword=keyword, books_search=pagination_books, pagination=pagination)

app.run("0.0.0.0")



