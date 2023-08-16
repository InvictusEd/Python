"""
爬取日本分子协会封面图
"""
import re
from urllib.parse import urljoin

import requests

import os.path
url = "https://www.mbsj.jp/gtc/cover_gallery.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
response = requests.get(url)
# print(response.text)
for i in re.finditer(r"TOC/cover/\d{2}_\d{2}_large.jpg", response.text):
    basename = i.group()
    path = urljoin(url, i.group())
    with open(os.path.basename(basename), "wb") as f:
        f.write(requests.get(path, headers=headers).content)
