"""
Project name: fisher
Description:
Create Time: 2020/7/30 09:57
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
def is_isbn_or_keywords(q):
    isbn_or_key = "key"
    if len(q)==13 and q.isdigit():
        isbn_or_key = "isbn"
    if "-" in q and len(q.replace("-", ""))==10 and q.replace("-", "").isdigit():
        isbn_or_key = "isbn"
    return isbn_or_key