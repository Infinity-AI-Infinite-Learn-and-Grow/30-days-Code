#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
data = {}
for i in soup.find_all('div', class_='fact'):
    data[i.find('h3').text] = i.find('p').text
with open('data.json', 'w') as f:
    json.dump(data, f)

#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file


def get_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', class_='table-striped')
    data = []
    for row in table.find_all('tr'):
        data.append([i.text for i in row.find_all('td')])
    return data

data = get_table('https://archive.ics.uci.edu/ml/datasets.php')
with open('data.json', 'w') as f:
    json.dump(data, f)

