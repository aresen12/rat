import discord
from discord.ext import commands
from setings import TOKEN
bot = commands.Bot(command_prefix='*')


@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def h(ctx):
    await ctx.send('\*slava  \*test')


@bot.command(pass_context=True)
async def slava(ctx):
    await ctx.send('слава росси')


@bot.command(pass_context=True)
async def song(ctx):
    with open('nvty.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        await ctx.send(data)


bot.run(TOKEN)
