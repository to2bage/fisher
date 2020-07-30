"""
Project name: fisher
Description:
Create Time: 2020/7/30 13:27
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class SearchForm(Form):
    q = StringField(
        validators=[
            DataRequired(message="查询内容不能为空"),
            Length(min=1, max=30, message="查询内容的长度介于[1, 30]")
        ]
    )
    page = IntegerField(
        validators=[
            NumberRange(min=1, max=99, message="页号必须介于[1, 99]")
        ],
        default=1
    )