from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv

session = HTMLSession()
request = session.get('https://www.nbp.pl/')

soup = BeautifulSoup(request.content, 'html.parser')

table = soup.find(id='rightSide').find_all('table')[1]
rows = table.find_all('tr')

data = []
for row in rows:
    data.append(row.text)

f = open('currency.csv', 'w')
writer = csv.writer(f)
writer.writerow(data)
f.close()
