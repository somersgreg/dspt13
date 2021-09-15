import pandas as pd
import datetime


class User():
    def __init__(self, handle, verified=False, admin=False, followers=None, tweets=None, last_location=None,
                 join_date=datetime.datetime.today()):
        if not tweets:
            tweets = []
        if not followers:
            followers = []
        self.handle = handle
        self.verified = verified
        self.admin = admin
        self.followers = followers
        self.tweets = tweets
        self.join_date = join_date
        self.last_location = last_location

    def add_follower(self, follower):
        self.followers.append(follower)
        print('I just got a new follower. That is so great.')


class Influencer(User):
    def __init__(self, handle, verified, admin, followers, tweets, last_location, join_date, sponsorships,
                 industry_focus, ):
        self.sponsorships = sponsorships
        self.industry_focus = industry_focus
        User.__init__(self, handle, verified, admin, followers, tweets, last_location, join_date)


def get_twitter_followers(handle):
    follower_map = {
        'cher': 123
    }
    return follower_map[handle]


jack_dorsey = Influencer('jackdorsey', True, True, ['ariana_grande', 'mother_teresa'], 'hi', 'dallas', 'today',
                         ['twitter'], 'tweeting')
print(len(jack_dorsey.followers))
jack_dorsey.add_follower('angela_merkel')
print(len(jack_dorsey.followers))

pd.DataFrame
