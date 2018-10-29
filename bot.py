# -*- coding: utf-8 -*-

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
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_pizza_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_burger_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_drinks_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_pasta_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_salad_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_salad_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
                urllib2.urlretrieve(img_url, 'cache/picture_for_send.jpg')
                img = open('cache/picture_for_send.jpg', 'rb')
            except:
                urllib2.urlretrieve(img_url, 'cache/picture_for_send_two.jpg')
                img = open('cache/picture_for_send_two.jpg', 'rb')

            product_ = product.get_others_by_title(message.text)
            bot.send_photo(message.chat.id, img, messages.product_info(product_), parse_mode='HTML',
                           reply_markup=keyboards.add_to_basket())
            img.close()

    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(message.chat.id, States.S_MENU.value)
    elif message.text == '🏠 Начало':
        bot.send_message(message.chat.id, '🏠 Главное меню', reply_markup=keyboards.main_menu())
        states.set_state(message.chat.id, States.S_MAIN_MENU.value)
    elif message.text == '📥 Корзина':
        pass
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
    elif call.data == 'back':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                      reply_markup=keyboards.add_to_basket())
        bot.answer_callback_query(call.id, '⬅ Назад')
        bot.send_message(call.message.chat.id, 'Выберите раздел, чтобы вывести список блюд 👇🏻',
                         reply_markup=keyboards.categories())
        states.set_state(call.message.chat.id, States.S_MENU.value)
    elif call.data == 'chose_amount':
        bot.answer_callback_query(call.id, 'Выберите колличество')
    elif state == States.S_CHOSE_AMOUNT.value:
        if call.data == '1':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '2':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '3':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '4':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '5':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '6':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '7':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '8':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')
        elif call.data == '9':
            bot.answer_callback_query(call.id, '✅ Успешно добавлено в корзину')


bot.polling()
