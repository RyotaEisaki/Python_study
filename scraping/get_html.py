import requests 

response = requests.get('https://qiita.com/neet-AI/items/98d4194872ee4f53e3b4') 
print(response.text)