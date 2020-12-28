import requests
from bs4 import BeautifulSoup
import re

from location import eftLocation
from information import eftInformation

print("Program Starting, Enter the item")
user_input = input()

user_input = user_input.lower()
user_input = user_input.capitalize()

print("You entered: " + user_input)

URL = "https://escapefromtarkov.gamepedia.com/" + user_input
#URL = "https://escapefromtarkov.gamepedia.com/Crickent_lighter"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='mw-parser-output')

#============LOCATIONS============
eftLocation(results)

 #============HIDEOUT/QUESTS============
eftInformation(user_input)





