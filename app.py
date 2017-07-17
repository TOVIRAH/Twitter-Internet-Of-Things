import subprocess
import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

# You get these from twitter and they're associated with your username
consumer_key=   "XXXXXXXXXXXXXXXXXXXXXX"
consumer_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key=     "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret=  "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Get the Tweepy API set up and authenticated
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Streaming - this listens to your twitter account
class listener(StreamListener):

    def on_data(self, data):
        print type(data)
        get_tweet(data);
        return True

    def on_error(self, status):
        print status

# Start some process on the device
def call_subroutine():
    print "Starting the recordings..."
    subprocess.call("alsa.sh") #subprocess.call alsa ... & alsa ... ; SCP ...

def get_tweet(tweet):
    try: # check that it is a tweet
        jtweet = json.loads(tweet)["user"]['screen_name']
    except: # catches non tweets
        return False;

    # outside try catch so it has its own exception handler.
    if (jtweet == "Stephen_MacNeil"):
        call_subroutine();

# Set up the twitter stream associated with the user.
twtStream = Stream(auth, listener())
twtStream.userstream(_with="user", replies="none")
