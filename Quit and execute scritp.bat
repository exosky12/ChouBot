@echo off
echo [!] You can quit
timeout /t 15 /nobreak
echo ' Create WScript Shell Object to access filesystem.>%temp%/y.vbs
echo Set WshShell = WScript.CreateObject("WScript.Shell")>>%temp%/y.vbs
echo WScript.Sleep 500>>%temp%/y.vbs
echo WshShell.SendKeys "{ENTER}">>%temp%/y.vbs
start %temp%\y.vbs
echo [!] Script will be executed
timeout /t 5 /nobreak
start C:\Users\TikTokBot\Desktop\TikTokBot-main\main-task.bat
exit