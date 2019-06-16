import requests
from bs4 import BeautifulSoup
import sqlite3
from db_services import create_table, drop_table

page = requests.get('https://g1.globo.com')

soup = BeautifulSoup(page.content, 'html.parser')

# tag = soup.find_all('a', {'class': 'feed-post-link', 'class': 'gui-color-primary', 'class': 'gui-color-hover'})

search = soup.find_all('a', class_="feed-post-link")

for s in search:
    print(s.contents)
    print(s['href'])

create_table()
