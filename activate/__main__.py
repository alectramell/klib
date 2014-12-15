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

    if jobs == ('skype'):
       os.system('clear')
       os.system('CONTACT=$(zenity --entry --text="Message User:" --title="Skype..") && skype:$CONTACT?chat &')

    username = getpass.getuser()
    username = str(username)

    os.system('clear')

    os.system(jobs)
 
    os.system('clear')

    actions()

actions()




