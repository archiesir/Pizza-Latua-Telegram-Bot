# -*- coding: utf-8 -*-
import types

import telebot
import config
import product
import states
import db
import keyboards
import urllib.request as urllib2
from config import States
import messages
from messages import Messages

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    bot.send_message(message.chat.id, Messages.WELCOME.value.format(message.chat.first_name),
                     reply_markup=keyboards.main_menu())
    states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    db.add_username(message.chat.id, message.chat.username)


@bot.message_handler(commands=['menu'])
def cmd_menu(message):
    bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                     reply_markup=keyboards.categories())
    states.set_state(message.chat.id, States.S_MENU.value)


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_MAIN_MENU.value)
def main_menu(message):
    if message.text == '☎ Контакты':
        bot.send_message(message.chat.id, Messages.CONTACTS.value,
                         reply_markup=keyboards.main_menu())
    elif message.text == '🚀 Доставка':
        bot.send_message(message.chat.id, Messages.DELIVERY.value,
                         parse_mode='HTML',
                         reply_markup=keyboards.main_menu())
    elif message.text == '📢 Новости':
        bot.send_message(message.chat.id, Messages.NEWS.value,
                         reply_markup=keyboards.main_menu())
    elif message.text == '🍴 Меню':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    else:
        bot.send_message(message.chat.id, 'Неизвесная команда!\n'
                                          'Попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_MENU.value)
def categories_menu(message):
    if message.text == '🍕 Пицца':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.pizza())
        states.set_state(message.chat.id, States.S_PIZZA_MENU.value)
    elif message.text == '🍔 Бургеры':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.burger())
        states.set_state(message.chat.id, States.S_BURGER_MENU.value)
    elif message.text == '🍹 Напитки':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.drinks())
        states.set_state(message.chat.id, States.S_DRINKS_MENU.value)
    elif message.text == '🍝 Паста':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.pasta())
        states.set_state(message.chat.id, States.S_PASTA_MENU.value)
    elif message.text == '🥗 Салаты':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.salad())
        states.set_state(message.chat.id, States.S_SALAD_MENU.value)
    elif message.text == '🥘 Супы':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.soup())
        states.set_state(message.chat.id, States.S_SOUP_MENU.value)
    elif message.text == '🍽 Прочие блюда':
        bot.send_message(message.chat.id, 'Выберите блюдо 👇🏻', reply_markup=keyboards.others())
        states.set_state(message.chat.id, States.S_OTHER_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML', reply_markup=keyboards.basket())
    else:
        bot.send_message(message.chat.id, 'Неизвесная команда!\n'
                                          'Попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_PIZZA_MENU.value)
def pizza_menu(message):
    for p in product.get_pizza_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_pizza_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/pizza.jpg')
                img = open('cache/pizza.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/pizza_two.jpg')
                img = open('cache/pizza_two.jpg', 'rb')

            product_ = product.get_pizza_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_pizza_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_BURGER_MENU.value)
def burger_menu(message):
    for p in product.get_burger_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_burger_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/burger.jpg')
                img = open('cache/burger.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/burger_two.jpg')
                img = open('cache/burger_two.jpg', 'rb')

            product_ = product.get_burger_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_burger_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_DRINKS_MENU.value)
def drinks_menu(message):
    for p in product.get_drinks_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_drinks_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/drinks.jpg')
                img = open('cache/drinks.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/drinks_two.jpg')
                img = open('cache/drinks_two.jpg', 'rb')

            product_ = product.get_drinks_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_drinks_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_PASTA_MENU.value)
def pasta_menu(message):
    for p in product.get_pasta_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_pasta_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/pasta.jpg')
                img = open('cache/pasta.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/pasta_two.jpg')
                img = open('cache/pasta_two.jpg', 'rb')

            product_ = product.get_pasta_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_pasta_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_SALAD_MENU.value)
def salad_menu(message):
    for p in product.get_salad_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_salad_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/salad.jpg')
                img = open('cache/salad.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/salad_two.jpg')
                img = open('cache/salad_two.jpg', 'rb')

            product_ = product.get_salad_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_salad_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_SOUP_MENU.value)
def soup_menu(message):
    for p in product.get_soup_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_soup_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/soup.jpg')
                img = open('cache/soup.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/soup_two.jpg')
                img = open('cache/soup_two.jpg', 'rb')

            product_ = product.get_soup_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_soup_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_OTHER_MENU.value)
def others_menu(message):
    for p in product.get_others_titles():
        if message.text == p:
            bot.send_chat_action(message.chat.id, 'upload_photo')

            img_url = product.get_others_by_title(message.text)['picture']
            try:
                urllib2.urlretrieve(img_url, 'cache/other.jpg')
                img = open('cache/other.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/other_two.jpg')
                img = open('cache/other_two.jpg', 'rb')

            product_ = product.get_others_by_title(message.text)
            bot.send_message(message.chat.id, 'Ваш продукт: ', reply_markup=keyboards.keyboard_hide)
            bot.send_photo(message.chat.id, img, messages.product_data(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()
            db.add_order(message.chat.id,
                         message.text,
                         product_['comp'],
                         product_['price'],
                         product_['picture'])
            db.set_cache(message.chat.id, message.text)

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        db.delete_empty_orders(message.chat.id)
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_empty_orders(message.chat.id)
    elif message.text == '📥 Корзина':
        bot.send_message(message.chat.id, messages.basket(message.chat.id), parse_mode='HTML',
                         reply_markup=keyboards.basket())
    elif not product.get_others_by_title(message.text)['title']:
        bot.send_message(message.chat.id, 'Неизвесное название продукта попробуйте другое!\n'
                                          'Или попробуйте /start или /help')


@bot.callback_query_handler(func=lambda call: True)
def add_to_basket(call):
    state = states.get_current_state(call.message.chat.id)
    if call.data == 'add_to_basket':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                      reply_markup=keyboards.chose_amount())
        bot.answer_callback_query(call.id, 'Выберите колличество')
        states.set_state(call.message.chat.id, States.S_CHOSE_AMOUNT.value)

    elif call.data == 'back_to_menu':
        bot.answer_callback_query(call.id, '⬅ Назад')
        bot.send_message(call.message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(call.message.chat.id, States.S_MENU.value)
    elif call.data == 'back':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                      reply_markup=keyboards.add_to_basket())
        bot.answer_callback_query(call.id, '⬅ Назад')
        bot.send_message(call.message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(call.message.chat.id, States.S_MENU.value)
        db.delete_empty_orders(call.message.chat.id)
    elif call.data == 'chose_amount':
        bot.answer_callback_query(call.id, 'Выберите колличество')

    elif state == States.S_CHOSE_AMOUNT.value:
        title = db.get_cache(call.message.chat.id)
        if call.data == '1':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 1
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '2':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 2
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '3':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 3
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '4':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 4
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '5':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 5
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '6':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 6
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '7':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 7
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '8':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 8
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
        elif call.data == '9':
            sum = db.get_orders_by_chat_id_and_title(call.message.chat.id, title)[0][2] + 9
            db.edit_order_amount(call.message.chat.id, title, sum)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                          reply_markup=keyboards.add_to_basket())
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
            states.set_state(call.message.chat.id, States.S_MENU.value)
    elif call.data == 'clear_basket':
        db.clear_basket(call.message.chat.id)
        bot.answer_callback_query(call.id, '✅ Корзина очищена')
        bot.send_message(call.message.chat.id, 'Корзина очищена ✅ \n\nВыберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(call.message.chat.id, States.S_MENU.value)
    elif call.data == 'reg_order':
        try:
            orders = db.get_orders_by_chat_id(call.message.chat.id)
            sum = 0
            for o in orders:
                sum = sum + o[5] * o[2]
        except:
            sum = 0
        if sum <= 0:
            bot.answer_callback_query(call.id, '❌ Не доступно')
            bot.send_message(call.message.chat.id, 'Минимальная сумма заказа должна быть больше чем 0 руб.')
        else:
            bot.answer_callback_query(call.id, '✅ Выберите вид доставки')
            bot.send_message(call.message.chat.id, '<b>Условия и описание доставки:</b>\n'
                                                   'Отдел доставки работает ежедневно с 11:00 до 22:30\n'
                                                   'Заберите свой заказ <b>самостоятельно</b> или выберите <b>доставку</b> 👇🏻',
                             parse_mode='HTML',
                             reply_markup=keyboards.check_delivery())
            states.set_state(call.message.chat.id, States.S_DELIVERY.value)
            orders = db.get_orders_by_chat_id(call.message.chat.id)
            sum = 0
            description = ''
            for o in orders:
                description = description + o[3] + ' — ' + str(o[2]) + ' шт. = ' + str(o[5]*o[2]) + ' руб.; '
            for o in orders:
                sum = sum + o[5]*o[2]

            db.add_reg_order(call.message.chat.id, description, sum)


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_DELIVERY.value)
def delivery_menu(message):
    if message.text == '🚖 Доставка':
        bot.send_message(message.chat.id, '<b>Куда нужно доставить?</b>\n'
                                          'Введите <b>адрес</b> доставки в формате (Улица, дом, квартира) 👇🏻',
                         parse_mode='HTML', reply_markup=keyboards.back_keyboard())
        states.set_state(message.chat.id, States.S_GEOPOSITION.value)
        db.edit_self_delivery(message.chat.id, True)
    elif message.text == '🏃 Самовывоз':
        bot.send_message(message.chat.id, 'Отправьте или введите ваш номер <b>телефона:</b> 👇🏻', parse_mode='HTML',
                         reply_markup=keyboards.check_phone_number())
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_false_reg_orders(message.chat.id)
    elif message.text == '⬅ Назад':
        bot.send_message(message.chat.id, '<b>Условия и описание доставки:</b>\n'
                                          'Отдел доставки работает ежедневно с 11:00 до 22:30\n'
                                          'Заберите свой заказ <b>самостоятельно</b> или выберите <b>доставку</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.check_delivery())
        states.set_state(message.chat.id, States.S_DELIVERY.value)
    else:
        bot.send_message(message.chat.id, 'Неизвесная команда!\n'
                                          'Попробуйте /start или /help')


@bot.message_handler(content_types=['location'])
def geo_menu(message):
    print(message.location.longitude)
    print(message.location.latitude)


@bot.message_handler(content_types=['contact'])
def phone_menu(message):
    db.add_phone_number(message.chat.id, message.contact.phone_number)
    db.add_phone_number_reg_order(message.chat.id, message.contact.phone_number)
    bot.send_message(message.chat.id, '<b>Когда хотите получить заказ?</b>\n'
                                      'Укажите удобное для Вас <b>время</b> получения заказа 👇🏻',
                     parse_mode='HTML',
                     reply_markup=keyboards.check_time())
    states.set_state(message.chat.id, States.S_TIME.value)


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_GEOPOSITION.value)
def geoposition_menu(message):
    if message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_false_reg_orders(message.chat.id)
    elif message.text == '⬅ Назад':
        bot.send_message(message.chat.id, '<b>Условия и описание доставки:</b>\n'
                                          'Отдел доставки работает ежедневно с 11:00 до 22:30\n'
                                          'Заберите свой заказ <b>самостоятельно</b> или выберите <b>доставку</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.check_delivery())
        states.set_state(message.chat.id, States.S_DELIVERY.value)
        db.edit_self_delivery(message.chat.id, False)
    else:
        db.add_geoposition_reg_order(message.chat.id, message.text)
        bot.send_message(message.chat.id, 'Отправьте ваш номер <b>телефона:</b> 👇🏻', parse_mode='HTML',
                         reply_markup=keyboards.check_phone_number())


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_TIME.value)
def time_menu(message):
    if message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_false_reg_orders(message.chat.id)
    elif message.text == '⬅ Назад':
        bot.send_message(message.chat.id, '<b>Условия и описание доставки:</b>\n'
                                          'Отдел доставки работает ежедневно с 11:00 до 22:30\n'
                                          'Заберите свой заказ <b>самостоятельно</b> или выберите <b>доставку</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.check_delivery())
        states.set_state(message.chat.id, States.S_DELIVERY.value)
    else:
        db.add_time(message.chat.id, message.text)
        bot.send_message(message.chat.id, '<b>Оставьте комментарии к заказу и адресу</b>\n'
                                          'Например: точное время доставки, номер'
                                          'подъезда, код домофона, номер этажа,'
                                          'ориентиры, а также пожелания к заказу 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.comments_key())
        states.set_state(message.chat.id, States.S_COMMENTS.value)


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_COMMENTS.value)
def comments_menu(message):
    if message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_false_reg_orders(message.chat.id)
    elif message.text == '⬅ Назад':
        bot.send_message(message.chat.id, '<b>Условия и описание доставки:</b>\n'
                                          'Отдел доставки работает ежедневно с 11:00 до 22:30\n'
                                          'Заберите свой заказ <b>самостоятельно</b> или выберите <b>доставку</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.check_delivery())
        states.set_state(message.chat.id, States.S_DELIVERY.value)
    elif message.text == '➡ Продолжить':
        bot.send_message(message.chat.id, 'Выберите удобный для Вас <b>метод оплаты:</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.payments_key())
    else:
        bot.send_message(message.chat.id, 'Выберите удобный для Вас <b>метод оплаты:</b> 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.payments_key())
        db.add_comments(message.chat.id, message.text)


@bot.message_handler(func=lambda message: states.get_current_state(message.chat.id) == States.S_PAYMENTS.value)
def payments_menu(message):
    if message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
        db.delete_false_reg_orders(message.chat.id)
    elif message.text == '⬅ Назад':
        bot.send_message(message.chat.id, '<b>Оставьте комментарии к заказу и адресу</b>\n'
                                          'Например: точное время доставки, номер'
                                          'подъезда, код домофона, номер этажа,'
                                          'ориентиры, а также пожелания к заказу 👇🏻',
                         parse_mode='HTML',
                         reply_markup=keyboards.comments_key())
        states.set_state(message.chat.id, States.S_COMMENTS.value)


bot.polling()
