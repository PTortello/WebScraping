# Listfortress is a website containing a list of X-Wing tournaments

from bs4 import BeautifulSoup
from requests import get
from datetime import date
from os import path

# Creates a filename based on script name + current date
filename = path.basename(__file__)[:-3] + '_' + str(date.today()) + '.csv'

# Obtains last page
address = 'https://listfortress.com/tournaments'
req = get(address).text
soup = BeautifulSoup(req, 'lxml')
match = soup.find('ul', class_='pagination justify-content-center')
match = match.find_all('li')
lastPage = int(match[len(match)-2].text)

with open(filename, 'w', encoding='utf-8') as f:

    for page in range(1, lastPage + 1):
        print('Scraping page ' + str(page) + ' ...')
        param = {'page': page}
        req = get(address, param).text
        soup = BeautifulSoup(req, 'lxml')

        for tournament in soup.tbody.find_all('tr'):
            column = 0
            for info in tournament.find_all('td'):
                f.write(info.text)
                if column < 7:
                    f.write(',')
                column += 1

# Removes one from every two lines
print('Removing lines ...')
lines = open(filename, 'r', encoding='utf-8').readlines()[::2]
with open(filename, 'w', encoding='utf-8') as f:
    for i in lines:
        f.write(i)

print('Scraping completed.\n<Press any key to exit>')
input()
