# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
'''Bot stuff
Client ID: 391247384618729483
Client Secret: IhEXpbkRUFaNFOILqvAfJrnPma5UtIXa
Username: Teddy_V2#2004
Token: MzkxMjQ3Mzg0NjE4NzI5NDgz.DRWIGA.Xykn4_vPbh0UAnYBOt0iKTyNqUY
'''

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import datetime
import urllib.request



client = Bot(description="Teddy_V2 by teddy robbins", command_prefix="!", pm_help = False)

@client.event
async def on_ready():
		print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
		print('--------')
		print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
		print('--------')
		print('Use this link to invite {}:'.format(client.user.name))
		print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
		print('--------')

@client.event
async def on_message(message):
	if message.content.upper().startswith("!SAY"): #say stuff
		await client.send_message(message.channel, message.content[5:])
	elif message.content.upper().startswith("!HELP"):
		await client.send_message(message.channel, "Check your dms!")
		await client.send_message(message.author, "Command prefix is !")
		await client.send_message(message.author, "say: make me say anything, duh")
		await client.send_message(message.author, "math: do math using python syntax")
		await client.send_message(message.author, "dankmeme: gets you a fresh meme from the front page of r/dankmemes")
		await client.send_message(message.author, "convert: convert distance measurements, m, cm, mm, in, and ft")
		await client.send_message(message.author, "countdown: set a countdown to any date, what are you waiting for?")
		await client.send_message(message.author, "sourcecode: get my source code")
		await client.send_message(message.author, "lcgit: get the robotics github")
		await client.send_message(message.author, "---------------------------------")
	elif message.content.upper().startswith("!SOURCECODE"): #bot's github
		await client.send_message(message.channel, "https://github.com/trobb20/Trobb_V2")
	elif message.content.upper().startswith("!LCGIT"): #lc github
		await client.send_message(message.channel, "https://github.com/trobb20/LC_Robotics_18")
	elif message.content.upper().startswith("!CONVERT"): #convert command
		await client.send_message(message.channel,"Type starting units:")
		ratioD1 = 0.
		type1 = await client.wait_for_message(author=message.author)
		type1_text = type1.content.upper()
		if type1_text=="M":
			ratioD1 = 1.
		elif type1_text=="CM":
			ratioD1 = 100.
		elif type1_text=="MM":
			ratioD1 = 1000.
		elif type1_text=="FT":
			ratioD1 = 3.28
		elif type1_text=="IN":
			ratioD1 = 12*3.28
		else:
			await client.send_message(message.channel, "Invalid unit.")
		await client.send_message(message.channel, "Type final units:")
		ratioD2 = 0.
		type2 = await client.wait_for_message(author=message.author)
		type2_text = type2.content.upper()
		if type2_text=="M":
			ratioD2 = 1.
		elif type2_text=="CM":
			ratioD2 = 100.
		elif type2_text=="MM":
			ratioD2 = 1000.
		elif type2_text=="FT":
			ratioD2 = 3.28
		elif type2_text=="IN":
			ratioD2 = 12*3.28
		else:
			await client.send_message(message.channel, "Invalid unit.")
		await client.send_message(message.channel, "Type the number you want to convert:")
		numbermsg = await client.wait_for_message(author=message.author)
		number=float(numbermsg.content)
		final = str(number*(ratioD2/ratioD1))
		'''await client.send_message(message.channel, "TELEMETRY")
		await client.send_message(message.channel, str(type1_text))
		await client.send_message(message.channel, str(type2_text))
		await client.send_message(message.channel, str(ratioD1))
		await client.send_message(message.channel, str(ratioD2))
		await client.send_message(message.channel, str(number))'''
		await client.send_message(message.channel, "Your conversion is:")
		await client.send_message(message.channel, final+" "+type2_text.lower())
	elif message.content.upper().startswith("!QUOTE"):
		try:
			quoteF = open('quotes.txt','r',encoding="utf8")
		except:
			await client.send_message(message.channel, "Error opening quotes file")

		quoteIndex = random.randint(0,49)
		quoteL = quoteF.readlines()
		quoteS = quoteL[quoteIndex].rstrip("\n")
		await client.send_message(message.channel, quoteS)
		quoteF.close()
	elif message.content.upper().startswith("!SUPREMELEADER"):
		await client.send_message(message.channel, "Our supreme leader is Teddy, bow before his robotics abilities.")
	elif message.content.upper().startswith("!COUNTDOWN"):
		await client.send_message(message.channel, "Access Countdown or Create New? (type access or new)")
		answer = await client.wait_for_message(author=message.author)
		answerContent = answer.content.lower()
		if answerContent == "access":
			countdownF = open("countdowns.txt","r",encoding="utf8")
			await client.send_message(message.channel, "Input Countdown Name")
			namemsg=await client.wait_for_message(author=message.author)
			name=namemsg.content.lower()
			for line in countdownF.readlines():
				L = line.split(",")
				if L[0]==name:
					targetyear=int(L[1])
					targetmonth=int(L[2])
					targetday=int(L[3].rstrip("\n"))
					targetdate=datetime.date(targetyear,targetmonth,targetday)
					now = datetime.datetime.now()
					currentdate=datetime.date(now.year,now.month,now.day)
					deltadate = targetdate-currentdate
					daysLeft = deltadate.days
					monthsLeft=0
					yearsLeft=0
					if daysLeft>365:
						yearsLeft = int(daysLeft) // 365
						daysLeft = daysLeft%365
					if daysLeft>30:
						monthsLeft = int(daysLeft) // 30
						daysLeft = daysLeft%30
					await client.send_message(message.channel, "There are %s year(s) %s month(s) and %s day(s) until the target date"%(yearsLeft,monthsLeft,daysLeft))

		elif answerContent == "new":
			await client.send_message(message.channel, "Input Countdown Name, no spaces please")
			namemsg=await client.wait_for_message(author=message.author)
			name=namemsg.content.lower()
			await client.send_message(message.channel, "Input Target Date as mm/dd/yyyy")
			datemsg=await client.wait_for_message(author=message.author)
			dateS=datemsg.content
			targetmonth=int(dateS[0:2])
			targetday = int(dateS[3:5])
			targetyear = int(dateS[6:])
			targetdate=datetime.date(targetyear,targetmonth,targetday)
			now = datetime.datetime.now()
			currentdate=datetime.date(now.year,now.month,now.day)
			deltadate = targetdate-currentdate
			daysLeft = deltadate.days
			monthsLeft=0
			yearsLeft=0
			if daysLeft>365:
				yearsLeft = int(daysLeft) // 365
				daysLeft = daysLeft%365
			if daysLeft>30:
				monthsLeft = int(daysLeft) // 30
				daysLeft = daysLeft%30
			await client.send_message(message.channel, "There are %s year(s) %s month(s) and %s day(s) until the target date"%(yearsLeft,monthsLeft,daysLeft))

			countdownF = open("countdowns.txt","a",encoding="utf8")
			countdownF.write("%s,%d,%d,%d"%(str(name),targetyear,targetmonth,targetday)+"\n")
			countdownF.close()

			await client.send_message(message.channel, "Countdown saved")
	elif message.content.upper().startswith("!MATH"):
		await client.send_message(message.channel, "Input your expression in python format")
		expressmsg=await client.wait_for_message(author=message.author)
		express=expressmsg.content
		try:
			final = str(eval(express))
			await client.send_message(message.channel, "Your answer is: "+final)
		except:
			await client.send_message(message.channel, "I could not understand your expression")
	elif message.content.upper().startswith("!DANKMEME"):
		await client.send_message(message.channel, "Finding you a good meme, this may take a sec...")
		links=[]
		try:
			with urllib.request.urlopen('https://www.reddit.com/r/dankmemes/') as response:
			   html = response.read().decode("utf8")
		except:
			await client.send_message(message.channel, "Unfortunately, our meme source is overwhelmed by requests, check back again soon!")
		else:
			startIndex=html.find('<div id="siteTable"')
			#print(startIndex)
			endIndex=html.find('<div class="nav-buttons">')
			#print(endIndex)
			startLinkIndex=startIndex

			for i in range(0,27):
				startLinkIndex=html.find('data-url="',startLinkIndex,endIndex)+10
				#print(startLinkIndex)
				i=startLinkIndex

				while True:
					if html[i]=='"':
						endLinkIndex=i
						break
					i=i+1
				#print(endLinkIndex)
				currentLink = html[startLinkIndex:endLinkIndex]
				links.append(currentLink)
				i=i+1
				startLinkIndex=endLinkIndex+1

			memeIndex = random.randint(0,len(links))
			await client.send_message(message.channel, links[memeIndex])
			await client.send_message(message.channel, "Enjoy your meme!")
	elif message.author.nick.lower() == "griffin":
		await client.send_message(message.author, "https://i.kinja-img.com/gawker-media/image/upload/s--Dsm8Ht6G--/c_scale,fl_progressive,q_80,w_800/v4dcuuxjgvs2tixanwhh.png")







client.run('MzkxMjQ3Mzg0NjE4NzI5NDgz.DRWIGA.Xykn4_vPbh0UAnYBOt0iKTyNqUY')
# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
