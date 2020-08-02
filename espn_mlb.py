from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.espn.com/mlb/team/roster/_/name/bal/baltimore-orioles')
soup = BeautifulSoup(req.text, 'lxml')

team = soup.find('div', class_='Wrapper Card__Content')
team = team.h1.text
print(team)

position = soup.find('div', class_='Table__Title')
position = position.text
print(position)
