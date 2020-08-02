# Listfortress is a website containing a list of X-Wing tournaments

from bs4 import BeautifulSoup
import requests

with open('scrap.csv', 'w') as f:

    page = 1
    #while(True):
    for k in range(1,2):
        param = {'page': page}
        address = 'https://listfortress.com/tournaments'

        req = requests.get(address, param)
        soup = BeautifulSoup(req.text, 'lxml')

        #tournament = soup.tbody.find('tr')
        for tournament in soup.tbody.find_all('tr'):
            i = 0
            for info in tournament.find_all('td'):
                #print(info.text)
                f.write(info.text + ',')
                i += 1
                if i == 8:
                    f.write('\n')
                    break

        #page += 1
# lines = open( 'sta1214.txt', "r" ).readlines()[::2]