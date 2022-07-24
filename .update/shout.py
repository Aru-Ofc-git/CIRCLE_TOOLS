# -*- coding: UTF-8 -*-
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: sumarr
#!/usr/bin/env python3
#coded by ARU
#Aiful Islam Arman
#ARU Circle Tools
import os,sys,json,time
try:
	import requests
except:
	os.system("pip install requests")
	import requests

# Color Val
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'
purple = "\033[0;35m"
os.system("clear")

def header():
	os.chdir("..")
	os.system("lolcat banner.sh")
	os.chdir(".Text")
	os.system("lolcat MyText.txt")
	
	
def logoprint(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)
        

def main():
	while True:
		user=str(input(green+"\n     Enter Circle ID: "+yellow))
		if user != "":
			
			
			from requests.structures import CaseInsensitiveDict
		#	key=requests.get("https://pastebin.com/raw/RptmpLnK").text
			key="3c614faafa20eda7cfe001fbf5d0974d"
			url = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getMLStatusList&nickname="+user
			headers = CaseInsensitiveDict()
			headers["x-api-key"] = key
			headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
			resp = requests.get(url, headers=headers)
			os.system("clear")
			header()
			print(green+ "\n\n     Your Shout Loading...")
			time.sleep(3)
			os.system("clear")
			header()
			
			print(green+"\n     Your ID: "+yellow+user)
			time.sleep(2)
			y=resp.json()["data"]
			i=0
			for i in range(len(y)):
				print("\n\n   "+green+resp.json()["data"][i]["st"])
				time.sleep(0.3)
				i+1
			break
			
		else:
			print(red+"\n     Please Enter Valid ID")
			
	enter=str(input(yellow+"\n\n     Press Enter For Again Find "+purple))
	if enter=="":
			os.chdir("..")
			os.chdir(".update")
			os.system("python shout.py")
			time.sleep(3)
	else:
		sys.exit()


try:
    header()
    main()
except KeyboardInterrupt:
    sys.exit()