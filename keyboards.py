# -*- coding: utf-8 -*-

from telebot import types

import product

keyboard_hide = types.ReplyKeyboardRemove()


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
    key_pizza = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_pizza.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_pizza_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_pizza.add(btn)
    return key_pizza


def burger():
    key_burger = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_burger.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_burger_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_burger.add(btn)
    return key_burger


def drinks():
    key_drinks = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_drinks.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_drinks_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_drinks.add(btn)
    return key_drinks


def pasta():
    key_pasta = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_pasta.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_pasta_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_pasta.add(btn)
    return key_pasta


def salad():
    key_salad = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_salad.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_salad_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_salad.add(btn)
    return key_salad


def soup():
    key_soup = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_soup.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_soup_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_soup.add(btn)
    return key_soup


def others():
    key_other = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton('⬅ Назад')
    main_menu_btn = types.KeyboardButton('🏠 Начало')
    basket_btn = types.KeyboardButton('📥 Корзина')
    key_other.add(back_btn, main_menu_btn, basket_btn)

    for p in product.get_others_titles():
        btn = types.KeyboardButton('{}'.format(p))
        key_other.add(btn)
    return key_other


def add_to_basket():
    key_basket = types.InlineKeyboardMarkup()
    basket_btn = types.InlineKeyboardButton(text='📥 Добавить в корзину', callback_data='add_to_basket')
    back_btn = types.InlineKeyboardButton(text='⬅ Назад', callback_data='back_to_menu')
    key_basket.add(basket_btn)
    key_basket.add(back_btn)
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


def basket():
    basket_key = types.InlineKeyboardMarkup()
    clear_btn = types.InlineKeyboardButton(text='❌ Очистить корзину', callback_data='clear_basket')
    reg_btn = types.InlineKeyboardButton(text='✅ Оформить заказ?', callback_data='reg_order')
    basket_key.add(clear_btn)
    basket_key.add(reg_btn)
    return basket_key


def check_delivery():
    key_delivery = types.ReplyKeyboardMarkup(True)
    deliver_btn = types.KeyboardButton('🚖 Доставка')
    self_btn = types.KeyboardButton('🏃 Самовывоз')
    key_delivery.add(deliver_btn, self_btn)
    key_delivery.row('🏠 Начало')
    return key_delivery


def check_geo():
    key_geo = types.ReplyKeyboardMarkup(True)
    geo_btn = types.KeyboardButton(text='📌 отправить геолокацию', request_location=True)
    key_geo.add(geo_btn)
    key_geo.row('⬅ Назад', '🏠 Начало')
    return key_geo


def check_phone_number():
    key_number = types.ReplyKeyboardMarkup(True)
    num_btn = types.KeyboardButton(text='📱 отправить номер', request_contact=True)
    key_number.add(num_btn)
    key_number.row('⬅ Назад', '🏠 Начало')
    return key_number


def check_time():
    key_number = types.ReplyKeyboardMarkup(True)
    num_btn = types.KeyboardButton(text='В ближайшее время')
    key_number.add(num_btn)
    key_number.row('⬅ Назад', '🏠 Начало')
    return key_number


def comments_key():
    key_number = types.ReplyKeyboardMarkup(True)
    num_btn = types.KeyboardButton(text='➡ Продолжить')
    key_number.add(num_btn)
    key_number.row('⬅ Назад', '🏠 Начало')
    return key_number


def payments_key():
    key_number = types.ReplyKeyboardMarkup(True)
    first_btn = types.KeyboardButton(text='💵 Наличные')
    second_btn = types.KeyboardButton(text='💳 Безнал (Yandex Money)')
    key_number.add(first_btn)
    key_number.add(second_btn)
    key_number.row('⬅ Назад', '🏠 Начало')
    return key_number


def back_keyboard():
    back_key = types.ReplyKeyboardMarkup(True)
    back_btn = types.KeyboardButton(text='⬅ Назад')
    back_key.add(back_btn)
    return back_key