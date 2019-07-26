import sqlite3
import peewee
from difflib import SequenceMatcher


db = peewee.SqliteDatabase('scraping.db')


class Materia(peewee.Model):
    manchete = peewee.CharField()
    url = peewee.CharField()
    datahora = peewee.DateTimeField()

    class Meta:
        database = db


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def compara_manchetes(manchete):
        query_all = Materia.select()
        for row in query_all:
                rate = similar(row.manchete, manchete)
                if rate > 0.90:
                        return True

