from youtube_dl import YoutubeDL
from asyncio import sleep

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@bot.command()
async def play(ctx, arg):
    global vc

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)

        URL = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))

        while vc.is_playing():
            await sleep(1)
        if not vc.is_paused():
            await vc.disconnect()
