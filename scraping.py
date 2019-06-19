import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
from pytz import timezone
import peewee
from models import Scraping
from db_services import compara_manchetes

# Certifica-se da existência da tabela.
Scraping.create_table()

page = requests.get('https://g1.globo.com')

soup = BeautifulSoup(page.content, 'html.parser')

# Permite busca com múltiplas classes na tag
# tag = soup.find_all('a', {'class': 'feed-post-link', 'class': 'gui-color-primary', 'class': 'gui-color-hover'})

search = soup.find_all('a', class_="feed-post-link")

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
dt_hr_sp_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

for s in search:
    manchete = s.contents[0]
    url = s['href']
    data = dt_hr_sp_texto
    localizado = compara_manchetes(manchete)
    if not localizado:
        insert = Scraping.create(manchete=manchete, url=url, datahora=data)
        print('Nova adição!')