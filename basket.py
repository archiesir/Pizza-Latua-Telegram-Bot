# -*- coding: utf-8 -*-

import json


def add_product_to_basket(chat_id, title, comp, price, picture, amount):
    product_info = ({'chat_id': chat_id,
                    'title': title,
                    'comp': comp,
                    'price': price,
                    'picture': picture,
                    'amount': amount})
    file_name = 'users_data/' + str(chat_id) + '.json'
    try:
        user_file = open(file_name, mode='a')
    except:
        user_file = open(file_name, mode='w')
    json.dump(product_info, user_file)
    user_file.close()


add_product_to_basket(182552976, '«Деревенская»', 'Состав: Соус медово-горчичный, картофель по-деревенски, курица маринованная, лук красный, огурцы маринованные, соус фирменный, моцарелла, грибы', 123, 'https://avatars3.githubusercontent.com/u/30303225?s=60&v=4', 10)


def get_basket(chat_id):
    file_name = 'users_data/' + str(chat_id) + '.json'
    user_file = open(file_name).read()
    user_data = json.load({user_file})

    return {user_data}


print(get_basket(182552976))
