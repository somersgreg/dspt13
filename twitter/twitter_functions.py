import tweepy
from .data_model import DB, Tweet, Author
import numpy as np
import os

twitter_auth = tweepy.OAuthHandler(os.environ['twitter_key'], os.environ['twitter_secret'])
twitter_api = tweepy.API(twitter_auth)


def upsert_author(author_handle, spacy_model):
    twitter_author = twitter_api.get_user(user_id=author_handle)
    if Author.query.get(twitter_author.id):
        db_author = Author.query.get(twitter_author.id)
    else:
        db_author = Author(id=twitter_author.id, name=author_handle)
        DB.session.add(db_author)

    author_tweet_ids = [tweet.id for tweet in Tweet.query.filter(Tweet.author_id == db_author.id)]

    if len(author_tweet_ids) > 0:
        last_tweet_stored_id = np.max(author_tweet_ids)
        author_tweets = twitter_author.timeline(count=200, exclude_replies=True, include_rts=False,
                                                tweet_mode='extended', since_id=last_tweet_stored_id)
    else:
        author_tweets = twitter_author.timeline(count=200, exclude_replies=True, include_rts=False,
                                                tweet_mode='extended')

    for tweet in author_tweets:
        vectorized_tweet = spacy_model(tweet.full_text).vector
        db_tweet = Tweet(id=tweet.id, body=tweet.full_text, vect=vectorized_tweet)
        db_author.tweets.append(db_tweet)
        DB.session.add(db_tweet)
    DB.session.commit()
    return db_author
