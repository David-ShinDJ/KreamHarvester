import requests
from bs4 import BeautifulSoup

url = "https://kream.co.kr/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

print(response)
print("-------")
print(html)
print("-------")
print(soup)
print("-------")