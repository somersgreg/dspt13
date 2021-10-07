from flask import Flask, request
from .twitter_functions import upsert_author
from .predict import get_most_likley_author
from .data_model import DB
import pathlib
import spacy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////Users/johnhurdle/Dropbox/PS/clients/Lambda/repos/dspt13/twitter/twitter_db.sqlite3'
DB.init_app(app)

spacy_path = pathlib.Path(pathlib.Path(__file__).parent, 'spacy_model')
spacy_model = spacy.load(spacy_path)


def create_app():

    @app.route('/')
    def landing():
        DB.create_all()
        return 'welcome to my twitter app'


    @app.route('/add_author')
    def add_author():
        author_handle = request.args['author_handle']
        author = upsert_author(author_handle=author_handle, spacy_model=spacy_model)
        return ', '.join([t.body for t in author.tweets])


    @app.route('/get_author')
    def get_author():
        tweet_body = request.args['tweet_body']
        author = get_most_likley_author(tweet_body=tweet_body, spacy_model=spacy_model)
        return author[0]

    return app
