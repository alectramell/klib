#!/usr/bin/python

import os
import getpass

os.system('clear')

def actions(): 
    jobs = raw_input('Run command(s): ')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system('gnome-terminal --title="Karmon v1.0 | Terminal.." -x sh -c "' + jobs + '"')

actions()

os.system('clear')




