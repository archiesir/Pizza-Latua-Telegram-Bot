# -*- coding: utf-8 -*-

from enum import Enum


# BOT TOKEN FROM "BotFather:
token = '771779902:AAFpLvV5as0nr7zTWUmyDg3lheqByaOgKpg'


# ROBOKASSA SETTINGS
mrh_login = "LaTua"
mrh_pass1 = "DYQ0h44nHN9YjveTeq6b"
inv_id = 0
inv_desc = ""
out_summ = ""
IsTest = 1


# DATABASE SETTINGS
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "shop_bot"


# USER STATES - DON'T TOUCH!!!!!
class States(Enum):
    S_START = "0"
    S_MAIN_MENU = "1"
    S_MENU = "2"
    S_PIZZA_MENU = "3"
    S_BURGER_MENU = "4"
    S_DRINKS_MENU = "5"
    S_PASTA_MENU = "6"
    S_SALAD_MENU = "7"
    S_SOUP_MENU = "8"
    S_OTHER_MENU = "9"
    S_CHOSE_AMOUNT = "10"
    S_CHOSE_PIZZA_WEIGHT = "11"
    S_BASKET = "12"
    S_DELIVERY = '13'
    S_PHONE_NUMBER = '15'
    S_GEOPOSITION = '16'
    S_TIME = '17'
    S_COMMENTS = '18'
    S_PAYMENTS = '19'
    S_YANDEX_PAYMENT = '20'
