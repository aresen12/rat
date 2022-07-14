import requests
query = query.replace(' ','+')
url = 'https://www.youtube.com/results?search_query='+query
r = requests.get(url).text

balise = 'data-context-item-id="'   #balise signalant l'élément manquant dans le code source

liste_videos = []

for e in range(nb): #on ajoute les url de chaque video

    liste_videos.append([])
    i = r.index(balise)     #renvoie la position de la balise dans le code
    liste_videos[-1].append('https://www.youtube.com/watch?v='+r[i+22:i+22+11])
    r = r[i+100:]   #on coupe le début du code pour aller chercher dans la suite plus facilement


for vid in range(nb): #puis leurs titre

    url = liste_videos[vid][0]  #on prend l'url d'une video
    r = requests.get(url).text  #on ouvre la page correspondante
    title = r[r.index('<title>')+7:r.index('</title>')]     #et on cherche le titre dedans
    liste_videos[vid].append(title) #puis on met le titre dans le tableau video
    u = liste_videos[vid][0]

return liste_videos     #on finit par renvoyer ce tableau

opts = {'default_search': 'auto','quiet': True,}    #options pour youtube-dl que je comprends pas
    if voice == None:   #si le bot n'a pas encore été connecté à un channel
        await bot.say('Summon me in your channel first (!summon)')

    elif query[:3] == 'url':
        try:
            n = int(query[4])
            await bot.say(videos[n][0])
        except Exception as e:
            await bot.say (e)


    elif len(query) != 1: #si le joueur essaie de taper !play recherche et non !play 1/2/3/4
        videos = yt.recherche(query,4)  #on charge les informations des vidéos avec le module yt
        for i in range(4): #on affiche les 4 résultas avec un emebed contenant un apercu de chaque vidéo
            em = discord.Embed(title=videos[i][1], colour=0xff0000, type = 'rich')
            em.set_thumbnail(url='https://i.ytimg.com/vi/'+videos[i][0][32:]+'/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDBtpHoodvOvDCPjzg9t7PzSljI3A')
            await bot.send_message(ctx.message.channel,None,embed=em)
        await bot.say('Make your choice! (!play 1/2/3/4)')

    else:   #si le joueur essaie de choisir une video avec !play 1/2/3/4
        try:
            if player != None:  #si le bot joue déjà une chanson, on stoppe la précédente avant de commencer la suivante (sinon ca plante)
                player.stop()
            query = int(query)  #on convertit en entier : str -> int
            player = await voice.create_ytdl_player(videos[query-1][0],ytdl_options=opts) #on initialise le player audio dans la varialble globale
            player.volume = 0.2     #on fixe le volume
            player.start()          #on démarre la lecture

        except Exception as e:     #exception atteinte en général si on a pas réussi à faire query = int(query), c'est à dire que le joueur à fait une faute de frappe
            await bot.say(e)
