from flask import Flask
import sqlite3


app = Flask(__name__)


@app.route('/')
def landing():

    conn = sqlite3.connect('/Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/rpg_db.sqlite3')

    curs = conn.cursor()

    curs.execute("""select * from charactercreator_character limit 10""")

    results = curs.fetchall()

    conn.close()

    return app.send_static_file('landing.html')


@app.route('/items')
def items():

    conn = sqlite3.connect('/Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/rpg_db.sqlite3')

    curs = conn.cursor()

    curs.execute("""select * from armory_item limit 10""")

    results = curs.fetchall()

    return str(results)


app.run()
