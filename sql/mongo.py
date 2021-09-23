import pymongo
import sqlite3

mongo_client = pymongo.MongoClient(
    "mongodb+srv://jhurdle:jhurdle@dspt13.ualgx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

sql_conn = sqlite3.connect('/Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/rpg_db.sqlite3')
sql_cursor = sql_conn.cursor()
db = mongo_client.myFirstDatabase
if 'rpg_collection' not in db.list_collection_names():
        print(db.list_collection_names())
        db.create_collection('rpg_collection')

character_query = """select * from charactercreator_character"""

character_results = sql_cursor.execute(character_query).fetchall()

for c in character_results:
    doc = {}
    keys = [col[0] for col in sql_cursor.description]
    for i, key in enumerate(keys):
        doc.update({key: c[i]})
    db.rpg_collection.insert_one(doc)
    print(doc)

