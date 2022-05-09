# ANTARES (Advanced Null Technical Artificial Raider)
# Antares was proudly made by Platinum
# Copyright (C) 2022 Platinuk, all rights reserved

# Import required modules
import os, sys
from string import whitespace
import os.path
import time
from colorama import *
import requests
import threading
import discord
from discord.ext import commands

# Color
init()
BLUE = Fore.LIGHTBLUE_EX
WHITE = Fore.WHITE

# Banner
banner = f"""{BLUE}
 █████╗ ███╗   ██╗████████╗ █████╗ ██████╗ ███████╗███████╗
██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██╔██╗ ██║   ██║   ███████║██████╔╝█████╗  ███████╗  {WHITE}(C) Eternity{BLUE}
██╔══██║██║╚██╗██║   ██║   ██╔══██║██╔══██╗██╔══╝  ╚════██║
██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
{WHITE}Version: 1.0.0
{WHITE}Github: {BLUE}Eternity25
{WHITE}Discord: {BLUE}Eternity#8125
{BLUE}-----------------------------------------------------------
{BLUE}[{WHITE}-{BLUE}] {WHITE}Antares Advanced Discord Raider
{BLUE}-----------------------------------------------------------
{WHITE}type in {BLUE}"help" {WHITE}for a list of commands
{BLUE}-----------------------------------------------------------{Style.RESET_ALL}
"""

help_banner = f"""{BLUE}
 █████╗ ███╗   ██╗████████╗ █████╗ ██████╗ ███████╗███████╗
██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██╔██╗ ██║   ██║   ███████║██████╔╝█████╗  ███████╗  {WHITE}(C) Platinum{BLUE}
██╔══██║██║╚██╗██║   ██║   ██╔══██║██╔══██╗██╔══╝  ╚════██║
██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
{WHITE}                 --- Help Commands ---
{BLUE}-----------------------------------------------------------
{BLUE}[{WHITE}0{BLUE}] {WHITE}Webhook Spammer - Spam continuosly using webhook
{BLUE}[{WHITE}1{BLUE}] {WHITE}Raid Bot - Create bot event specialize in raiding
{BLUE}[{WHITE}2{BLUE}] {WHITE}Token Generator - Generate user tokens
{BLUE}[{WHITE}3{BLUE}] {WHITE}IP-Lookup - Track and lookup IP
{BLUE}[{WHITE}3{BLUE}] {WHITE}Message Spammer - Spam message using token
{BLUE}-----------------------------------------------------------{Style.RESET_ALL}
"""

# Variable
TOKEN = []
WEBHOOK = []

# Definiton functions
def spamMessageChannel(token, channel, mess, delay : int):
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header = {"authorization": token}

    while True:
        time.sleep(int(delay))
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)

def startSpamWebhook(message : str):
    try:
        if os.path.exists("./webhook.txt"):
            if os.stat("webhook.txt").st_size == 0:
                print("[ LOGS ] ERROR: No webhook found in the required file")
            else:
                while True:
                    for line in open("webhook.txt"):
                        line = line.strip()
                        req = requests.post(
                            line,
                            json = {
                                "content": message
                            }
                        )
                        status = str(req.status_code)
                        if status.startswith("2"):
                            size = os.stat("webhook.txt").st_size
                            print(f"{WHITE}[{BLUE}SPAM{WHITE}] {WHITE}Spammed total of: {size} webhook, content: {message}")
                        elif status.startswith("4"):
                            if status == "429":
                                retry = int(req.headers['retry-after']) / int(1000)
                                print(f"{WHITE}[{BLUE}ERROR{WHITE}] {WHITE}Message rate-limited, waiting for -> " + str(retry) + " seconds")
                                time.sleep(retry)
                            else:
                                print(f"{WHITE}[{BLUE}ERROR{WHITE}] {WHITE}Failed to send webhook data")
        else:
            print("[ ERROR ] Tokens file not found")
    except KeyboardInterrupt:
        exit()

# Main functions
def consoleCommand():
    command = input(f"[Antares@Main]~#: ")
    if command == "0":
        message = input("Message: ")
        startSpamWebhook(message)
    elif command == "2":
        bot_token = input("Bot Token: ")
        ownerid = input("Owner ID: ")
    elif command == "4":
        tokens = open("tokens.txt", "r").read().splitlines()
        channel = input("ChannelID: ")
        message = input("Message: ")
        delay = int(input("Delay: "))
        for token in tokens:
            time.sleep(int(delay))
            threading.Thread(target=spamMessageChannel, args=(token, channel, message, delay)).start()
    elif command == "clear":
        os.system("cls")
        mainMenu()
    elif command == "help":
        os.system("cls")
        print(help_banner)
        consoleCommand()
    else:
        print("Still under development")
        consoleCommand()

def mainMenu():
    os.system("title AntaresNuker - Advanced & mode con cols=80 lines=25")
    print(banner)
    consoleCommand()

# Start main functions
mainMenu()