# Project Omega
# Developer: ImPeterWA⛧
# Colab: ZeroMeia, Henguerz_
# Demo game


# color
from colorama import *

color = {
    "red": Fore.RED,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "magenta": Fore.MAGENTA,
    "green": Fore.GREEN,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}

# for clear and sleep functions
import os
from time import sleep

# game imports
from headers import *
from player import Player
from miscFunctions import *
import random
from playsound import playsound
import threading

init(autoreset=True)

threading.Thread(target=playsound, args=["file.mp3", False]).start()

clear()

print(color['white']+main)
print(color['red']+dragon2)

choice = input("?: ")

if choice.lower() == "exit":
    quit()
elif choice.lower() == "enter":
    for i in range(10):
        sleep(0.05)
        print(color['white']+fate)
else:
    quit()


clear()

sleep(2.00)
print(color['white']+hei)
sleep(2.00)

clear()

print(color['white']+rabbit)
sleep(1.00)

clear()

print(color['white']+rabbit2)
sleep(0.70)

clear()

print(color['white']+rabbit)
sleep(0.50)
beautifulPrint(instaPrint="\n are you OK?!", text="looks bad, need a little help? <3")

print(color['green']+""" 
1- Of Course, tnks friend, so, what happened to me?
2- you seem strangely dangerous, I am not mistaken with your cuteness
3- CUM INSIDE ME""") # que porra é essa russo.

choice = input("?: ")

if choice.lower() == "1":  
    clear() 
    beautifulPrint(text="Dont worry Cuttie")

input('\nPress enter to quit...')
