import requests
from bs4 import BeautifulSoup
import re

def is_item(s, find):
    temp_list = re.match(".*" + find + "*.", s)
    if temp_list:
        return True
    else:
        return False

def i_sort(query):
    stopwords = {"barter", "item", "other", "crafting", "building", "materials", "flammable", "valuables", "info",
                 "electronics", "energy", "elements", "household", "goods", "tools", "medical", "supplies"}

    resultwords = [word for word in re.split("\W+",query) if word.lower() not in stopwords]

    boolDog = False
    if resultwords[1] == "Dogtag":
        boolDog = True

    occurList = [idx for idx, val in enumerate(resultwords) if val == 'Quests']
    for i,idx in enumerate(occurList):
        resultwords.insert(idx+i, '\n')

    occurList = [idx for idx, val in enumerate(resultwords) if val == 'Hideout']
    for i,idx in enumerate(occurList):
        resultwords.insert(idx+i, '\n')

    occurList = [idx for idx, val in enumerate(resultwords) if val == 'Used']
    for i,idx in enumerate(occurList):
        resultwords.insert(idx+i, '\n')
    occurList = [idx for idx, val in enumerate(resultwords) if val == 'Can']
    for i,idx in enumerate(occurList):
        resultwords.insert(idx+i, '\n')



    
    occurList = [idx for idx, val in enumerate(resultwords) if val == 'need']      
    if boolDog:
        for i,idx in enumerate(occurList):
            resultwords.insert(idx+i-2, '\n')
    else:
        for i,idx in enumerate(occurList):
            resultwords.insert(idx+i-1,'\n')
    
    occurList = [idx for idx, val in enumerate(resultwords) if val == 'needs']      
    if boolDog:
        for i,idx in enumerate(occurList):
            resultwords.insert(idx+i-2, '\n')
    else:
        for i,idx in enumerate(occurList):
            resultwords.insert(idx+i-1,'\n')

    resultwords.pop(0)
    result = ' '.join(resultwords)
    return result

def eftInformation(user_input):
    URL = "https://escapefromtarkov.gamepedia.com/Loot"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='mw-parser-output')
    list = results.find_all('tr')
    print("======Hideout/Quests======")

    for i in list:
        if (is_item(i.text.strip(), user_input)):
            print(i.text.strip())
            print("+====Sort====+")
            i = i_sort(i.text)
            print(i)
            break

    print("======END======")