from bs4 import BeautifulSoup
import discord
import youtube_dl
import sqlite3
import os
from discord.ext import commands
from setings import TOKEN
bot = commands.Bot(command_prefix='*')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    return


@client.event
async def on_message(message):
    if message.content.startswith('*info'):
        await message.channel.send('список команд:\n*орел или решка\n*искать в интернете текст песни')


    if message.content.startswith('*орёл или решка'):
        import random
        r = random.randrange(1, 3)
        if r == 2 :
          await message.channel.send('решка')
        else:
          await message.channel.send('орел')


    if message.content.startswith('*искать в интернете '):
        song = message.content[20:56]
        print(song)
        url =f"https://pesni.guru/search/{song}"

        sel = "body > div > div.arow > div.acol1 > div > p:nth-child(3) > a"
        import requests
        respons = requests.get(url)
        text = respons.text
        soup = BeautifulSoup(text,"html.parser")
        a = soup.select_one(sel)
        textsong = a.attrs["href"]

        if not textsong :
            await message.channel.send("Текст не найден")

        else:
           sel1 = "body > div.container > div.arow > div.acol1 > div"

           attrs = "https://pesni.guru/"+textsong
           respons = requests.get(attrs)
           text = respons.text

           soup = BeautifulSoup(text,"html.parser")
           a = soup.select_one(sel1)
           a.select_one("a").clear()
           a.select_one(".bar_block").clear()
           a.select_one("p").clear()
           a.select_one("ul").clear()
           embed = discord.Embed(color=0xf00c89,  type='rich', description=a.get_text(separator="\n"))
           await message.channel.send(embed=embed)
        #await message.channel.send(a.text)


           #url2 =f'https://www.youtube.com/results?search_query={song}'
           #respons = requests.get(url2)
           #attrs = soup.select_one("table > tr:nth-child(2) a:nth-child(2)").attrs['href']
           #text = respons.text
           #soup = BeautifulSoup(text,"html.parser")
           #sel2 = "#video-title > yt-formatted-string"
           #h = soup.select_one(sel2)
           #print(h)
           #youtube = h.attrs['src']
           #print("youtube"+youtube)
           #url2 =f"https://www.youtube.com/results?search_query={song}"

           sel3 = "#movie_player > div.ytp-chrome-top.ytp-show-cards-title > div.ytp-title > div"
           a = soup.select_one(sel3)
           text = respons.text
           soup = BeautifulSoup(text,"html.parser")

           print(a)
          # attrs = soup.select_one("table > tr:nth-child(2) a:nth-child(2)").attrs['href']
          # youtube = requests.get("https:"+attrs)


client.run(TOKEN)
bot.run(TOKEN)
