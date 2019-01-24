import requests
from bs4 import BeautifulSoup
import slacker

r = requests.get('https://www.hearthpwn.com/')

soup = BeautifulSoup(r, 'html.parser')

all_li = soup.find_all('li class')

print(all_li)