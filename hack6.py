import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

URL = 'https://coinmarketcap.com'
HEADERS = {
    'User-Agent':
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'
}

r = requests.get(URL, headers=HEADERS, verify=False)
#print(r)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items = soup.findAll('div', class_='grid')
# print(items)

l =[]
for item in items:
    l.append({
        'Названия': item.find('div', class_='text-align:left'),#.get_text(strip=True),
        'Цена': item.find('div', class_='sc-131di3y-0 ')#.get_text(strip=True),
        # 'Фото': item.find('div', class_='listbox_img pull-left').find('a').find('img').get('src'),
        # 'Ссылка на товар':item.find('div', class_='listbox_title oh').find('a').get('href')
    })
pp(l)