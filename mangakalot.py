import requests
from bs4 import BeautifulSoup

url = "https://chapmanganato.to/manga-dr980474"
page = requests.get(url)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
tags = soup.find_all('a', class_='chapter-name text-nowrap')
tags = reversed(tags)
links = [tag.get('href') for tag in tags]

for i in links:
    print(i)
