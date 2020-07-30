"""
Project name: fisher
Description:
Create Time: 2020/7/30 09:42
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Blueprint, jsonify, request

from app.libs.helps import is_isbn_or_keywords
from app.libs.yushu_book import YushuBook
from app.validators.book import SearchForm
from app.view_models.book import BookViewModel

bp_book = Blueprint("book", __name__)

# /book/search
# @bp_book.route("/search/<q>/<int:page>")
# def search(q: str, page: int):
#     """
#     q: 可以是普通关键字 or isbn
#     page: 分页操作
#     :return:
#     """
#     key_or_isbn = is_isbn_or_keywords(q)
#     if key_or_isbn == "isbn":
#         rect = YushuBook.search_by_isbn(q)
#     elif key_or_isbn == "key":
#         rect = YushuBook.search_by_keyword(q)
#
#     return jsonify(rect)

# /book/search?q={}&count={}&start={}
@bp_book.route("/search")
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        key_or_isbn = is_isbn_or_keywords(q)
        if key_or_isbn == "isbn":
            rect = YushuBook.search_by_isbn(q)
            rect = BookViewModel.package_single(rect, q)
        elif key_or_isbn == "key":
            rect = YushuBook.search_by_keyword(q)
            rect = BookViewModel.package_collection(rect, q)

        return jsonify(rect)
    else:
        # return jsonify(dict(message="内部服务器出错", error_code=4000))
        return jsonify(form.errors)