# -*- coding: utf-8 -*-

import pymysql
import db
import config


def get_current_state(chat_id):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    states = cursor.fetchall()

    if states != ():
        state = str(states[0][2])
    else:
        state = config.States.S_START.value

    connection.commit()
    connection.close()
    return state


def set_state(chat_id, state):
    connection = pymysql.connect(host=config.db_host,
                                 user=config.db_user,
                                 password=config.db_password,
                                 db=config.db_name,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE chat_id = \'{}\'".format(chat_id)
    cursor.execute(sql)
    states = cursor.fetchall()

    if states != ():
        sql = "UPDATE users SET state = \'{}\' WHERE chat_id = \'{}\'".format(str(state), chat_id)
        cursor.execute(sql)
    else:
        db.add_user(chat_id, state)

    connection.commit()
    connection.close()
