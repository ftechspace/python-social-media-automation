import os, tweepy

TWITTER_CUSTOMER_API_KEY = os.environ.get('CUSTOMER_API_KEY')
TWITTER_CUSTOMER_API_KEY_SECRET = os.environ.get('CUSTOMER_API_KEY_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(
    TWITTER_CUSTOMER_API_KEY, 
    TWITTER_CUSTOMER_API_KEY_SECRET, 
    TWITTER_ACCESS_TOKEN, 
    TWITTER_ACCESS_TOKEN_SECRET
)

twitter_api = tweepy.API(auth)

def twitter(content):
    try:
        twitter_api.verify_credentials()
        print("Auth is verified")
    except:
        print("Auth failed")
        return ''

    # create a tweet 
    post_tweet = twitter_api.update_status(content)
    # like the tweet 
    twitter_api.create_favorite(post_tweet.id)
    return ''

content = '''
Testing bot: with my community
https://www.youtube.com/watch?v=zGcMOh2eNdg&feature=youtu.be
'''
twitter(content)