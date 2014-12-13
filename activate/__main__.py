#!/usr/bin/python

import os

os.system('clear')

def actions(): 
    jobs = raw_input('What would you have me do?: ')

    if jobs == ('facebook'):
       os.system('sensible-browser --new-window="http://www.facebook.com"')

    if jobs == ('idk'):
       os.system('clear')
       print ('Well, you better think of something..')
       os.system('sleep 4 && python ~/klib/activate')

    if jobs == ('exit'):
       os.system('clear')
       print ('Ok, let me know if you need anything..')
       os.system('sleep 4')

actions()
