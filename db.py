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
    sql = "SELECT * FROM users WHERE chat_id = \'{}\'".format(user_name)
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