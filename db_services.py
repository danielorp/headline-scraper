import sqlite3


def drop_table():
    try:
        conn = sqlite3.connect('scraping.db')

        cursor = conn.cursor()

        cursor.execute("DROP TABLE SCRAPING")

        conn.close()

        print('Tabela SCRAPING excluída com sucesso.')
    except Exception as e:
        print(e)

def create_table():
    try:
        conn = sqlite3.connect('scraping.db')

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE SCRAPING (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                manchete TEXT NOT NULL,
                url TEXT NOT NULL,
                datahora DATETIME NOT NULL
        );
        """)

        conn.close()

        print('Tabela SCRAPING criada com sucesso.')
    except Exception as e:
        print(e)