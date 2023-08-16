"""
爬取日本分子协会封面图
"""
import requests
import re
from urllib.parse import urljoin
import os.path
# chrome://version/
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://www.mbsj.jp/en/gtc/cover_gallery.html"
response = requests.get(url)
urls = []
names = []
for i in re.findall(r"../../gtc/TOC/cover/\d{2}_\d{2}_large.jpg", response.text):
    j = urljoin(url, i)
    urls.append(j)
    names.append(os.path.basename(j))
print(urls)
print(names)
for i in urls:
    with open(os.path.basename(j), "wb") as file:
        file.write(requests.get(i, headers=headers).content)
