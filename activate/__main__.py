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

    if jobs == ('create a website'):
       os.system('clear')
       name = raw_input('What would you like to call it?: ')
       os.system('clear')
       newsite = str('mkdir ~/Desktop/' + name + '/')
       os.system(newsite)
       newindex = str('touch ~/Desktop/' + name + '/index.html')
       os.system(newindex)
       addcode = str('echo "<!DOCTYPE html>" > ~/Desktop/' + name + '/index.html')
       addcode2 = str('echo "<html>" >> ~/Desktop/' + name + '/index.html')
       addcode3 = str('echo "<head><title>This site is called ' + name + '</title></head>" >> ~/Desktop/' + name + '/index.html')
       addcode4 = str('echo "<body>" >> ~/Desktop/' + name + '/index.html')
       addcode5 = str('echo "<marquee behavior=slide direction=left scrollamount=25><font face=ubuntu size=7 color=#000000><b>' + name + '</b></font></marquee>" >> ~/Desktop/' + name + '/index.html')
       addcode6 = str('echo "</body>" >> ~/Desktop/' + name + '/index.html')
       addcode7 = str('echo "</html>" >> ~/Desktop/' + name + '/index.html')
       os.system(addcode)
       os.system(addcode2)
       os.system(addcode3)
       os.system(addcode4)
       os.system(addcode5)
       os.system(addcode6)
       os.system(addcode7)
       os.system('sensible-browser --new-window="~/Desktop/' + name + '/index.html"')
       os.system('clear')

    if jobs == ('make a website'):
       os.system('clear')
       name = raw_input('What would you like to call it?: ')
       os.system('clear')
       newsite = str('mkdir ~/Desktop/' + name + '/')
       os.system(newsite)
       newindex = str('touch ~/Desktop/' + name + '/index.html')
       os.system(newindex)
       addcode = str('echo "<!DOCTYPE html>" > ~/Desktop/' + name + '/index.html')
       addcode2 = str('echo "<html>" >> ~/Desktop/' + name + '/index.html')
       addcode3 = str('echo "<head><title>This site is called ' + name + '</title></head>" >> ~/Desktop/' + name + '/index.html')
       addcode4 = str('echo "<body>" >> ~/Desktop/' + name + '/index.html')
       addcode5 = str('echo "<marquee behavior=slide direction=left scrollamount=25><font face=ubuntu size=7 color=#000000><b>' + name + '</b></font></marquee>" >> ~/Desktop/' + name + '/index.html')
       addcode6 = str('echo "</body>" >> ~/Desktop/' + name + '/index.html')
       addcode7 = str('echo "</html>" >> ~/Desktop/' + name + '/index.html')
       os.system(addcode)
       os.system(addcode2)
       os.system(addcode3)
       os.system(addcode4)
       os.system(addcode5)
       os.system(addcode6)
       os.system(addcode7)
       os.system('sensible-browser --new-window="~/Desktop/' + name + '/index.html"')
       os.system('clear')

    if jobs == ('create a site'):
       os.system('clear')
       name = raw_input('What would you like to call it?: ')
       os.system('clear')
       newsite = str('mkdir ~/Desktop/' + name + '/')
       os.system(newsite)
       newindex = str('touch ~/Desktop/' + name + '/index.html')
       os.system(newindex)
       addcode = str('echo "<!DOCTYPE html>" > ~/Desktop/' + name + '/index.html')
       addcode2 = str('echo "<html>" >> ~/Desktop/' + name + '/index.html')
       addcode3 = str('echo "<head><title>This site is called ' + name + '</title></head>" >> ~/Desktop/' + name + '/index.html')
       addcode4 = str('echo "<body>" >> ~/Desktop/' + name + '/index.html')
       addcode5 = str('echo "<marquee behavior=slide direction=left scrollamount=25><font face=ubuntu size=7 color=#000000><b>' + name + '</b></font></marquee>" >> ~/Desktop/' + name + '/index.html')
       addcode6 = str('echo "</body>" >> ~/Desktop/' + name + '/index.html')
       addcode7 = str('echo "</html>" >> ~/Desktop/' + name + '/index.html')
       os.system(addcode)
       os.system(addcode2)
       os.system(addcode3)
       os.system(addcode4)
       os.system(addcode5)
       os.system(addcode6)
       os.system(addcode7)
       os.system('sensible-browser --new-window="~/Desktop/' + name + '/index.html"')
       os.system('clear')

    if jobs == ('make a site'):
       os.system('clear')
       name = raw_input('What would you like to call it?: ')
       os.system('clear')
       newsite = str('mkdir ~/Desktop/' + name + '/')
       os.system(newsite)
       newindex = str('touch ~/Desktop/' + name + '/index.html')
       os.system(newindex)
       addcode = str('echo "<!DOCTYPE html>" > ~/Desktop/' + name + '/index.html')
       addcode2 = str('echo "<html>" >> ~/Desktop/' + name + '/index.html')
       addcode3 = str('echo "<head><title>This site is called ' + name + '</title></head>" >> ~/Desktop/' + name + '/index.html')
       addcode4 = str('echo "<body>" >> ~/Desktop/' + name + '/index.html')
       addcode5 = str('echo "<marquee behavior=slide direction=left scrollamount=25><font face=ubuntu size=7 color=#000000><b>' + name + '</b></font></marquee>" >> ~/Desktop/' + name + '/index.html')
       addcode6 = str('echo "</body>" >> ~/Desktop/' + name + '/index.html')
       addcode7 = str('echo "</html>" >> ~/Desktop/' + name + '/index.html')
       os.system(addcode)
       os.system(addcode2)
       os.system(addcode3)
       os.system(addcode4)
       os.system(addcode5)
       os.system(addcode6)
       os.system(addcode7)
       os.system('sensible-browser --new-window="~/Desktop/' + name + '/index.html"')
       os.system('clear')

actions()






