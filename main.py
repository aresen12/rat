import discord
from discord.ext import commands

TOKEN = "OTk0NTA5MjA2ODc3MTE0NDU4.GkfSa0.7ShlaZeG-FpeBpHABCPlABx-eeIw61C_IrkeOs"
bot = commands.Bot(command_prefix='*')


@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def h(ctx):
    await ctx.send('\*slava  \*test')
@bot.command(pass_context=True)
async def slava(ctx):
    await ctx.send('слава россии')

@bot.event
async def on_message(message):
    print(message.content)
    await message.channel.send("принял сообщение")
bot.run(TOKEN)
