#coding=utf-8
import os, sys, platform
try:os.system('rm -rf ig64')
except:pass
try:os.system('xdg-open https://youtube.com/@Niki404-Cyber')
except:pass
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ig64')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ig64'):
        os.system('curl -L https://github.com/Niki404-Cyber/Insta/blob/main/ig64?raw=true -o ig64')
        os.system('chmod 777 ig64;./ig64')
    else:
        os.system('chmod 777 ig64;./ig64')
