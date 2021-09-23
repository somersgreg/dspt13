import psycopg2
import sqlite3
import os

sqlite_conn = sqlite3.connect('/Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/rpg_db.sqlite3')

sqlite_curs = sqlite_conn.cursor()

sqlite_curs.execute("""select * from charactercreator_character limit 5000""")

characters = sqlite_curs.fetchall()

conn = psycopg2.connect(dbname=os.environ['DBUSER'], user=os.environ['DBUSER'], password=os.environ['DBPASS'],
                        host=os.environ['DBHOST'])

curs = conn.cursor()

for x in characters:
    curs.execute("""insert into character values ({})""".format(', '.join(["'{}'".format(str(y)) for y in x])))
    print('inserted character')

conn.commit()

curs.execute("""select count(*) from character""")

results = curs.fetchall()

print(results)
