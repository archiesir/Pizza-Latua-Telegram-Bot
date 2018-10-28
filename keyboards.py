# -*- coding: utf-8 -*-

from telebot import types

import product


def main_menu():
    key_main_menu = types.ReplyKeyboardMarkup(True, True)
    key_main_menu.row('🍴 Меню', '📥 Корзина')
    key_main_menu.row('🛎 Заказы', '📢 Новости')
    key_main_menu.row('🚀 Доставка', '☎ Контакты')
    return key_main_menu


def categories():
    key_categories = types.ReplyKeyboardMarkup(True, True)
    key_categories.row('🏠 Начало', '📥 Корзина')  # Главное меню
    key_categories.row('🍕 Пицца', '🍔 Бургеры')
    key_categories.row('🍹 Напитки', '🍝 Паста')
    key_categories.row('🥗 Салаты', '🥘 Супы')
    key_categories.row('🍽 Прочие блюда')
    return key_categories


def pizza():
    key_pizza = types.ReplyKeyboardMarkup(True, row_width=3)
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
    key_amount = types.ReplyKeyboardMarkup(True, True)
    amount_btn = types.InlineKeyboardButton('')
    key_amount.row('+1', '+2', '+5')  # Главное меню
    return key_amount