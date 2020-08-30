"""
tempscrap.py
Pedro Tortello - 08/2020
Current temperature web scraping for choosen location.
"""

from bs4 import BeautifulSoup
from requests import get

# CAUTION: Hard coded file name containing url address
source = "sorocaba.dat"
with open(source, 'r') as data:
    address = data.read()

# Web scraping url address
req = get(address).text
soup = BeautifulSoup(req, 'lxml')

# Searching current temperature
match = soup.find('div', id='mainContent')
match = match.find_all('span')
match = match[7].text[1:3]

print(match + '\xb0C')
input()
