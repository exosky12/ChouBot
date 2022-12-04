@echo off
echo [!] You can quit!
timeout /t 15 /nobreak
echo ' Create WScript Shell Object to access filesystem.>%temp%/y.vbs
echo Set WshShell = WScript.CreateObject("WScript.Shell")>>%temp%/y.vbs
echo WScript.Sleep 500>>%temp%/y.vbs
echo WshShell.SendKeys "{ENTER}">>%temp%/y.vbs
start %temp%\y.vbs
exit