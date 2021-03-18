'''
Author: Neek Panchal
ID: 200804310
Email: panc4310@mylaurier.ca
__updated__ = "2021-01-14"
'''

# Imports (Libraries)

import asyncio
import builtins
import random
import time


from bs4 import BeautifulSoup
from discord import channel, member, __author__
from discord.utils import get
import discord
import requests

from discord.ext import commands
from hawkfunctions import CHAMPKDA
from hawkfunctions import KDA
from hawkfunctions import LIVE
from hawkfunctions import RANK
from hawkfunctions import SNIPE
from hawkfunctions import TOKEN
         
    

# Imports (Functions)
class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='h!help'))
    
    
    async def on_message_delete(self, message):
        global user, usermessage, userlist
        
        userlist = []
        user = str(message.author)
        usermessage = message.content
        
        userlist.append(user)
        userlist.append(usermessage)
        
        await asyncio.sleep(86400)
        user = None
        usermessage = None
        userlist = None
        
    async def on_message(self, message):
        print(message.channel, ':', 'Message from {0.author}: {0.content}'.format(message))
        
        if message.content.lower().startswith('h!ping'):
            await message.channel.send('My ping is ' + str(round((client.latency*1000), 2)) + ' ms')
        
                
        if str(message.author) == 'Dyno#3861':
            spam = ["shutup uwu bot", "uwu bot == gay", "/ban uwu bot", ">:("]
            await message.channel.send(random.choice(spam))
        
        if message.content.lower().startswith('h!snipe'):
            
            try:
            
                sender = userlist[0]
                sendersmessage = userlist[1]
                embed = SNIPE(sender, sendersmessage)
                await message.channel.send(embed=embed)
                
            except:
                
                await message.channel.send('Theres nothing to snipe!')
                
        if message.content.lower().startswith('h!kda'):
            
            user = ''
            for x in range(len(message.content)):
                if x > 5:
                    user += message.content[x]
            user = user.strip()
    
            try:
                
                embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
                embed = discord.Embed(title="Champion Statistics", description="(based on current season)", color=0xf20707)
                embed.set_author(name="League", icon_url="https://static.wikia.nocookie.net/leagueoflegends/images/9/9a/League_of_Legends_Update_Logo_Concept_05.jpg/revision/latest/top-crop/width/300/height/300?cb=20191029062637")
                embed.add_field(name=KDA(user), value='Champ K/D/A:1', inline=True)
                embed.set_thumbnail(url="https://o.aolcdn.com/images/dims?quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fuu%2Fapi%2Fres%2F1.2%2Fa5CAEgO_cWGwhB9slSRxvQ--%7EB%2FaD0xMjAwO3c9MTgwMDthcHBpZD15dGFjaHlvbg--%2Fhttps%3A%2F%2Fo.aolcdn.com%2Fimages%2Fdims%3Fresize%3D2000%252C2000%252Cshrink%26image_uri%3Dhttps%253A%252F%252Fs.yimg.com%252Fos%252Fcreatr-uploaded-images%252F2020-03%252F0c280880-683f-11ea-9ffb-46d7e0435a1f%26client%3Da1acac3e1b3290917d92%26signature%3Dfa801e4c3997e16ad73e19e33a15f02ebfe52420&client=amp-blogside-v2&signature=863517ea1b015e17523671273e1bc501ff20cb83")
                embed.set_footer(text="Certified by Riot Games®")
                await message.channel.send(embed=embed)
                await message.channel.send('𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐒𝐞𝐚𝐬𝐨𝐧 𝐊𝐃𝐀 𝐟𝐨𝐫: ' + user)
                
            except:
                embed = discord.Embed(description="*pings MIA on KDA*")
                embed.set_thumbnail(url="https://i.redd.it/tyvpt1fy7b601.jpg")
                embed.add_field(name=user, value="😞", inline=False)
                await message.channel.send(embed=embed)
                
        if message.content.startswith('h!friends') or message.content.startswith('h!FRIENDS'):
            
            user = ''
            for x in range(len(message.content)):
                if x > 9:
                    user += message.content[x]
            user = user.strip()
            
            try:
                
                embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
                embed = discord.Embed(title="League Bestfriend List", description="(based on most frequent)", color=0xf20707)
                embed.set_author(name="League", icon_url="https://static.wikia.nocookie.net/leagueoflegends/images/9/9a/League_of_Legends_Update_Logo_Concept_05.jpg/revision/latest/top-crop/width/300/height/300?cb=20191029062637")
                embed.add_field(name=LIVE(user), value='Bestfriend List', inline=True)
                embed.set_thumbnail(url="https://o.aolcdn.com/images/dims?quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fuu%2Fapi%2Fres%2F1.2%2Fa5CAEgO_cWGwhB9slSRxvQ--%7EB%2FaD0xMjAwO3c9MTgwMDthcHBpZD15dGFjaHlvbg--%2Fhttps%3A%2F%2Fo.aolcdn.com%2Fimages%2Fdims%3Fresize%3D2000%252C2000%252Cshrink%26image_uri%3Dhttps%253A%252F%252Fs.yimg.com%252Fos%252Fcreatr-uploaded-images%252F2020-03%252F0c280880-683f-11ea-9ffb-46d7e0435a1f%26client%3Da1acac3e1b3290917d92%26signature%3Dfa801e4c3997e16ad73e19e33a15f02ebfe52420&client=amp-blogside-v2&signature=863517ea1b015e17523671273e1bc501ff20cb83")
                embed.set_footer(text="Certified by Riot Games®")
                await message.channel.send(embed=embed)
                await message.channel.send('𝐏𝐥𝐚𝐲𝐞𝐫𝐬 𝐢𝐧 𝐇𝐢𝐬𝐭𝐨𝐫𝐲: ' + user)
                
            except:
                embed = discord.Embed(description="*pings MIA on Friends*")
                embed.set_thumbnail(url="https://i.redd.it/tyvpt1fy7b601.jpg")
                embed.add_field(name=user, value="😞", inline=False)
                await message.channel.send(embed=embed)
                
            
        if message.content.startswith('h!rank') or message.content.startswith('h!RANK'):
            
            user = ''
            for x in range(len(message.content)):
                if x > 6:
                    user += message.content[x]
            user = user.strip()
            
            try:
                
                embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
                embed = discord.Embed(title="League Solo/Duo Ranking", description="(based on current ranking)", color=0xf20707)
                embed.set_author(name="League", icon_url="https://static.wikia.nocookie.net/leagueoflegends/images/9/9a/League_of_Legends_Update_Logo_Concept_05.jpg/revision/latest/top-crop/width/300/height/300?cb=20191029062637")
                embed.add_field(name=RANK(user), value='Rank', inline=True)
                embed.set_thumbnail(url="https://o.aolcdn.com/images/dims?quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fuu%2Fapi%2Fres%2F1.2%2Fa5CAEgO_cWGwhB9slSRxvQ--%7EB%2FaD0xMjAwO3c9MTgwMDthcHBpZD15dGFjaHlvbg--%2Fhttps%3A%2F%2Fo.aolcdn.com%2Fimages%2Fdims%3Fresize%3D2000%252C2000%252Cshrink%26image_uri%3Dhttps%253A%252F%252Fs.yimg.com%252Fos%252Fcreatr-uploaded-images%252F2020-03%252F0c280880-683f-11ea-9ffb-46d7e0435a1f%26client%3Da1acac3e1b3290917d92%26signature%3Dfa801e4c3997e16ad73e19e33a15f02ebfe52420&client=amp-blogside-v2&signature=863517ea1b015e17523671273e1bc501ff20cb83")
                embed.set_footer(text="Certified by Riot Games®")
                await message.channel.send(embed=embed)
                await message.channel.send('𝐑𝐚𝐧𝐤: ' + user)
                
            except:
                embed = discord.Embed(description="*pings MIA on Rank*")
                embed.set_thumbnail(url="https://i.redd.it/tyvpt1fy7b601.jpg")
                embed.add_field(name=user, value="😞", inline=False)
                await message.channel.send(embed=embed)
                
        if message.content.startswith('h!champkda') or message.content.startswith('h!CHAMPKDA'):
            
            user = ''
            for x in range(len(message.content)):
                if x > 10:
                    user += message.content[x]
            user = user.strip()
            
            try:
                
                embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
                embed = discord.Embed(title="League Champion Stats KDA", description="(based on top five played)", color=0xf20707)
                embed.set_author(name="League", icon_url="https://static.wikia.nocookie.net/leagueoflegends/images/9/9a/League_of_Legends_Update_Logo_Concept_05.jpg/revision/latest/top-crop/width/300/height/300?cb=20191029062637")
                embed.add_field(name=CHAMPKDA(user), value='Champion History', inline=True)
                embed.set_thumbnail(url="https://o.aolcdn.com/images/dims?quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fuu%2Fapi%2Fres%2F1.2%2Fa5CAEgO_cWGwhB9slSRxvQ--%7EB%2FaD0xMjAwO3c9MTgwMDthcHBpZD15dGFjaHlvbg--%2Fhttps%3A%2F%2Fo.aolcdn.com%2Fimages%2Fdims%3Fresize%3D2000%252C2000%252Cshrink%26image_uri%3Dhttps%253A%252F%252Fs.yimg.com%252Fos%252Fcreatr-uploaded-images%252F2020-03%252F0c280880-683f-11ea-9ffb-46d7e0435a1f%26client%3Da1acac3e1b3290917d92%26signature%3Dfa801e4c3997e16ad73e19e33a15f02ebfe52420&client=amp-blogside-v2&signature=863517ea1b015e17523671273e1bc501ff20cb83")
                embed.set_footer(text="Certified by Riot Games®")
                await message.channel.send(embed=embed)
                await message.channel.send('𝐂𝐡𝐚𝐦𝐩𝐢𝐨𝐧 𝐊𝐃𝐀: ' + user)
                
            except:
                embed = discord.Embed(description="*pings MIA on Champion KDA History*")
                embed.set_thumbnail(url="https://i.redd.it/tyvpt1fy7b601.jpg")
                embed.add_field(name=user, value="😞", inline=False)
                await message.channel.send(embed=embed)
                
        if message.content.startswith('h!help'):
            embed=discord.Embed(title="Hawk Bot Command Centre", color=0x0008fa)
            embed.add_field(name="h!kda (user)", value="Returns Summoner KDA (X:1)", inline=False)
            embed.add_field(name="h!champkda (user)", value="Returns Champ Specific KDA (X/X/X)", inline=True)
            embed.add_field(name="h!friends (user)", value="Returns League Best Friends List", inline=True)
            embed.add_field(name="h!rank (user)", value="Returns Rank of User (Current Season)", inline=True)
            embed.add_field(name="h!snipe", value="Returns Last Deleted Message", inline=True)
            embed.add_field(name="h!msg", value="Sends a Special Message ;)", inline=True)
            embed.add_field(name="h!dank", value="Returns The Dank", inline=True)
            embed.set_footer(text="By: primo")
            await message.channel.send(embed=embed)
        
        if message.content.lower().startswith("league?"):
            await message.channel.send('<@&688824339306381337>')
            ping = round(((client.latency)*1000), 1)
            
            if ping < 30:
                await message.channel.send('<@!135842041677611008> ' + ' Will be able to play!')
                
                
            elif 30 < ping < 80:
                await message.channel.send('<@!135842041677611008> ' + 'Will be able to play but expect lag!')
                
                
            elif ping > 80:
                await message.channel.send('<@!135842041677611008> ' + 'Shouldnt play but when does he listen to me anyways lol.')
            
        if message.content.lower().replace(' ', '').startswith("risk?"):
            await message.channel.send('<@&794052701993828372>')
            
            
        if message.content.lower().startswith("csgo?"):
            await message.channel.send('<@&799409207580819467>')
            
        if message.content.startswith('<@&799409207580819467>'):
            ping = round(((client.latency)*1000), 1)
            
            if ping < 30:
                await message.channel.send('<@!135842041677611008> ' + ' Will be able to play!')
                
                
            elif 30 < ping < 80:
                await message.channel.send('<@!135842041677611008> ' + 'Will still be able to play but expect lag!')
                
                
            elif ping > 80:
                await message.channel.send('<@!135842041677611008> ' + 'Shouldnt play but when does he listen to me anyways lol.')
                
                
        if message.content.startswith("﷽"):
            user = message.author
            await user.add_roles(discord.utils.get(user.guild.roles, name='secret society'))
            await message.channel.send('مرحبا بكم في الجمعية السرية')
            time.sleep(3)
            await message.delete()
            
                
        if message.channel == client.get_channel(791196807057113090):
            if message.content.lower().replace(' ', '').startswith('h!buy'): 
                embed=discord.Embed(title="【﻿Ｂｌａｃｋ　Ｍａｒｋｅｔ】", description="Take a look around😈", color=0xff0000)
                embed.set_thumbnail(url="https://blackmarketnewyork.com/wp-content/themes/blackmarket/img/logo_bmny.jpg")
                embed.add_field(name="Space Weed", value="Ψ15.00", inline=True)
                embed.add_field(name="Pure Snow", value="Ψ75.00", inline=True)
                embed.add_field(name="Herobrine", value="Ψ666.666", inline=True)
                embed.add_field(name="Chicky Nuggies", value="Ψ5.00", inline=True)
                embed.add_field(name="Poopoo Weed", value="Ψ0.75", inline=True)
                await message.channel.send(embed=embed)
                
                
        if message.content.lower().replace(' ', '').startswith('h!dank'):
            choices = ['https://media.tenor.com/images/95fba7e7546a3985111c8e59a7d05ab0/tenor.gif','https://media.tenor.com/images/aafdfdcf15681b0c81a43b8dce787f45/tenor.gif','https://media.tenor.com/images/2922c8421e73af8b38314143ed2f9af7/tenor.gif','https://media.tenor.com/images/4e5d32b32492af1447f75025decf3003/tenor.gif']
            pick = random.choice(choices)
            await message.channel.send(pick)
            
        if message.content.lower().replace(' ', '').startswith('h!msg'):
            await message.author.send(pick)
            
client = MyClient()
client.run(TOKEN())
