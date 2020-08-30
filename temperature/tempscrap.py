from bs4 import BeautifulSoup
from requests import get


source = "sorocaba.dat"
with open(source, 'r') as data:
    address = data.read()

req = get(address).text
soup = BeautifulSoup(req, 'lxml')

match = soup.find('div', id='mainContent')
match = match.find_all('span')
match = match[7].text[1:3]

print(match)
input()
