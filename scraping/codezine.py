import requests

r = requests.get('https://codezine.jp/')
print(type(r))
print(r.status_code)

text = r.text
for line in text.split('\n'):
    if '<title>' in line or '<h1>' in line:
        print(line.strip())


################

from bs4 import BeautifulSoup

# HTMLを解析したオブジェクトを生成
soup = BeautifulSoup(text, 'html.parser')
print(soup.title) # <title> タグの情報を取得
print(soup.h1) # <h1> タグの要素を取得
# h1タグの中のaタグのなかのimgタグの中のalt属性
print(soup.h1.a.img['alt'])

atags = soup.find_all('a')
# print('number of a tags:'. len(atags))
for atag in atags[:5]:
    print('title:', atag.text)
    print('link:', atag['href'])
