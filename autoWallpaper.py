import json
from os import chdir
from os import listdir
from random import randrange
import socket
import ctypes

f = open("options.json")

options = json.load(f)

wallpaperDir = options["wallpaperDir"]
mode = options["mode"]
startIp = options["startIp"]

f.close()

chdir(wallpaperDir)

wallpaperList = listdir()

if mode == "random":
    randNum = randrange(len(wallpaperList))
    wallpaper = wallpaperDir + "\\" + wallpaperList[randNum]
elif mode == "perPC":
    hostname = socket.gethostname()
    ipAddr = socket.gethostbyname(hostname)
    
    startIpList = startIp.split(".")
    ipAddrList = ipAddr.split(".")

    if startIpList[0] == ipAddrList[0] and startIpList[1] == ipAddrList[1] and startIpList[2] == ipAddrList[2]:
        pcNum = int(ipAddrList[3]) - int(startIpList[3]) + 1

        for i in wallpaperList:
            if i.split(".")[0] == ("PC" + str(pcNum)):
                wallpaper = wallpaperDir + "\\" + i
                

SPI_SETDESKWALLPAPER = 20 

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 3)
