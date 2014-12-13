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

    else:
       os.sysytem('clear')
       print "I'm sorry, what?"
       os.system('sleep 4 && python ~/klib/activate')

actions()
