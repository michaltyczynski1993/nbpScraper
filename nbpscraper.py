from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
request = session.get('https://www.nbp.pl/')

soup = BeautifulSoup(request.content, 'html.parser')

table = soup.find(id='rightSide').find_all('table')[1]
cols = table.findAll('tr')

for col in cols:
    col.findAll('td')
    print(col)