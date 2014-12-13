#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('What would you have me do?: ')

    username = getpass.getuser()
    username = str(username)

    if jobs == ('facebook'):
       os.system('sensible-browser --new-window="http://www.facebook.com"')

    if jobs == ('who are you?'):
       os.system('clear')
       print ('I am Karmon, you know that..')
       os.system('sleep 4 && python ~/klib/activate')

    if jobs == ('who am i?'):
       os.system('clear')
       print ('You are ' + username + ', and you operate my library..')
       os.system('sleep 4 && clear')

    if jobs == ('whoami?'):
       os.system('clear')
       print ('You are ' + username + ', and you operate my library..')
       os.system('sleep 4 && clear')

    if jobs == ('whoami'):
       os.system('clear')
       print ('You are ' + username + ', and you operate my library..')
       os.system('sleep 4 && clear')

    if jobs == ('idk'):
       os.system('clear')
       print ('Well, you better think of something..')
       os.system('sleep 4 && python ~/klib/activate')

    if jobs == ('exit'):
       os.system('clear')
       print ('Ok, let me know if you need anything..')
       os.system('sleep 4')

    if jobs == ('help'):
       os.system('clear')
       os.system('sensible-browser ~/klib/activate/lib')

actions()
