@bot.event
async def on_message(message):
    print(message.content)
    await message.channel.send("принял сообщение")
