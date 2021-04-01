
from bs4 import BeautifulSoup
import discord
import requests 


def TOKEN():
    return ''


def KDA(user):
    finalString = ""

    URL = 'http://na.op.gg/summoner/userName=' + user
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("span", class_='KDA')
    results1 = soup.find_all("div", class_='ChampionName')

    for x in range(10):
        try:
            stripper = results1[x].get_text()
            stripped = stripper.strip()
            finalString += stripped + " " + results[x].get_text() + "\n"
        except:
            
            break
        
    return finalString


def LIVE(user):
    
    finalString = ''
    
    URL = 'http://na.op.gg/summoner/userName=' + user
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("td", class_='SummonerName')

    for x in range(len(results)):
        resultant = results[x].get_text()
        resultant = resultant.strip()
        finalString += resultant + '\n'
    
    return finalString


def SNIPE(sender, sendersmessage):
                embed = discord.Embed(title="Idiot of the Week", url="https://i.ytimg.com/vi/bFZxqmHQaIA/hqdefault.jpg")
                embed.set_thumbnail(url="https://i.ytimg.com/vi/bFZxqmHQaIA/hqdefault.jpg")
                embed.add_field(name=sender, value=sendersmessage, inline=True)
                embed.set_footer(text="get sniped😂")
                return embed
    
def REPLAY(user):
    finalString = ""
    
    URL = 'http://na.op.gg/summoner/userName=' + user
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results1 = soup.find_all("div", class_='SummonerName')
    for x in range(10):
        try:
            stripper = results1[x].get_text()
            stripped = stripper.strip()
            finalString += stripped + " " + results1[x].get_text() + "\n"
        except: break
        
    return finalString
    
    
def RANK(user):
    
    finalString = ''
    
    URL = 'http://na.op.gg/summoner/userName=' + user
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("div", class_='TierRank')
    results1 = soup.find_all("span", class_="LeaguePoints")
    
    for x in range(len(results)):
        stripped = (results1[x].get_text()).strip()
        resultant = results[x].get_text()
        resultant = resultant.strip()
        finalString += resultant + '\n' + stripped
    
    return finalString


def CHAMPKDA(user):
    finalString = ''
    
    URL = 'http://na.op.gg/summoner/userName=' + user
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('span', class_='Kill')
    results1 = soup.find_all('span', class_="Death")
    results2 = soup.find_all('span', class_='Assist')
    results3 = soup.find_all('div', class_='ChampionName')
    
    for x in range(5):
        try:
            stripped = (results[x].get_text()).strip()
            stripped1 = (results1[x].get_text()).strip()
            stripped2 = (results2[x].get_text()).strip()
            stripped3 = (results3[x].get_text()).strip()
            finalString += stripped3 + '\n' + stripped + '/' + stripped1 + '/' + stripped2 + '\n' + "\n" 
        
        except:
            break

    return finalString

