import requests
from bs4 import BeautifulSoup

url = 'http://www.smclinic.ru/diseases/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

def getinfo(link):
    page_url = 'http://www.smclinic.ru/diseases/' + link
    if requests.get(page_url).status_code == 200:
        page_r = requests.get(page_url)
        page_soup = BeautifulSoup(page_r.content, 'html.parser')
        description = page_soup.select_one('div[itemprop=description]').text
        main_text = page_soup.find('div', attrs={'class' : 'b-text-block-6__text text'}).text

if requests.get(url).status_code == 200:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    diseases = soup.find('div', attrs={'class' : 'diseases-list__items'})

    items_dict = {}

    for item in diseases.find_all('a'):
        item_url = url + item.get('href')
        item_name = item.text
        items_dict[item_name] = item_url
