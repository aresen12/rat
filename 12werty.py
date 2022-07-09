import random
from bs4 import BeautifulSoup
import discord
import os
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


    if message.content.startswith('*дай текст песни цой'):
      with open('nvty.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        await message.channel.send(data)

    if message.content.startswith('*дай текст песни гимн'):
      with open('гимн.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        await message.channel.send(data)


    if message.content.startswith('*дай текст песни ддт'):
      with open('ддт.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        await message.channel.send(data)


    if message.content.startswith('*info'):
        await message.channel.send('*дай текст песни ддт \n *дай текст песни гимн \n *дай текст песни цой\n*орел или решка\n*искать в интернете')


    if message.content.startswith('*искать в интернете'):
        print(message.content.split("$$"))

        url = f"https://amdm.ru/search/?q={song}"

        sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2)"
        import requests
        respons = requests.get(url)
        print (respons.text)
        text = respons.text
        soup = BeautifulSoup(text,"html.parser")
        a = soup.select_one(sel)

        await message.channel.send(a.text)

    elif message.content.startswith('**искать в интернете'):
        url = "https://amdm.ru/akkordi/viktor_coi/155737/zvezda_po_imeni_solnce/"

        sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2)"
        import requests
        respons = requests.get(url)
        print (respons.status_code)
        text = respons.text
        soup = BeautifulSoup(text,"html.parser")
        a = soup.select_one(sel)

        await message.channel.send(a.text)




    if message.content.startswith('*орёл или решка'):
       r = random.randrange(1, 3)
       if r == 2 :
          await message.channel.send('решка')
       else:
          await message.channel.send('орел')
client.run(TOKEN)
bot.run(TOKEN)
