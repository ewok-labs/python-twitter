#!/usr/bin/env python
#This file is modified from the https://github.com/bear/python-twitter
#Kudos go all to bear and the makers of this lib, all lib/wrapper related things remain with same LICENSE, please see: https://github.com/bear/python-twitter for LICENSE

import ConfigParser
import getopt
import os
import sys
import twitter

def GetConsumerKeyEnv():
  return os.environ.get("TWEETUSERNAME", None)
def GetConsumerSecretEnv():
  return os.environ.get("TWEETPASSWORD", None)

def GetAccessKeyEnv():
  return os.environ.get("TWEETACCESSKEY", None)

def GetAccessSecretEnv():
  return os.environ.get("TWEETACCESSSECRET", None)
class TweetRc(object):
  def __init__(self):
    self._config = None

  def GetConsumerKey(self):
    return self._GetOption('consumer_key')

  def GetConsumerSecret(self):
    return self._GetOption('consumer_secret')

  def GetAccessKey(self):
    return self._GetOption('access_key')

  def GetAccessSecret(self):
    return self._GetOption('access_secret')

  def _GetOption(self, option):
    try:
      return self._GetConfig().get('Tweet', option)
    except:
      return None

  def _GetConfig(self):
    if not self._config:
      self._config = ConfigParser.ConfigParser()
      self._config.read(os.path.expanduser('~/.tweetrc'))
    return self._config

def main(message):
  try:
    shortflags = 'h'
    longflags = ['help', 'consumer-key=', 'consumer-secret=', 
                 'access-key=', 'access-secret=', 'encoding=']
    opts, args = getopt.gnu_getopt(sys.argv[1:], shortflags, longflags)
  except getopt.GetoptError:
    print("No file exception")
  consumer_keyflag = None
  consumer_secretflag = None
  access_keyflag = None
  access_secretflag = None
  encoding = None
  rc = TweetRc()
  consumer_key = consumer_keyflag or GetConsumerKeyEnv() or rc.GetConsumerKey()
  consumer_secret = consumer_secretflag or GetConsumerSecretEnv() or rc.GetConsumerSecret()
  access_key = access_keyflag or GetAccessKeyEnv() or rc.GetAccessKey()
  access_secret = access_secretflag or GetAccessSecretEnv() or rc.GetAccessSecret()
  if not consumer_key or not consumer_secret or not access_key or not access_secret:
    PrintUsageAndExit()
  api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_key, access_token_secret=access_secret,
                    input_encoding=encoding)
  try:
    status = api.PostUpdate(message)
  except UnicodeDecodeError:
    print("Your message could not be encoded.  Perhaps it contains non-ASCII characters?")
    print("Try explicitly specifying the encoding with the --encoding flag")
    sys.exit(2)
  print("%s just posted: %s" % (status.user.name, status.text))

if __name__ == "__main__":
  main("hello, patrik put here the message to send out!")
