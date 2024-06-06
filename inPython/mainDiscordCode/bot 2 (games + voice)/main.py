import discord
from discord.ext import commands 
from discord import FFmpegPCMAudio
from dotenv import load_dotenv
import os
import yt_dlp as youtube_dl

# import requests
# import json

# Making an output directory
output_dir = r'discordBots\inPython\mainDiscordCode'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#setting up yt_dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(output_dir, '%(extractor)s-%(id)s-%(title)s.%(ext)s'),
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # Bind to IPv4 since IPv6 addresses cause issues sometimes
}


# Load the .env file
load_dotenv()

# Fetch the token from the .env file
my_key = os.getenv("MY_KEY2")

joke_key = os.getenv("JOKE_KEY")

# Gives the bot access to all the intents (permissions) we gave it
intents: discord.Intents = discord.Intents.default()

intents.members = True

# Making message_content = true
intents.message_content = True 

bot = commands.Bot(command_prefix="$", intents=intents)

# Events

@bot.event
async def on_ready():
    print(f"{bot.user} is now ready! \n -------------------------")

@bot.event
async def on_member_join(member):

    channel = bot.get_channel(1066090136451952754)

    await channel.send(f"Everybody welcome {member.name}"), member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_member_remove(member):

    print(f"{member} has left the server")
   # Try to send a farewell message to the member
    try:

        await member.send(f"Farewell {member.name}")
    
    except discord.Forbidden:

        print(f"Could not send farewell message to {member.name}")

#Bot Commands

@bot.command()
async def hello(ctx):
    
    await ctx.send("hello!")

# has it join voice channels
@bot.command(pass_content=True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(r"discordBots\inPython\mainDiscordCode\bot 2 (games + voice)\videoplayback.wav")
        player = voice.play(source)
        await ctx.send("I have joined the voice channel")
    else:
        await ctx.send("Please join a voice channel before asking me to join it!!")

@bot.command(pass_content=True)
async def leave(ctx):

    if ctx.voice_client:
        
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    
    else:

        await ctx.send("I am not in a voice channel")


@bot.command(pass_content=True)
async def pause(ctx) -> None:
    
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():

        voice.pause()
    
    else:
        await ctx.send("I am not playing anything right now")

@bot.command(pass_content=True)
async def resume(ctx) -> None:

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_paused():

        voice.resume()
    
    else:

        await ctx.send("I am playing something already, nothing is paused")

@bot.command(pass_content=True)
async def stop(ctx) -> None:

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    voice.stop()


# downloaded songs on the pc
# @bot.command(pass_content=True)
# async def play(ctx, song) -> None:

#     with open(file=r"discordBots\inPython\mainDiscordCode\bot 2 (games + voice)\song_paths.txt", mode="r") as a:
#         lines = a.readlines()

#     lines = [line.strip() for line in lines]

#     names = []

#     links = []

#     link = ""

#     for item in lines:

#         if item.lower() == "end of songs":

#             break

#         if item.lower() == "":
            
#             continue

#         parts = item.split(":", 1)

#         names.append(parts[0])

#         links.append(parts[1])


#     voice = ctx.guild.voice_client

#     if names[0] in song:
    
#         source = FFmpegPCMAudio(r"discordBots\inPython\mainDiscordCode\bot 2 (games + voice)\videoplayback.wav")

#     elif names[1] in song:

#         source = FFmpegPCMAudio(r"discordBots\inPython\mainDiscordCode\bot 2 (games + voice)\Shakira - Hips Don't Lie (Official 4K Video) ft. Wyclef Jean.wav")

#     player = voice.play(source)


#using youtube
@bot.command(pass_content=True)
async def play(ctx, url):
    try:
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            await ctx.send("You are not connected to a voice channel.")
            return
    except AttributeError:
        await ctx.send("You are not connected to a voice channel.")
        return

    vc = await voice_channel.connect()

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            print(f'Playing URL: {url2}')  # Debug URL

        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=url2), after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send(f'Now playing: {info["title"]}')
    except Exception as e:
        print(f'Error: {e}')
        await ctx.send("An error occurred while trying to play the audio.")


# @bot.command()
# async def help(ctx):

#     await ctx.send()

## In Progress

# @bot.command()
# async def joke(ctx):

#     joke_url = "https://joke3.p.rapidapi.com/v1/joke"

#     headers = {
#         "X-RapidAPI-Key": joke_key,
#         "X-RapidAPI-Host": "joke3.p.rapidapi.com"
#     }

#     response = requests.get("GET", joke_url, headers=headers)

#     await ctx.send(response.json())


bot.run(my_key)