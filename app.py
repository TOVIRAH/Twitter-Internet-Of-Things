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

username = "raspgarden" # must correspond to userid
userid = "213877377"    # (http://gettwitterid.com)

deviceID = "ineq1" # some unique way to identify the device.

modes = { # on tweet command : shell script to execute
    'start': 'start-alsa.sh',
    'end': 'kill-alsa.sh'
    }

# Get the Tweepy API set up and authenticated
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Streaming - this listens to your twitter account
class listener(StreamListener):

    def on_data(self, data):
        get_tweet(data);
        return True

    def on_error(self, status):
        print (status)

# Start some shell scripts processes on the device (specified above)
def call_subroutine(content):
    for i in modes:
        if (content == i):
            print (modes[i])
            try:
                subprocess.call(modes[i]) #alsa ... & alsa ... ; SCP ...
                #api.update_status(deviceID + ": " + modes[i] + " @" + username) # tweet a response.
            except:
                print ("exception thrown")
                #api.update_status(deviceID + ": " + "problem occurred" + " @" + username) # tweet a response.

def get_tweet(tweet):
    try: # check that it is a tweet
        tweetObj = json.loads(tweet)
        tweetUser = tweetObj["user"]['screen_name']
    except: # catches non tweets
        return False;
    # outside try catch so it has its own exception handler.
    if (tweetUser == username):
        print (tweetObj["user"]['screen_name'] + ": " + tweetObj["text"])
        call_subroutine(tweetObj["text"]);

# Set up the twitter stream associated with the user.
twtStream = Stream(auth, listener())
twtStream = twtStream.filter(follow=[userid]) # needs to be ID not username.
#twtStream.userstream(_with="user", replies="none") # works only for username associated with app.
