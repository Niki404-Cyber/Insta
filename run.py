#coding=utf-8
import os, sys, platform
try:os.system('rm -rf nikig')
except:pass
try:os.system('xdg-open https://youtube.com/@Niki404-Cyber')
except:pass
try:
    if sys.argv[1]=='update':
        os.system('rm -rf nikig')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('nikig'):
        os.system('curl -L https://github.com/Niki404-Cyber/Insta/blob/main/nikig?raw=true -o nikig')
        os.system('chmod 777 nikig;./nikig')
    else:
        os.system('chmod 777 nikig;./nikig')
