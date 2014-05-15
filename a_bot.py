#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy import API,OAuthHandler,Stream 
import __builtin__
from tweepy.streaming import StreamListener
import sqlite3, sys


#these variables can be found in the http://dev.twitter.com  setup page
#under 'details'
#.gitignore on bot.py  


#-----------        this is what .gitignore is for     ---------------------

CONSUMER_KEY = '__________________'
CONSUMER_SECRET = '__________________' 
ACCESS_TOKEN = '__________________'
TOKEN_SECRET = '__________________'

#==============================================================================

#make sure this part gets copied over exactly to a_bot.py

c = sqlite3.connect('waluigi_tt.db')
cur = c.cursor()
cur.execute('create table if not exists tweets (uid, user, timestamp, status, replies, geo, source)')


class Listener(StreamListener):  #taken from tweepy github
  #this replaces timeline methods

  def on_status(self, status): 
    #directly from https://github.com/tweepy/tweepy/blob/master/tweepy/models.py
    try:
      uid = status.id_str
      usr = status.author.screen_name.strip()
      txt = status.text.strip()
      recip = status.in_reply_to_status_id
      geo = status.coordinates
      src = status.source.strip()
      ts = status.created_at
      cur.execute("insert into tweets (user,  status, uid) values(?, ?, ?)", (usr,  txt, uid))
      c.commit()

    except Exception as exc:
      # Most errors we're going to see relate to the handling of UTF-8 messages (sorry)
      print 'error'      
    if usr == "tree_herder":
      print usr, txt
      if "l_on" in txt:
        print "lights on"
        sys.call(["sh", "/home/pi/meetups/lamp.sh", "1"])
      elif "l_off" in txt:
        print "lights off"
        sys.call(["sh", "/home/pi/meetups/lamp.sh", "0"])

  def on_error(self, status):
    print status
  
listener = Listener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
__builtin__.handle = API(auth)
__builtin__.stream =Stream(auth, listener)
