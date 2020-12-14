# e6


import os
import requests
import socket
import sys
import time
from colorama import Fore

def __target__():
    time.sleep(0.3)
    os.system("clear")
    time.sleep(0.4)
    print(Fore.YELLOW + "Hello , This Is Test ;)")
    time.sleep(0.4)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter Your Adress Target" + Fore.GREEN + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "[!] ~ Error : Your Target Is None Or Not Found ;(")
            time.sleep(0.3)
            sys.exit()
        except:
            pass
    if not "http" in target or not "https://" in target:
        target = "http://" + target
    #ip = socket.gethostbyname(target)
    r = requests.get(target)
    while True:
        if r.status_code == 200:
            print(Fore.GREEN + "[" + Fore.BLUE + "+" + Fore.GREEN + "]" + Fore.BLUE + " ~ " + Fore.GREEN + target )
        else:
            print(Fore.RED + "[" + Fore.YELLOW + "+" + Fore.RED + "]" + Fore.YELLOW + " ~ " + Fore.RED + target )
__target__()
