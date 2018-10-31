# -*- coding: utf-8 -*-

import pymysql
import config


def get_all_users():
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    output = cursor.fetchall()

    connection.commit()
    connection.close()
    return output


def get_user(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    output = cursor.fetchall()

    connection.commit()
    connection.close()
    return output


def add_user(chat_id, state):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "INSERT INTO users(chat_id, state) VALUES(\'{}\', \'{}\')".format(chat_id, state)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_username(chat_id, user_name):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE users SET user_name = \'{}\' WHERE chat_id = \'{}\'".format(user_name, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_phone_number(chat_id, phone_number):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE users SET phone_number = \'{}\' WHERE chat_id = \'{}\'".format(phone_number, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_order(chat_id, title, comp, price, picture):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    delete_empty_orders(chat_id)
    sql = "INSERT INTO orders(chat_id, title, comp, price, picture) VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')".format(
        chat_id, title, comp, price, picture)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def edit_order_amount(chat_id, title, amount):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE orders SET amount = \'{}\' WHERE chat_id = \'{}\' AND title = \'{}\'".format(amount, chat_id, title)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def get_cache(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT cache FROM users WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    output = cursor.fetchall()

    connection.commit()
    connection.close()
    return output[0][0]


def set_cache(chat_id, cache):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE users SET cache = \'{}\' WHERE chat_id = \'{}\'".format(cache, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def get_orders_by_chat_id(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM orders WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    output = cursor.fetchall()

    connection.commit()
    connection.close()
    return output


def get_orders_by_chat_id_and_title(chat_id, title):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM orders WHERE chat_id = \'{}\' AND title = \'{}\'".format(chat_id, title)
    cursor.execute(sql)
    output = cursor.fetchall()

    connection.commit()
    connection.close()
    return output


def clear_basket(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "DELETE FROM orders WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    connection.commit()
    connection.close()


def delete_empty_orders(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "DELETE FROM orders WHERE amount = \'{}\' AND chat_id = \'{}\'".format(0, chat_id)
    cursor.execute(sql)
    connection.commit()
    connection.close()


def add_reg_order(chat_id, description, price):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    delete_false_reg_orders(chat_id)
    sql = "INSERT INTO reg_orders(chat_id, description, price) VALUES(\'{}\', \'{}\', \'{}\')".format(chat_id, description, price)
    cursor.execute(sql)

    connection.commit()
    connection.close()




def add_phone_number_reg_order(chat_id, phone_number):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE reg_orders SET phone_number = \'{}\' WHERE chat_id = \'{}\'".format(phone_number, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_geoposition_reg_order(chat_id, geoposition):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE reg_orders SET geopisition = \'{}\' WHERE chat_id = \'{}\'".format(geoposition, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def delete_false_reg_orders(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "DELETE FROM reg_orders WHERE ordered = \'{}\' AND chat_id = \'{}\'".format(0, chat_id)
    cursor.execute(sql)
    connection.commit()
    connection.close()


def edit_self_delivery(chat_id, self_delivery):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    input = '0'
    if self_delivery:
        input = '1'
    sql = "UPDATE reg_orders SET self_delivery = \'{}\' WHERE chat_id = \'{}\'".format(input, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_geoposition_reg_order(chat_id, geoposition):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE reg_orders SET geopisition = \'{}\' WHERE chat_id = \'{}\'".format(geoposition, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_time(chat_id, time):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE reg_orders SET time = \'{}\' WHERE chat_id = \'{}\'".format(time, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()


def add_comments(chat_id, comments):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "UPDATE reg_orders SET comments = \'{}\' WHERE chat_id = \'{}\'".format(comments, chat_id)
    cursor.execute(sql)

    connection.commit()
    connection.close()
