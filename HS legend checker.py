import requests
from bs4 import BeautifulSoup
import slacker

already = []

r = requests.get('http://dda.ac/deck?sw=%201%EC%9C%84')
r.encoding = 'utf-8'

html = r.text

soup = BeautifulSoup(html, 'html.parser')

all_div = soup.findAll('div', {'class': 'a-deck'})

for div in all_div:

    ids = div.findAll('p', {'class': 'ellipsis a-deck-title'})
    for id in ids:
        print(id.text)

