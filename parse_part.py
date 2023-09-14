import json
import requests
from bs4 import BeautifulSoup

url = 'http://www.smclinic.ru/diseases/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


def set_default(obj):
    '''перерабатывает данные из кортежа в список'''
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def getMiniDesc(link):
    '''функция берет краткое описание болезни из шапки'''
    page_url = 'http://www.smclinic.ru' + link
    if requests.get(page_url).status_code == 200:
        page_r = requests.get(page_url)
        page_soup = BeautifulSoup(page_r.content, 'html.parser')
        if page_soup.select_one('div[itemprop=description]') != None:
            description = page_soup.select_one('div[itemprop=description]').text
            return description
        else:
            return getDesc(link)


def getDesc(link):
    '''функция берет полное описание болезни со страницы'''
    page_url = 'http://www.smclinic.ru' + link
    if requests.get(page_url).status_code == 200:
        page_r = requests.get(page_url)
        page_soup = BeautifulSoup(page_r.content, 'html.parser')
        main_text = page_soup.find('div', attrs={'class': 'b-text-block-6__text text'}).text
        return main_text


if requests.get(url).status_code == 200:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    diseases = soup.find('div', attrs={'class': 'diseases-list__items'})

    item_element = {}

    count = 1

    '''дальше идет основной парсинг приложения. берутся ссылка, имя, описание, а после
        перебрасываются в словарь
    '''
    # for item in diseases.find_all('a'):
    #     if 'www.sm-stomatology.ru/patients/diseases/' in item.get('href'):
    #         continue
    #     else:
    #         item_url = 'http://www.smclinic.ru' + item.get('href')
    #         item_name = item.text
    #         item_desc = getMiniDesc(item.get('href'))
    #
    #         item_element[count] = {
    #             'Имя': {
    #                 item_name
    #             },
    #             'Описание': {
    #                 item_desc
    #             },
    #             'Ссылка': {
    #                 item_url
    #             }
    #         }
    #
    #         print(f'{item_name} : {count}')
    #
    #         count += 1

    '''парсинг в json формат'''

    # with open('diseases_dict.json', 'w', encoding='utf-8') as file:
    #     json.dump(item_element, file, indent=4, ensure_ascii=False, default=set_default)


    '''из json файла берутся данные для последующего отправления пользователю'''
    with open("diseases_dict.json", 'r', encoding='utf-8') as file:
        json_data = file.read()
        data = json.loads(json_data)
