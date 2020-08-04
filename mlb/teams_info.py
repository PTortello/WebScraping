from bs4 import BeautifulSoup
from requests import get

teams = ['orioles', 'redsox', 'whitesox', 'indians', 'tigers', 'astros',
        'royals', 'angels', 'twins', 'yankees', 'athletics', 'mariners',
        'rays', 'rangers', 'bluejays', 'diamondbacks', 'braves', 'cubs',
        'reds', 'rockies', 'dodgers', 'marlins', 'brewers', 'mets',
        'phillies', 'pirates', 'padres', 'giants', 'cardinals', 'nationals']

"""
for team in teams:
    address = 'https://www.mlb.com/' + team + '/roster/40-man'
    req = get(address).text
    soup = BeautifulSoup(req, 'lxml')
    print(address)
"""

def roster_update(team):
    """Updates roster for selected team."""
    address = 'https://www.mlb.com/' + team + '/roster/40-man'
    req = get(address).text
    soup = BeautifulSoup(req, 'lxml')

    for position in soup.find_all('table', class_='roster__table'):
        players = position.tbody.find_all('a')
        jerseys = position.tbody.find_all('span', class_='jersey')
        position = position.find('td')

        print(position.text[:-1])
        for i in range(len(players)):
            print(jerseys[i].text + ' ' + players[i].text)
        print()

roster_update('padres')
