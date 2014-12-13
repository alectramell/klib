#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('KARMON$ ')

    if jobs == ('exit'):
       exit()

    if jobs == ('hide'):
       os.system('killall karmon')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system(jobs)
 
    os.system('clear')

    actions()

actions()




