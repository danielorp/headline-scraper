import sqlite3
import peewee
from models import Scraping


def create_table():
        try:
                Scraping.create_table()
        except peewee.OperationalError:
                print('Tabela Author ja existe!')

