# -*- coding: utf-8 -*-

from telebot import types

import product


def main_menu():
    key_main_menu = types.ReplyKeyboardMarkup(True)
    key_main_menu.row('🍴 Меню', '📥 Корзина')
    key_main_menu.row('🛎 Заказы', '📢 Новости')
    key_main_menu.row('🚀 Доставка', '☎ Контакты')
    return key_main_menu


def categories():
    key_categories = types.ReplyKeyboardMarkup(True)
    key_categories.row('🏠 Начало', '📥 Корзина')
    key_categories.row('🍕 Пицца', '🍔 Бургеры')
    key_categories.row('🍹 Напитки', '🍝 Паста')
    key_categories.row('🥗 Салаты', '🥘 Супы')
    key_categories.row('🍽 Прочие блюда')
    return key_categories


def pizza():
    key_pizza = types.ReplyKeyboardMarkup(True, True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_pizza.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_pizza_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_pizza.add(btn)
    return key_pizza


def burger():
    pass


def drinks():
    pass


def pasta():
    pass


def salad():
    pass


def soup():
    pass


def amount():
    key_amount = types.InlineKeyboardMarkup(True, True)
    key_amount.row('1', '2', '3', '4')
    key_amount.row('5', '6', '7', '8')
    key_amount.row('9', '10', '11', '12')
    return key_amount


def add_to_basket():
    key_basket = types.InlineKeyboardMarkup()
    basket_btn = types.InlineKeyboardButton(text='📥 Добавить в корзину', callback_data='add_to_basket')
    key_basket.add(basket_btn)
    return key_basket


def chose_amount():
    chose_amount_key = types.InlineKeyboardMarkup()
    one_btn = types.InlineKeyboardButton(text='1', callback_data='1')
    two_btn = types.InlineKeyboardButton(text='2', callback_data='2')
    three_btn = types.InlineKeyboardButton(text='3', callback_data='3')
    four_btn = types.InlineKeyboardButton(text='4', callback_data='4')
    five_btn = types.InlineKeyboardButton(text='5', callback_data='5')
    six_btn = types.InlineKeyboardButton(text='6', callback_data='6')
    seven_btn = types.InlineKeyboardButton(text='7', callback_data='7')
    eight_btn = types.InlineKeyboardButton(text='8', callback_data='8')
    nine_btn = types.InlineKeyboardButton(text='9', callback_data='9')
    chose_btn = types.InlineKeyboardButton(text='Выберите колличество', callback_data='chose_amount')
    back_btn = types.InlineKeyboardButton(text='⬅ Назад', callback_data='back')
    chose_amount_key.add(chose_btn)
    chose_amount_key.add(one_btn, two_btn,three_btn)
    chose_amount_key.add(four_btn, five_btn, six_btn)
    chose_amount_key.add(seven_btn, eight_btn, nine_btn)
    chose_amount_key.add(back_btn)
    return chose_amount_key


keyboard_hide = types.ReplyKeyboardRemove()
