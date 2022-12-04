import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
import time
import os

############################################################################################

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

os.system("cd")
os.system("start chrome --start-fullscreen")
time.sleep(2)
keyboard.press(Key.f11)
time.sleep(2)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(180, 50)
time.sleep(2)
mouse.click(Button.left)

###########################################################################################



keyboard.type("https://www.tiktok.com/upload?lang=fr%27")

time.sleep(2)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)

mouse.position = (0, 0)
time.sleep(3)
mouse.move(775, 310)
time.sleep(2)
mouse.click(Button.left)
time.sleep(4)
keyboard.type("N'hésite pas à t'abonner, il y a de l'exclu qui sort tous les jours ")
time.sleep(2)
keyboard.type("#twitch")
time.sleep(2)
keyboard.type(" #pourtoi")
time.sleep(2)
keyboard.type(" #youtube")
time.sleep(2)
keyboard.type(" #argent")
time.sleep(2)
keyboard.type(" #fyp")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #foryoupage")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #streamer")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #gotaga")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #sardoche")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #kameto")
time.sleep(2)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(600, 370)
time.sleep(1)

mouse.click(Button.left)


mouse.position = (0, 0)
time.sleep(2)
mouse.move(600, 55)
time.sleep(1)
mouse.click(Button.left)

time.sleep(1)

keyboard.type("C:/Users/TikTokBot/Desktop/TikTokBot-main/result")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(270, 145)
time.sleep(1)
mouse.click(Button.left)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(785, 510)
time.sleep(1)
mouse.click(Button.left)
time.sleep(15)

# mouse.position = (0, 0)
# time.sleep(2)
# mouse.move(1918, 880)
# time.sleep(1)
# mouse.click(Button.left)


# mouse.position = (0, 0)
# time.sleep(2)
# mouse.move(950, 385)
# time.sleep(1)
# mouse.click(Button.left)
# time.sleep(20)

# mouse.position = (0, 0)
# time.sleep(2)
# mouse.move(1020, 550)
# time.sleep(1)
# mouse.click(Button.left)
# time.sleep(30)

# mouse.position = (0, 0)
# time.sleep(2)
# mouse.move(1910, 10)
# time.sleep(1)
# mouse.click(Button.left)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(1020, 952)
time.sleep(1)
mouse.click(Button.left)

time.sleep(5)
os.system("taskkill /f /im chrome.exe")
