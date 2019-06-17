import requests
from bs4 import BeautifulSoup
import sqlite3
from db_services import create_table, drop_table, insert_manchete
from datetime import datetime
from pytz import timezone

page = requests.get('https://g1.globo.com')

soup = BeautifulSoup(page.content, 'html.parser')

# tag = soup.find_all('a', {'class': 'feed-post-link', 'class': 'gui-color-primary', 'class': 'gui-color-hover'})

search = soup.find_all('a', class_="feed-post-link")

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
dt_hr_sp_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

connection = sqlite3.connect('scraping.db')

for s in search:
    manchete = s.contents
    url = s['href']
    data = dt_hr_sp_texto
    insert_manchete(conn=connection, manchete=manchete, url=url, data=data)    
