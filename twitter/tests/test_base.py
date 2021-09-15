from twitter.twitter import User, Influencer


def test_add_user():
    test_user = User(handle='test')
    test_user.add_follower('nicki_minaj')
    assert('nicki_minaj' in test_user.followers)
