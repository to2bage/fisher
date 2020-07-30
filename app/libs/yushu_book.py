"""
Project name: fisher
Description:
Create Time: 2020/7/30 12:47
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import current_app

from app.libs._http import HTTP

class YushuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return  result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(
            keyword,
            current_app.config["PER_PAGE"],
            cls._paging_to_start(page))
        result = HTTP.get(url)
        print(current_app.config["PER_PAGE"])
        return result

    @classmethod
    def _paging_to_start(cls, page):
        (page - 1) * current_app.config["PER_PAGE"]