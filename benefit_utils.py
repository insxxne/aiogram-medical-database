import copy
import pprint

from parse_part import data
from random import randint
import json


def handler(switch=False):
    if switch == False:
        pass
    else:
        # new_copy = copy.deepcopy(data)
        # with open('to_order.json', 'w', encoding='utf-8') as file:
        #     json.dump(new_copy, file, indent=4, ensure_ascii=False)

        with open('to_order.json', 'r', encoding='utf-8') as file:
            json_data = file.read()
            new_data = json.loads(json_data)

        index = str(randint(1, 926))

        # после этого комментария идет финальная версия

        # forwarding_message = new_data[index]
        #
        # del new_data[index]
        # with open('to_order.json', 'w', encoding='utf-8') as file:
        #     json.dump(new_data, file, indent=4, ensure_ascii=False)

        return new_data[index]

