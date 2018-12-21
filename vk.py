# -*- coding: utf-8 -*-

import sys
import os
import argparse
import datetime
from getpass import getpass
import vk_api

user = 'kudesnick@inbox.ru'
password = getpass('input password:')

owner_id = '-175443750'

# https://vk.com/wall-40911268_479 #08.04.2018
# https://vk.com/wall-40911268_507
# https://vk.com/wall-40911268_551
# https://vk.com/wall-40911268_555
# https://vk.com/wall-40911268_610
# https://vk.com/wall-40911268_617
# https://vk.com/wall-40911268_684
# https://vk.com/wall-40911268_741
# https://vk.com/wall-40911268_789
# https://vk.com/wall-40911268_825
# https://vk.com/wall-40911268_832
# https://vk.com/wall-40911268_836
# https://vk.com/wall-40911268_855
# https://vk.com/wall-40911268_898
# https://vk.com/wall-40911268_933
# https://vk.com/wall-40911268_954
# https://vk.com/wall-40911268_964
# https://vk.com/wall-40911268_991
# https://vk.com/wall-40911268_997
# https://vk.com/wall-40911268_999 #21.12.2018

posts_id = {'-40911268_479': {'publish_date': datetime.datetime(2018, 12, 21, 23, 17)},
            '-40911268_507': {'publish_date': datetime.datetime(2018, 12, 22,  9, 11)},
            '-40911268_551': {'publish_date': datetime.datetime(2018, 12, 22, 21, 24)},
            '-40911268_555': {'publish_date': datetime.datetime(2018, 12, 23, 12, 43)},
            '-40911268_610': {'publish_date': datetime.datetime(2018, 12, 23, 20, 35)},
            '-40911268_617': {'publish_date': datetime.datetime(2018, 12, 24,  9, 18)},
            '-40911268_684': {'publish_date': datetime.datetime(2018, 12, 24, 21, 52)},
            '-40911268_741': {'publish_date': datetime.datetime(2018, 12, 25, 10, 31)},
            '-40911268_789': {'publish_date': datetime.datetime(2018, 12, 25, 22,  8)},
            '-40911268_825': {'publish_date': datetime.datetime(2018, 12, 26,  9, 42)},
            '-40911268_832': {'publish_date': datetime.datetime(2018, 12, 26, 21, 29)},
            '-40911268_836': {'publish_date': datetime.datetime(2018, 12, 27, 10, 21)},
            '-40911268_855': {'publish_date': datetime.datetime(2018, 12, 27, 22, 37)},
            '-40911268_898': {'publish_date': datetime.datetime(2018, 12, 28,  9, 11)},
            '-40911268_933': {'publish_date': datetime.datetime(2018, 12, 28, 21, 19)},
            '-40911268_954': {'publish_date': datetime.datetime(2018, 12, 29, 12, 15)},
            '-40911268_964': {'publish_date': datetime.datetime(2018, 12, 29, 20, 46)},
            '-40911268_991': {'publish_date': datetime.datetime(2018, 12, 30, 11, 54)},
            '-40911268_997': {'publish_date': datetime.datetime(2018, 12, 30, 19, 41)},
            '-40911268_999': {'publish_date': datetime.datetime(2018, 12, 31, 10, 11)}
            };

add_to_header = ''
add_to_footer = '''
@club40911268 (© Амариэ /Мария Гуцол/)

Когда: 7 января в 19:00
Где: кафе-бар "KUNST" (Итальянская ул., 37)
Начало в 19:00
Вход: свободный'''

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def attachments(attachs):
    results = []
    for att in attachs:
        type_name = att['type']
        results.append(type_name + str(att[type_name]['owner_id']) + '_' + str(att[type_name]['id']))
        
    return results


#vk_session = vk_api.VkApi(user, password, auth_handler = auth_handler)
vk_session = vk_api.VkApi(user, password)
vk_session.auth()

vk = vk_session.get_api()

for k, v in posts_id.items():
    posts_id[k]['data'] = vk.wall.getById(posts = k)[0]

for k, v in posts_id.items():
    result = vk.wall.post(
        owner_id = owner_id,
        from_group = 1,
        message = '\n'.join([add_to_header, v['data']['text'], add_to_footer]),
        attachments = ','.join(attachments(v['data']['attachments'])),
        publish_date = v['publish_date'].timestamp()
        )

    print(result)

os.system('pause')
