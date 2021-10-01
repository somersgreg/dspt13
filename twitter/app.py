from flask import Flask, request
from twitter_functions import upsert_author
from data_model import DB

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/twitter/twitter_db.sqlite3'
DB.init_app(app)


@app.route('/')
def landing():
    DB.create_all()
    return 'welcome to my twitter app'


@app.route('/add_author')
def add_author():
    author_handle = request.args['author_handle']
    author = upsert_author(author_handle=author_handle)
    return ', '.join([t.body for t in author.tweets])


app.run()
