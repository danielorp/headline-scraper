import sqlite3


def drop_table(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("DROP TABLE SCRAPING")

        print('Tabela SCRAPING excluida com sucesso.')
    except Exception as e:
        print(e)

def create_table(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE SCRAPING (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                manchete TEXT NOT NULL,
                url TEXT NOT NULL,
                datahora TEXT NOT NULL
        );
        """)

        print('Tabela SCRAPING criada com sucesso.')
    except Exception as e:
        print(e)
        
def insert_manchete(conn, manchete, url, data):
    try:
        cursor = conn.cursor()

        lista = [manchete, url, data]

        cursor.execute('insert into scraping(manchete, url, datahora) values (?, ?, ?)', lista);
        
        conn.commit()

        #cursor.execute('INSERT INTO SCRAPING VALUES({}, {} ,{});'.format(manchete, url, data))

        print('Registro inserido na tabela SCRAPING com sucesso.')
    except Exception as e:
        print(e)

