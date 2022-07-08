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


    if message.content.startswith('*info')
     await message.channel.send('*дай текст песни ддт/n*дай текст песни гимн/n*дай текст песни цой')

client.run(TOKEN)
bot.run(TOKEN)
