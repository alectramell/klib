#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('[Karmon v1.0]$ ')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system(jobs)

actions()

os.system('clear')




