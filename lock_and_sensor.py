#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import os
import re

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
pinList = [26, 20, 21]

flag = 0
keywords=['Matthew','Fadi']
with open('match.txt') as f:
    txt=f.read()
   ## for profile in keywords:
    for profile in keywords:
        if re.search(r'\b{}\b'.format(profile),txt):
           flag = 1

if flag:
    print("MATCH")
    print("GREEN")
    print ("OPEN")
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
else:
    print("NO MATCH")
    print("RED")
    for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
try:
  GPIO.output(26, GPIO.LOW)
  # time.sleep(5);
  while True:
      if GPIO.input(15):
          print ("--DOOR SENSOR OPEN--")
          time.sleep(2)
      else:
          print ("--DOOR SENSOR CLOSED--")
          #break
          time.sleep(2)
          GPIO.cleanup()
          print ("Close")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

# Reset GPIO settings
  GPIO.cleanup()
