import requests
import bs4
import csv

sach={'q':'Python', 'users':'1000'}
url = 'http://b.hatena.ne.jp/search/text'
req = requests.get(url, params = sach, timeout = 15)
soup = bs4.BeautifulSoup(req.text, 'html.parser')

bookmarks = []

for b in soup.findAll('h3', {'class':''}):
    title = b.find('a').get('title')
    url = b.find('a').get('href')
    bookmarks.append([title, url])

with open('bookmarks.csv', 'w', encoding='shift-jis') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(bookmarks)