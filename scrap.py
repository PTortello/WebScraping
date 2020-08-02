from bs4 import BeautifulSoup
import requests
import re

# Website
#req = requests.get('https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_team_rosters')
#soup = BeautifulSoup(req.text, 'lxml')

# Arquivo local
with open('.\Skulpt\index.html') as file:
    soup = BeautifulSoup(file, 'lxml')


# Organiza o html com indentation, opcional se quiser visualizar tudo
# print(soup.prettify())

# Retorna apenas a primeira tag encontrada
match = soup.link   # tag "link", poderia ser "title", "script", etc
print(match)

# Retorna apenas o texto da tag
match = soup.h3.text
print(match)

# Retorna lista com todos os encontrados
match = soup.select('script')
for i in range(len(match)):
    print(match[i])
