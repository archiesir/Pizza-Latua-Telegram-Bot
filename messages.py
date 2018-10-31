# -*- coding: utf-8 -*-

from enum import Enum

import db


def product_data(product):
    title = product['title']
    price = product['price']

    if not product['comp']:
        output = '<b>{}</b>\n\n' \
                 '<b>Цена: {} руб.</b>'.format(title, price)
    else:
        comp = product['comp']
        output = '<b>{}</b>\n\n' \
                 '{}\n\n' \
                 '<b>Цена: {} руб.</b>'.format(title, comp, price)
    return output


def basket(chat_id):
    db.delete_empty_orders(chat_id)
    orders = db.get_orders_by_chat_id(chat_id)
    sum = 0
    output = '<b>📥 Корзина:</b>\n\n'
    for o in orders:
        output = output + o[3] + ' — ' + str(o[2]) + ' шт. = ' + str(o[5]*o[2]) + ' руб.' + '\n\n'
    for o in orders:
        sum = sum + o[5]*o[2]
    output = output + '<b>Общая сумма: ' + str(sum) + ' руб.</b>'
    if sum == 0:
        output = 'Минимальная сумма заказа должна быть больше чем 0 руб.'
    return output


class Messages(Enum):
    WELCOME = 'Добро пожаловать, {}. \n' \
              'Мы рады приветсвовать вас в нашем боте для доставки еды. \nВ случае ' \
              'возникновения вопросов, звониите по номеру \n+99 999 999 99 99 '

    DELIVERY = '<b>Условия и описание доставки:</b>\n' \
               'Отдел доставки работает ежедневно с nn:nn до nn:nn'

    CONTACTS = '🏴 Здесь будут контакты'

    NEWS = '📢 Здесь будут новости'
