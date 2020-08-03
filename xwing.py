# Listfortress is a website containing a list of X-Wing tournaments

from bs4 import BeautifulSoup
import requests

with open('scrap.csv', 'w', encoding='utf-8') as f:

    page = 1
    #while(True):
    for k in range(1,58):
        print('Scraping page ' + str(page) + ' ...')
        param = {'page': page}
        address = 'https://listfortress.com/tournaments'

        req = requests.get(address, param)
        soup = BeautifulSoup(req.text, 'lxml')

        #tournament = soup.tbody.find('tr')
        for tournament in soup.tbody.find_all('tr'):
            column = 0
            for info in tournament.find_all('td'):
                f.write(info.text)
                if column < 7:
                    f.write(',')
                column += 1

        page += 1

# Removes one from every two lines
print('Removing lines ...')
lines = open('scrap.csv', 'r', encoding='utf-8').readlines()[::2]
with open('scrap.csv', 'w', encoding='utf-8') as f:
    for i in lines:
        f.write(i)

print('Finished')
