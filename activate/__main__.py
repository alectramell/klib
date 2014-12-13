#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('KARMON$ ')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system(jobs)
 
    actions()

actions()




