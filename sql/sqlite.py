import sqlite3
import pandas as pd


conn = sqlite3.connect('/Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/rpg_db.sqlite3')

curs = conn.cursor()

curs.execute("""select * from charactercreator_character limit 10""")

results = curs.fetchall()

print(pd.DataFrame(results).head())