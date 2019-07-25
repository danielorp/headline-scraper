import peewee
import sqlite3

db = peewee.SqliteDatabase('scraping.db')

class Scraping(peewee.Model):
    manchete = peewee.CharField()
    url = peewee.CharField()
    datahora = peewee.DateTimeField()

    class Meta:
        database = db
