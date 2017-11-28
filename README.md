# Twitter-Internet-Of-Things

This project is a super simple barebones way to get your tweets to activate some functionality on a device. The device uses this code to listen to your twitter account. When you tweet it starts. It would be trivial to modify this code to listen to the text property as well and start on a *start* command or end on an *end* command.

# Installation

```
pip install tweepy
pip install moment
pip install psutil
```

# Authentication

You need twitter keys to make this work. You can get them here:

https://apps.twitter.com/app/new

# Getting it to work

```
python app.py
```

# Common Issues

1. If you get a ```401``` error code - you probably forgot to add your keys
2. Username and UserID have to match and correspond to the account that the device wants to listen to.
