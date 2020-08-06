from bs4 import BeautifulSoup
from requests import get


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


def update_all():
    """Updates roster for every team."""
    teams = ['angels', 'astros', 'athletics', 'bluejays', 'braves', 'brewers',
            'cardinals', 'cubs', 'dbacks', 'dodgers', 'giants', 'indians',
            'mariners', 'marlins', 'mets', 'nationals', 'orioles', 'padres',
            'phillies', 'pirates', 'rangers', 'rays', 'reds', 'redsox',
            'rockies', 'royals', 'tigers', 'twins', 'whitesox', 'yankees']

    for team in teams:
        print(team)
        roster_update(team)
        print()


#roster_update('padres')
update_all()
