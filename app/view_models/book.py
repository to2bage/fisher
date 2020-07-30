"""
Project name: fisher
Description:
Create Time: 2020/7/30 14:52
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""

class BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }

        if data:
            returned["total"] = 1
            returned["book"] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }

        if data:
            returned["total"] = data["total"]
            returned["book"] = [cls.__cut_book_data(book) for book in data["books"]]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """ 裁剪数据 """
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or "",
            "author": ", ".join(data["author"]),
            "price": data["price"],
            "summary": data["summary"] or "",
            "image": data["image"]
        }