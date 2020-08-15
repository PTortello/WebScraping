from bs4 import BeautifulSoup
from requests import get

address = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_area'
req = get(address).text
soup = BeautifulSoup(req, 'lxml')
match = soup.tbody

countries = match.find_all('tr')
countries.pop(0)

sum = 0
for country in countries:
    area = country.find('td', style='text-align:right;')
    sum += float(area.text.replace(',',''))

print('Europe total area is %.2f km2' % sum)
