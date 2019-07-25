import sqlite3
import peewee
from models import Scraping
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def compara_manchetes(manchete):
        query_all = Scraping.select()
        for row in query_all:
                rate = similar(row.manchete, manchete)
                if rate > 0.90:
                        return True

