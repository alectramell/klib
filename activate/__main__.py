#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('[GHOST]$')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system('touch ~/Desktop/karmon.log')
    log = str('echo ' + jobs + ' >> ~/Desktop/karmon.log')

    os.system(log)

actions()

os.system('clear')




