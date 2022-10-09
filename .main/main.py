#Codded By Ariful Islam Arman (ARU)
#writen With python


import os,time,json,sys,random
# color
#Color Value 
blueVal="94m"
redVal = "91m"
greenVal= "32m"
whiteVal= "97m"
yellowVal="93m"
cyanVal= "96m"
#normal
normal = "\33["
#Bold
bold = "\033[1;"
#italic
italic = "\x1B[3m"
#Color Normal
blue = normal + blueVal #Blue Color Normal
red = normal + redVal #Red Color Normal
green = normal + greenVal #Green Color Normal
white = normal + whiteVal #white Color Normal
yellow = normal + yellowVal #yellow Color Normal
cyan = normal + cyanVal #Cyan Color Normal
#Color Bold
blueBold = bold + blueVal #Blue Color Bold
redBold = bold + redVal #Red Color Bold
greenBold = bold + greenVal #Green Color Bold
whiteBold = bold + whiteVal #white Color Bold
yellowBold = bold + yellowVal #yellow Color Bold
cyanBold = bold + cyanVal #Cyan Color Bold
#Close Color
end = '\033[0m'   

option='''

    [1] Number To ID or ID To Number
    [2] Get API with OTP
    [3] API to ID
    [4] Following Check
    [5] Follower Check
    [6] Check Block List
    [7] Following Clean
    [8] Follower Clean
    [9] Block Clean
    [10] CIRCLE PIN [Not available For Harassments Issue]
    [11] Clean Those People who not Joined  your CIRCLE
    [12] Join Those People you not joined his/her CIRCLE.
    [13] Change Nickname
    [14] Change Gender
    [15] Change Birthday
    [16] Send CPOKE
    [17] Send Unlimited CPOKE
    [18] Send CCOM
    [19] Send Unlimited CCOM
    [20] Shout
    [21] Unlimited Shout
    [22] Unlimited Join And xjoin [Not available For Harassments Issue]
    [23] Chek User Update
    [24] Get Latest Update in Apps
    [25] Reactive CIRCLE ID
    [26] Stop CIRCLE ID
    [27] Connect Us
    [28] Update PIP
'''
connectOptions = '''

    [1] GitHub
    [2] Facebook
    [3] Chat with admin
    [4] Instagram
    [5] YouTube    
'''
colorArr = ["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"]

#Char Print
def printchar(w,t): #w=word and t =time
    for word in w + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(t)
#Import All Module   
try:
	import requests
except:
	printchar(cyanBold+"installing requests.....",0.05)
	time.sleep(2)
	os.system("pip install requests")
	import requests
	printchar(greenBold+"requests successfully installed.....",0.05)
	time.sleep(2)
	os.system('clear')
try:
	from circle import robicircle
except:
	printchar(cyanBold+"installing circlerobi.....",0.05)
	time.sleep(2)
	os.system("pip install circlerobi")
	import circle
	printchar(greenBold+"circlerobi successfully installed.....",0.05)
	time.sleep(2)
	os.system('clear')
#Banner FuncTion
def banner():
	os.chdir(".additionalText")
	os.system("lolcat banner.ts")
	os.system("lolcat toolsInfo.txt")
	os.chdir("..")
#connect
def connect():
		time.sleep(1)
		os.system("clear")
		banner()
		printchar(random.choice(colorArr)+connectOptions,0.005)
		inputConnectOption = str(input(random.choice(colorArr)+"    [>] Chosse a Option: "+random.choice(colorArr)))
		if inputConnectOption == "1":
			os.system('xdg-open https://github.com/Aru-Ofc-git/')
			time.sleep(5)
			main()
		elif inputConnectOption == "2":
			os.system('xdg-open https://www.facebook.com/Aru.Ofc/')
			time.sleep(5)
			main()
		elif inputConnectOption == "3":
			os.system('xdg-open https://m.me/1R13A14')
			time.sleep(5)
			main()
		elif inputConnectOption == "4":
			os.system('xdg-open https://www.instagram.com/aru.ofc.ins/')
			time.sleep(5)
			main()
		elif inputConnectOption == "5":
			os.system('xdg-open https://youtube.com/c/ARULyrics1')
			time.sleep(5)
			main()
		else:
			printchar(redBold+"\n    Invalid input",0.01)
			time.sleep(4)
			connect()
			
def main():
	os.system("clear")
	banner()
	colorOptions = random.choice(colorArr)
	printchar(colorOptions+option,0.005)	
	inputOption = str(input(random.choice(colorArr)+"    [>] Choose a option: "+random.choice(colorArr)))
	if inputOption =="1":
		time.sleep(1)
		os.system("clear")
		banner()
		idOrNum = str(input(random.choice(colorArr)+"\n\n    [>] Enter ID or Number: "+random.choice(colorArr)))
		if idOrNum.isnumeric():
			print("\n")
			robicircle.numbertoid(idOrNum)
		else:
			print("\n")
			robicircle.idtonumber(idOrNum)
	elif inputOption =="2":
		time.sleep(1)
		os.system("clear")
		banner()
		number = str(input(random.choice(colorArr)+"\n\n    [>] Enter Number: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"    Number: "+random.choice(colorArr)+"+88"+number,0.01)
		robicircle.requforapi(number)
		otp = str(input(random.choice(colorArr)+"\n\n    [>] Enter OTP: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		robicircle.getapi(number,otp)
		print("\n")		
	elif inputOption =="3":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		print("\n")
		robicircle.apitoid(api)
		
	elif inputOption =="4":
		time.sleep(1)
		os.system("clear")
		banner()
		CircleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		robicircle.flgcheck(CircleID)

	elif inputOption =="5":
		time.sleep(1)
		os.system("clear")
		banner()
		CircleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		robicircle.folcheck(CircleID)
	
	
	elif inputOption =="6":
		time.sleep(1)
		os.system("clear")
		banner()
		ApiKey = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		robicircle.blockcheck(ApiKey)
				
	
	elif inputOption =="7":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.flgclean(api)
		
	elif inputOption =="8":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.folclean(api)
		
		
	elif inputOption =="9":
		time.sleep(1)
		os.system("clear")
		banner()
		ApiKey = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		robicircle.blockclean(ApiKey)
		
	
	elif inputOption =="10":
		printchar(redBold+"\n    Not available For Harassments Issue",0.05)
		time.sleep(5)
		main()
	
	elif inputOption =="11":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.notinyour(api)
		
	elif inputOption =="12":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.notin(api)
		
	elif inputOption =="13":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		name = str(input(random.choice(colorArr)+"\n\n    [>] Enter Name: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.name(api,name)
		
	elif inputOption =="14":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		gender = str(input(random.choice(colorArr)+"\n\n    [>] Enter Gender M/F: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.gender(api,gender)
		
	elif inputOption =="15":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		birthday = str(input(random.choice(colorArr)+"\n\n    [>] Enter Birthday YYYY-MM-DD: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		robicircle.birthday(api,birthday)

	elif inputOption =="16":
		time.sleep(1)
		os.system("clear")
		banner()
		circleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		print("\n")
		robicircle.autoCp(api,circleID,message)
		
	elif inputOption =="17":
		time.sleep(1)
		os.system("clear")
		banner()
		circleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		while True:
			print("\n")
			robicircle.autoCp(api,circleID,message)

	elif inputOption =="18":
		time.sleep(1)
		os.system("clear")
		banner()
		circleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		print("\n")
		robicircle.autoCom(api,circleID,message)
		
	elif inputOption =="19":
		time.sleep(1)
		os.system("clear")
		banner()
		circleID = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		while True:
			print("\n")
			robicircle.autoCom(api,circleID,message)

	elif inputOption =="20":
		time.sleep(1)
		os.system("clear")
		banner()
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		print("\n")
		robicircle.autoShout(api,message)
		
	elif inputOption =="21":
		time.sleep(1)
		os.system("clear")
		banner()
		message = str(input(random.choice(colorArr)+"\n\n    [>] Enter Message: "+random.choice(colorArr)))
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		os.system("clear")
		banner()
		print("\n")
		printchar(random.choice(colorArr)+"     API Key: "+random.choice(colorArr)+api,0.01)
		while True:
			print("\n")
			robicircle.autoShout(api,message)	
	elif inputOption =="22":
		printchar(redBold+"\n    Not available For Harassments Issue",0.05)
		time.sleep(5)
		main()			
	elif inputOption =="23":
		time.sleep(1)
		os.system("clear")
		banner()
		user = str(input(random.choice(colorArr)+"\n\n    [>] Enter CIRCLE ID: "+random.choice(colorArr)))
		time.sleep(2)
		print("\n")
		robicircle.updateUser(user)	
	elif inputOption =="24":
		time.sleep(1)
		os.system("clear")
		banner()
		print("\n")
		robicircle.updateInapp()
	elif inputOption =="25":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		print("\n")
		robicircle.creg(api)	
	elif inputOption =="26":
		time.sleep(1)
		os.system("clear")
		banner()
		api = str(input(random.choice(colorArr)+"\n\n    [>] Enter API Key: "+random.choice(colorArr)))
		time.sleep(2)
		print("\n")
		robicircle.cstop(api)
	elif inputOption =="27":
		connect()
	elif inputOption =="28":
		os.system("clear")
		banner()
		os.chdir(".additionalText")
		os.system("bash upgrade.sh")
		
	else:
		printchar(redBold+"\n    Invalid input",0.01)
		time.sleep(4)
		main()	

try:
	main()
except:
	printchar(redBold+'     Found a error')
