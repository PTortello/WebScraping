from bs4 import BeautifulSoup
import requests

address = 'https://www.espn.com/mlb/team/roster/_/name/bal/baltimore-orioles'
req = requests.get(address).text
soup = BeautifulSoup(req, 'lxml')

team = soup.find('div', class_='Wrapper Card__Content')
team = team.h1.text
print(team)

position = soup.find('div', class_='Table__Title')
position = position.text
print(position)
