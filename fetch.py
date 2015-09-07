import twitter
from keys import *

api = twitter.Api(consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token_key = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET)

# Search for tweets by keyword
tweets = api.GetSearch("#yeahright", count=50)

for tweet in tweets:
	print tweet.text

# Search for tweets by users
statuses = api.GetUserTimeline(screen_name='rickygervais')

for tweet in statuses:
	print tweet.text
