import tweepy
import time
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword = input("Enter keyword to search : ")
num = int(input("Enter number of tweets to display : "))
for tweet in tweepy.Cursor(api.search, keyword).items(num):
	print('Tweet by ' + tweet.user.name + '(@' + tweet.user.screen_name + ')')
	print(tweet.text + '\n')
	time.sleep(1)

print('Done')