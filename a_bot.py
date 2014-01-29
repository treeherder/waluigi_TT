from tweepy import API,OAuthHandler
import __builtin__

#these variables can be found in the http://dev.twitter.com  setup page
#under 'details'

CONSUMER_KEY = '__________________'
CONSUMER_SECRET = '__________________' 
ACCESS_TOKEN = '__________________'
TOKEN_SECRET = '__________________'


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
__builtin__.handle = API(auth)