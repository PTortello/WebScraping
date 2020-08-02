from bs4 import BeautifulSoup
import requests

page = 1
#while(True):
for k in range(1,2):
    param = {'page': page}
    address = 'https://listfortress.com/tournaments'

    req = requests.get(address, param)
    soup = BeautifulSoup(req.text, 'lxml')

    #tournament = soup.tbody.find('tr')
    for tournament in soup.tbody.find_all('tr'):
        for info in tournament.find_all('td'):
            print(info.text)

    #page += 1

"""
data = ['aaa', 'bbb', 'ccc']
with open('scrap.csv', 'w') as f:
    f.write('START\n\n')
    for d in data:
        f.write(d + ',')
    f.write('\n\nEND')
"""