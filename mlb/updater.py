from bs4 import BeautifulSoup
from requests import get
from os import path

filedir = path.dirname(path.realpath('__file__'))


def roster_update(team):
    """Updates roster for selected team."""
    address = 'https://www.mlb.com/' + team + '/roster/40-man'
    req = get(address).text
    soup = BeautifulSoup(req, 'lxml')

    filename = path.join(filedir, 'teams/' + team + '.csv')
    with open(filename, 'w') as f:
        f.write(team.title() + '\n')

        for position in soup.find_all('table', class_='roster__table'):
            players = position.tbody.find_all('a')
            jerseys = position.tbody.find_all('span', class_='jersey')
            position = position.find('td')

            for i in range(len(players)):
                f.write(jerseys[i].text + ',' + players[i].text + ',' +
                    position.text[:-1] + '\n')


def update_all():
    """Updates roster for every team."""
    teams = ('angels', 'astros', 'athletics', 'bluejays', 'braves', 'brewers',
            'cardinals', 'cubs', 'dbacks', 'dodgers', 'giants', 'indians',
            'mariners', 'marlins', 'mets', 'nationals', 'orioles', 'padres',
            'phillies', 'pirates', 'rangers', 'rays', 'reds', 'redsox',
            'rockies', 'royals', 'tigers', 'twins', 'whitesox', 'yankees')
    for team in teams:
        roster_update(team)


roster_update('angels')
