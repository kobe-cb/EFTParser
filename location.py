import requests
from bs4 import BeautifulSoup
import re

def str_in(s):
    temp_list = re.match(".*In.*", s)
    if temp_list:
        return True
    else:
        return False

def eftLocation(results):
    list = results.find_all('li', string=lambda text: 'In')
    print("Locations:")
    for i in list:
        c = str_in(i.text)
    
        if (c):
            print(i.text.strip())
        else:
            continue
 