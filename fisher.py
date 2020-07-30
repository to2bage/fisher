"""
Project name: fisher
Description:
Create Time: 2020/7/30 09:03
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from app.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
