import random
from bs4 import BeautifulSoup
import discord
import os
import datetime
import sqlite3
from discord.ext import commands
from setings import TOKEN
bot = commands.Bot(command_prefix='*')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    #if message.content.startswith('*дай текст песни ддт'):
     # with open('ддт.txt', 'r', encoding='utf-8') as file:
      #  data = file.read()
       # await message.channel.send(data)


    if message.content.startswith('*info'):
        await message.channel.send('*дай текст песни ддт \n *дай текст песни гимн \n *дай текст песни цой\n*орел или решка\n*искать в интернете текст песни')


    if message.content.startswith('*искать в интернете '):
        song = message.content[20:56]
        print(song)
        selsong ="#body > div.content-table > article > div.b-podbor > div:nth-child(2) > h1 > span:nth-child(2)"
        url =f"https://amdm.ru/search/?q={song}"
        sel1 = "#body > div.content-table > article > div.b-podbor > div:nth-child(2) > h1 > span:nth-child(1)"
        seltexst ="#body > div.content-table > article > div.b-podbor > div:nth-child(2) > div.b-podbor__text > pre"
        sel = "#body > div.content-table > article"
        import requests
        respons = requests.get(url)
        text = respons.text
        soup = BeautifulSoup(text,"html.parser")
        a = soup.select_one(sel)
        await message.channel.send(a.text)


        attrs = soup.select_one("table > tr:nth-child(2) a:nth-child(2)").attrs['href']
        respons = requests.get("https:"+attrs)
        text = respons.text
        print("attrs",attrs)
        soup = BeautifulSoup(text,"html.parser")
        a = soup.select_one(seltexst)
        songtexst = soup.select_one(seltexst)
        print(songtexst)
        embed = discord.Embed(color=0xf00c89,  type='rich', description=a.text)
        await message.channel.send(embed=embed)
        #await message.channel.send(a.text)


        respons = requests.get("https:"+attrs)
        sel2 = "#body > div.content-table > article > div.b-video > div > iframe"
        h = soup.select_one(sel2)
        print(h)
        youtube = h.attrs['src']
        print(youtube)
        await message.channel.send("ссылка на песню"+youtube)

    #elif message.content.startswith('**искать в интернете'):
     #   url = "https://amdm.ru/akkordi/viktor_coi/155737/zvezda_po_imeni_solnce/"

      #  sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2)"
       # import requests
        #respons = requests.get(url)
        #print (respons.status_code)
        #text = respons.text
        #soup = BeautifulSoup(text,"html.parser")
        #a = soup.select_one(sel)
        #print(a)

        #await message.channel.send(a.text)




    if message.content.startswith('*орёл или решка'):
       r = random.randrange(1, 3)
       if r == 2 :
          await message.channel.send('решка')
       else:
          await message.channel.send('орел')
client.run(TOKEN)
bot.run(TOKEN)
