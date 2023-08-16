"""
爬取美国白宫总统名字
"""
import requests
from bs4 import BeautifulSoup
url = "https://www.whitehouse.gov/about-the-white-house/presidents/"
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "lxml")
for i in soup.select("a.full-link > span.screen-reader-text"):
    print(i.text.strip())
