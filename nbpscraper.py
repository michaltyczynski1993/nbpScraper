from locale import currency
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

session = HTMLSession()
request = session.get('https://www.nbp.pl/')

soup = BeautifulSoup(request.content, 'html.parser')

table_data = []
table = soup.find(id='rightSide').find_all('table')[1]
cols = table.find_all('tr')

for col in cols:
    table_dict = {
        'currency': col.find('td').text.strip(),
        'value': col.find('td').findNext('td').text.strip()
    }

    table_data.append(table_dict)

df = pd.DataFrame(table_data)
df.to_csv('table.csv') 