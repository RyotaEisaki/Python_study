import requests
from bs4 import BeautifulSoup

url = 'https://programming-beginner-zeroichi.jp/'

headers = {'User-Agent':'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url,headers=headers).content,'lxml')
images =[]

for img in soup.find_all('img',class_="img",limit=5):
    print(img.get("src"))
    images.append(img.get("src"))

for target in images:
    re = requests.get(target)
    with open ('/Users/RYOTA/Desktop/scraping_img/' + target.split('/')[-1],'wb') as f:
        f.write(re.content)

print("Image Scraping Done")