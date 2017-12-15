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
    elif message.content.upper().startswith("!SOURCECODE"): #bot's github
        await client.send_message(message.channel, "https://github.com/trobb20/Trobb_V2")
    elif message.content.upper().startswith("!LCGIT"): #lc github
        await client.send_message(message,channel, "https://github.com/trobb20/LC_Robotics_18")
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
        quoteF = open('quotes.txt','r')
        quoteIndex = random.randint(0,49)
        quoteL = quoteF.readlines()
        quoteS = quoteL[quoteIndex].rstrip("\n")
        await client.send_message(message.channel, quoteS)
    elif message.content.upper().startswith("!SUPREMELEADER"):
        await client.send_message(message.channel, "Our supreme leader is Teddy, bow before his robotics abilities.")





client.run('MzkxMjQ3Mzg0NjE4NzI5NDgz.DRWIGA.Xykn4_vPbh0UAnYBOt0iKTyNqUY')
# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
