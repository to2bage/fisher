"""
Project name: fisher
Description:
Create Time: 2020/7/30 12:29
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json() if return_json else resp.text
        return {} if return_json else ""
