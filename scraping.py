import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime, timedelta
from pytz import timezone
import peewee
from db_services import compara_manchetes, Materia


def insereMateriaCompleta(manchete, url, data):
        insert = Materia.create(manchete=manchete, url=url, datahora=data)
        return


def formatData(data):
        year = int(data[:4])
        month = int(data[5:7])
        day = int(data[8:10])
        hour = int(data[11:13])
        minute = int(data[14:16])
        dt = datetime(year, month, day, hour, minute) - timedelta(hours=3)
        return dt


def extraiData(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        materiacompl = soup.find_all('time')
        for mt in materiacompl:
                if mt['itemprop'] == 'datePublished':
                        dataPublic = formatData(mt['datetime'])
                        return dataPublic
                #if mt['itemprop'] == 'dateModified':
                #        dataModified = formatData(mt['datetime'])
                #        dataModified

######################################################################################################

# Certifica-se da existência da tabela.
Materia.create_table()

search = requests.get('https://g1.globo.com')
search = BeautifulSoup(search.content, 'html.parser')
# Permite busca com múltiplas classes na tag
# tag = soup.find_all('a', {'class': 'feed-post-link', 'class': 'gui-color-primary', 'class': 'gui-color-hover'})
search = search.find_all('a', class_="feed-post-link")


for s in search:
        manchete = s.getText()
        url = s['href']
        data = extraiData(url)
        localizado = compara_manchetes(manchete)
        if not localizado:
                insereMateriaCompleta(manchete, url, data)
                print('Nova adição!')

