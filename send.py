#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
	print('Error !! : Some dependencies are not installed')
	print("Error Occurred!!!\nUsing Basic version")
	time.sleep(4)
	os.system('bash send.sh --sendsms')

# colors
yellow='\033[93m'
green='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

# The Credit For This Code Goes To Panda Hackers https://github.com/HACK3RY2J/
# And The Contributors Mentioned At https://github.com/HACK3RY2J/Anon-SMS/

def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """                                                  
     \033[0m████████████████████████████████████████████████████████████████████
     \033[0m████\033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\033[0m████
     \033[0m██\033[92m▒▒\033[0m██         \033[93m___   _  ______  _  __ \033[94m   ______  _______      \033[0m██\033[92m▒▒\033[0m██
     \033[0m██  \033[92m▒▒\033[0m██      \033[93m/ _ | / |/ / __ \/ |/ /_\033[94m__/ __/  |/  / __/    \033[0m██\033[92m▒▒  \033[0m██
     \033[0m██    \033[92m▒▒\033[0m██   \033[93m/ __ |/    / /_/ /    /__\033[94m_/\ \/ /|_/ /\ \    \033[0m██\033[92m▒▒    \033[0m██
     \033[0m██      \033[92m▒▒\033[0m██\033[93m/_/ |_/_/|_/\____/_/|_/   \033[94m/___/_/  /_/___/  \033[0m██\033[92m▒▒      \033[0m██
     \033[0m██        \033[92m▒▒\033[0m██                                   \033[91mV1.4 \033[0m██\033[92m▒▒        \033[0m██
     \033[0m██          \033[92m▒▒\033[0m████████████████████████████████████████\033[92m▒▒          \033[0m██
     \033[0m██            \033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            \033[0m██
     \033[0m██     \033[94mCoded by: https://github.com/HACK3RY2J                     \033[0m██
     \033[0m██     \033[94mYoutube : https://www.youtube.com/c/PandaHackers           \033[0m██
     \033[0m██    \033[94mTelegram : https://t.me/itzAnonSMS                          \033[0m██
     \033[0m██                                                                ██
     \033[0m████████████████████████████████████████████████████████████████████
     \033[92m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                                         """
    print(logo)
    print("\n")

def Track() :
  TXTID = input("Enter Text ID of Anon-SMS \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPress Enter To Exit..")
  print("\nThanks For Using Anon-Sms..")
  print("\tWe Hope To See You Again\n Type bash Run.sh\n\tTo Run Again..")
  exit()

def update():
    stuff_to_update = ['send.py', 'Run.sh', '.version']
    for stuff in stuff_to_update:
        dat = urllib.request.urlopen("https://raw.githubusercontent.com/HACK3RY2J/Anon-SMS/master/" + stuff).read()
        file = open(stuff, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tRun The Script Again...')
    exit()

def checkConnection():
	try:
		urllib.request.urlopen('https://www.google.com')
	except Exception:
		print("Error While Connecting To Internet!!!")
		print("\tPlease Connect To Internet To Continue...\n")
		input('Exiting....\n Press Enter To Exit....')
		exit()

def checkUpdate():
	print('\tChecking For Updates...')
	ver = urllib.request.urlopen("https://raw.githubusercontent.com/HACK3RY2J/Anon-SMS/master/.version").read().decode(
		'utf-8')
	verl = ''
	try:
		verl = open(".version", 'r').read()
	except Exception:
		pass
	if ver != verl:
		print('\n\t\tAn Update is Available....')
		print('\tUpdating Anon-SMS...')
		update()
	print("Congratulation")
	print("Your Version is Up-To-Date")
	print('\n\tStarting Anon-SMS...\n')

if os.path.exists(".Apis") :
	apiList = open(".Apis", "r")
	api = apiList.readline()
	print("API Key : ",api)
	apiList.close()
else :
    api = 'textbelt'
    print("Using Default API : ", api)

clr()
banner()
checkConnection()
checkUpdate()

try:
    noti = urllib.request.urlopen("https://raw.githubusercontent.com/HACK3RY2J/Anon-SMS/master/.notify").read().decode('utf-8')
    if len(noti) > 10:
        print('\nNotification : ' + noti + '\n')
except Exception:
    pass
    

while True:
	print("\033[0mThis Tool Is Used To Send Anonymous Messages")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
	elif sys.argv[1] == "Add":
		type = 2
except Exception:
	type = 0
if type == 1:
	print("Track The Anonymous Message You Sent Using This Tool.")
	print()
	Track()
elif type == 0:
	while True:
		print("Enter The Details Of The Person You Want To Send Anonymous Message")
		cc = input("\tEnter Country Code (Without +) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
		        continue
		pn = input("Enter Phone Number : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nInvalid Phone Number..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nPhone Number Must Consist Of Numbers Only\n')
		            continue
		receiver = '+' + numbe
		text = input("Enter Message to send : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : api
		})
		
		print(resp.json())
		if '"success" : true ' in resp.text:
		    print("\033[92m Message Sent Succesfully \033[0m")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		if '"success" : false ' in resp.text:
		    print("\033[91m Error Occured")
		    print("\033[91m Failed to send SMS! ")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		exit() 
elif type == 2:
	addAPI = input("Enter API Key to Add : ")
	if os.path.exists(".Apis"):
		print("Clearing Older API.\n\n")
		time.sleep(0.3)
		print("Added new API Key\n\n")
		time.sleep(0.2)
		print("Returning To Main Menu")
		time.sleep(2)
		os.system("bash Run.sh")
	else:
		os.system("touch .Apis")
		addingAPI = open(".Apis", "w")
		addingAPI.write(addAPI)
		time.sleep(2)
		addingAPI.close()
		print("API Added Successfully!!!\n\n\n")
		time.sleep(0.8)
		print("\t\tReturning To Main Menu")
		time.sleep(2)
		os.system("bash Run.sh")
