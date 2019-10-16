import requests
from bs4 import BeautifulSoup

response = requests.get('https://qiita.com/neet-AI/items/98d4194872ee4f53e3b4')

soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string
print(title)