import requests

r = requests.get('https://codezine.jp/')
print(type(r))
print(r.status_code)

text = r.text
for line in text.split('\n'):
    if '<title>' in line or '<h1>' in line:
        print(line.strip())
