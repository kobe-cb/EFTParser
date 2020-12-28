import requests
from bs4 import BeautifulSoup
import re
import sys
from location import eftLocation
from information import eftInformation

def BS4Grab(user_input):
    URL = "https://escapefromtarkov.gamepedia.com/" + user_input
    #URL = "https://escapefromtarkov.gamepedia.com/Crickent_lighter"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='mw-parser-output')
    return results

def userDigit(user_command):
    if user_command.isdigit():
        return True
    return False

user_input = ""
user_command = sys.maxsize
while (True):
    print("===== Welcome to EFTParser, Please read the menu below =====")
    print("1 - Loot Item")
    print("2 - Weapon(WIP)")
    print("3 - Etc(WIP)")
    print("0 - Exit")
    user_command = input()
    if userDigit(user_command):
        user_command = int(user_command)

    if (user_command == 1):
        print("Please enter the loot item:")
        user_input = input()
        user_input = user_input.lower()
        user_input = user_input.capitalize()
        results = BS4Grab(user_input)
        if results == None:
            print("Invalid Response")
        else:
            #============LOCATIONS============
            eftLocation(results)
            #============HIDEOUT/QUESTS============
            eftInformation(user_input)
    elif (user_command == 2):
        continue
    elif (user_command == 3):
        continue
    elif (user_command == 0):
        break
    else:
        print("You entered an invalid choice")
        continue







