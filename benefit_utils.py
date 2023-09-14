import copy
import pprint

from parse_part import data
from random import randint
import json


def handler(switch=False):
    '''switch отвечает за то, чтобы запросы не повторялись. Если switch == false, то отправленные статьи могут повторяться
    если же switch == True, то данные удаляются с to_order json
    '''
    if switch == False:
        # new_copy = copy.deepcopy(data)
        # with open('to_order.json', 'w', encoding='utf-8') as file:
        #     json.dump(new_copy, file, indent=4, ensure_ascii=False)

        with open('to_order.json', 'r', encoding='utf-8') as file:
            json_data = file.read()
            new_data = json.loads(json_data)

            return new_data(str(randint(1, 926)))

    else:
        # new_copy = copy.deepcopy(data)
        # with open('to_order.json', 'w', encoding='utf-8') as file:
        #     json.dump(new_copy, file, indent=4, ensure_ascii=False)

        with open('to_order.json', 'r', encoding='utf-8') as file:
            json_data = file.read()
            new_data = json.loads(json_data)

            '''если статьи закончились'''
            if len(data) == 0:
                return 'в базе не осталось статей'

        index = str(randint(1, 926))

        # после этого комментария идет финальная версия

        # forwarding_message = new_data[index]
        #
        # del new_data[index]
        # with open('to_order.json', 'w', encoding='utf-8') as file:
        #     json.dump(new_data, file, indent=4, ensure_ascii=False)

        return new_data[index]

