#!/usr/bin/env python
#This file is modified from the https://github.com/bear/python-twitter
#Kudos go all to bear and the makers of this lib, all lib/wrapper related things remain with same LICENSE, please see: https://github.com/bear/python-twitter for LICENSE

import getopt
import os
import sys
from twitter import *
import config
import serial



def main(message):
  twitter_api = Twitter(auth=OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET))
  ser = serial.Serial(port=config.SERIAL_PORT, baudrate=19200, timeout=0, writeTimeout=0) 
  
  while True:
    data = self.ser.readline(1)                
    if data:
      # check how the plants are feeling.. IF they are under threshold X, then tweet!
      plant_name = "Mr X"
      #twitter_api.statuses.update(status=message + "\n Yours sincerely " + plant_name)
    time.sleep(1)
  
  

  

if __name__ == "__main__":
  main("Help! I'm dying!")
